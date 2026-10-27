#!/usr/bin/env python3
"""pynano: a small nano-style terminal text editor, built on curses.

Usage:  python pynano.py [FILE]
Requires Python 3.10+ (uses ``match`` statements).
Requires cursers, not available on Windows by default
(.venv) py -m pip install windows-curses
"""

from __future__ import annotations

import argparse
import curses
import os
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

TAB_WIDTH = 4
MIN_HEIGHT = 6

SHORTCUTS: tuple[tuple[tuple[str, str], ...], ...] = (
    (("^G", "Help"), ("^O", "Write Out"), ("^W", "Where Is"), ("^K", "Cut"), ("^C", "Location")),
    (("^X", "Exit"), ("^U", "Paste"), ("^A", "Home"), ("^E", "End"), ("^V", "Page Dn")),
)

HELP_TEXT: tuple[str, ...] = (
    "pynano help",
    "",
    "^G  Show this help          ^O  Write the buffer to disk",
    "^X  Exit (asks to save)     ^W  Search (case-insensitive)",
    "^K  Cut current line        ^U  Paste cut lines",
    "^C  Show cursor location    ^A / ^E  Start / end of line",
    "^Y / PgUp  Page up          ^V / PgDn  Page down",
    "",
    "Arrow keys, Home, End, Delete and Backspace work as expected.",
    "Tabs are inserted as spaces.",
    "",
    "Press any key to return.",
)


class Key(IntEnum):
    """Control-key codes as delivered by curses in raw mode."""

    CTRL_A = 1
    CTRL_C = 3
    CTRL_E = 5
    CTRL_G = 7
    BACKSPACE_H = 8
    TAB = 9
    NEWLINE = 10
    CTRL_K = 11
    RETURN = 13
    CTRL_O = 15
    CTRL_U = 21
    CTRL_V = 22
    CTRL_W = 23
    CTRL_X = 24
    CTRL_Y = 25
    ESCAPE = 27
    DELETE_ASCII = 127


@dataclass
class Editor:
    """Editor state plus the logic to edit and render it."""

    stdscr: "curses.window | None"
    path: Path | None = None
    lines: list[str] = field(default_factory=lambda: [""])
    row: int = 0
    col: int = 0
    want_col: int = 0
    top: int = 0
    left: int = 0
    modified: bool = False
    cut_buffer: list[str] = field(default_factory=list)
    last_was_cut: bool = False
    last_search: str = ""
    message: str = ""

    # ------------------------------------------------------------------ files

    def load(self) -> None:
        """Load ``self.path`` into the buffer, if it exists."""
        if self.path is None:
            return
        if not self.path.exists():
            self.message = "[ New File ]"
            return
        try:
            text = self.path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            self.message = f"[ Error reading {self.path.name}: {exc.strerror} ]"
            return
        self.lines = text.expandtabs(TAB_WIDTH).splitlines() or [""]
        self.message = f"[ Read {len(self.lines)} lines ]"

    def save(self) -> bool:
        """Prompt for a file name and write the buffer. Return True on success."""
        initial = str(self.path) if self.path else ""
        answer = self.prompt("File Name to Write: ", initial)
        if not answer:
            self.message = "[ Cancelled ]"
            return False
        target = Path(answer).expanduser()
        try:
            target.write_text("\n".join(self.lines) + "\n", encoding="utf-8")
        except OSError as exc:
            self.message = f"[ Error writing {target.name}: {exc.strerror} ]"
            return False
        self.path = target
        self.modified = False
        self.message = f"[ Wrote {len(self.lines)} lines ]"
        return True

    # ---------------------------------------------------------------- editing

    @property
    def line(self) -> str:
        return self.lines[self.row]

    def insert_text(self, text: str) -> None:
        self.lines[self.row] = self.line[: self.col] + text + self.line[self.col :]
        self.col += len(text)
        self.modified = True

    def insert_newline(self) -> None:
        head, tail = self.line[: self.col], self.line[self.col :]
        self.lines[self.row] = head
        self.lines.insert(self.row + 1, tail)
        self.row += 1
        self.col = 0
        self.modified = True

    def backspace(self) -> None:
        if self.col > 0:
            self.lines[self.row] = self.line[: self.col - 1] + self.line[self.col :]
            self.col -= 1
        elif self.row > 0:
            previous = self.lines[self.row - 1]
            self.lines[self.row - 1] = previous + self.line
            del self.lines[self.row]
            self.row -= 1
            self.col = len(previous)
        else:
            return
        self.modified = True

    def delete(self) -> None:
        if self.col < len(self.line):
            self.lines[self.row] = self.line[: self.col] + self.line[self.col + 1 :]
        elif self.row < len(self.lines) - 1:
            self.lines[self.row] += self.lines.pop(self.row + 1)
        else:
            return
        self.modified = True

    def cut_line(self, *, append: bool) -> None:
        """Cut the current line; consecutive cuts accumulate like in nano."""
        removed = self.lines.pop(self.row)
        if not self.lines:
            self.lines.append("")
        self.row = min(self.row, len(self.lines) - 1)
        self.col = min(self.col, len(self.line))
        if append:
            self.cut_buffer.append(removed)
        else:
            self.cut_buffer = [removed]
        self.modified = True

    def paste(self) -> None:
        if not self.cut_buffer:
            self.message = "[ Cutbuffer is empty ]"
            return
        self.lines[self.row : self.row] = self.cut_buffer
        self.row += len(self.cut_buffer)
        self.col = min(self.col, len(self.line))
        self.modified = True

    # ------------------------------------------------------------- navigation

    def move_left(self) -> None:
        if self.col > 0:
            self.col -= 1
        elif self.row > 0:
            self.row -= 1
            self.col = len(self.line)

    def move_right(self) -> None:
        if self.col < len(self.line):
            self.col += 1
        elif self.row < len(self.lines) - 1:
            self.row += 1
            self.col = 0

    def move_vertical(self, delta: int) -> None:
        self.row = max(0, min(self.row + delta, len(self.lines) - 1))
        self.col = min(self.want_col, len(self.line))

    @property
    def page_size(self) -> int:
        return max(1, self.text_height - 1)

    @property
    def text_height(self) -> int:
        assert self.stdscr is not None
        return max(1, self.stdscr.getmaxyx()[0] - 4)

    def search(self) -> None:
        query = self.prompt("Search: ", self.last_search)
        if not query:
            self.message = "[ Cancelled ]"
            return
        self.last_search = query
        needle = query.lower()
        total = len(self.lines)
        start_row = self.row
        for offset in range(total + 1):
            index = (start_row + offset) % total
            start = self.col + 1 if offset == 0 else 0
            found = self.lines[index].lower().find(needle, start)
            if found != -1:
                self.row, self.col = index, found
                wrapped = index < start_row or (offset == total)
                self.message = "[ Search Wrapped ]" if wrapped else ""
                return
        self.message = f'[ "{query}" not found ]'

    def show_location(self) -> None:
        self.message = (
            f"[ line {self.row + 1}/{len(self.lines)}, "
            f"col {self.col + 1}/{len(self.line) + 1} ]"
        )

    # ---------------------------------------------------------------- display

    def put(self, y: int, x: int, text: str, attr: int = curses.A_NORMAL) -> None:
        """addstr that clips to the window and ignores the bottom-right quirk."""
        assert self.stdscr is not None
        height, width = self.stdscr.getmaxyx()
        if not (0 <= y < height) or x >= width:
            return
        try:
            self.stdscr.addstr(y, x, text[: width - x], attr)
        except curses.error:
            pass

    def scroll_to_cursor(self, width: int) -> None:
        height = self.text_height
        if self.row < self.top:
            self.top = self.row
        elif self.row >= self.top + height:
            self.top = self.row - height + 1
        if self.col < self.left:
            self.left = self.col
        elif self.col >= self.left + width - 1:
            self.left = self.col - width + 2

    def draw(self) -> None:
        assert self.stdscr is not None
        height, width = self.stdscr.getmaxyx()
        self.stdscr.erase()
        if height < MIN_HEIGHT:
            self.put(0, 0, "Window too small")
            self.stdscr.refresh()
            return

        self.scroll_to_cursor(width)

        name = str(self.path) if self.path else "New Buffer"
        flag = "Modified" if self.modified else ""
        title = f"  pynano 1.0{name:^{max(0, width - 30)}}{flag:>10}  "
        self.put(0, 0, title.ljust(width), curses.A_REVERSE)

        for screen_row in range(self.text_height):
            index = self.top + screen_row
            if index >= len(self.lines):
                break
            self.put(screen_row + 1, 0, self.lines[index][self.left :])

        if self.message:
            self.put(height - 3, max(0, (width - len(self.message)) // 2), self.message, curses.A_REVERSE)

        column_width = max(1, width // len(SHORTCUTS[0]))
        for bar_row, entries in enumerate(SHORTCUTS):
            for column, (keys, label) in enumerate(entries):
                x = column * column_width
                self.put(height - 2 + bar_row, x, keys, curses.A_REVERSE)
                self.put(height - 2 + bar_row, x + len(keys) + 1, label)

        self.stdscr.move(self.row - self.top + 1, self.col - self.left)
        self.stdscr.refresh()

    def show_help(self) -> None:
        assert self.stdscr is not None
        self.stdscr.erase()
        for y, text in enumerate(HELP_TEXT):
            self.put(y, 1, text, curses.A_BOLD if y == 0 else curses.A_NORMAL)
        self.stdscr.refresh()
        self.stdscr.get_wch()

    # ------------------------------------------------------------------ input

    def prompt(self, label: str, initial: str = "") -> str | None:
        """Read a line on the status row. Return None if cancelled."""
        assert self.stdscr is not None
        buffer = initial
        while True:
            height, width = self.stdscr.getmaxyx()
            y = height - 3
            self.put(y, 0, (label + buffer).ljust(width), curses.A_REVERSE)
            self.stdscr.move(y, min(width - 1, len(label) + len(buffer)))
            self.stdscr.refresh()
            key = self.stdscr.get_wch()
            code = ord(key) if isinstance(key, str) else key
            if isinstance(key, str) and key.isprintable():
                buffer += key
            elif code in (Key.NEWLINE, Key.RETURN, curses.KEY_ENTER):
                self.message = ""
                return buffer
            elif code in (Key.CTRL_C, Key.ESCAPE):
                self.message = ""
                return None
            elif code in (curses.KEY_BACKSPACE, Key.BACKSPACE_H, Key.DELETE_ASCII):
                buffer = buffer[:-1]

    def confirm_exit(self) -> bool:
        """Return True if it is fine to quit (saving first if requested)."""
        assert self.stdscr is not None
        if not self.modified:
            return True
        height, width = self.stdscr.getmaxyx()
        question = "Save modified buffer? (Y/N, ^C to cancel) "
        self.put(height - 3, 0, question.ljust(width), curses.A_REVERSE)
        self.stdscr.refresh()
        while True:
            key = self.stdscr.get_wch()
            if isinstance(key, str) and key.lower() == "y":
                return self.save()
            if isinstance(key, str) and key.lower() == "n":
                return True
            if key in (chr(Key.CTRL_C), chr(Key.ESCAPE)):
                self.message = "[ Cancelled ]"
                return False

    def handle_key(self, key: str | int) -> bool:
        """Process one key press. Return False when the editor should exit."""
        was_cut, self.last_was_cut = self.last_was_cut, False
        code = ord(key) if isinstance(key, str) else key
        vertical = False

        if isinstance(key, str) and key.isprintable():
            self.message = ""
            self.insert_text(key)
        else:
            match code:
                case Key.CTRL_X:
                    return not self.confirm_exit()
                case Key.CTRL_O:
                    self.save()
                case Key.CTRL_W:
                    self.search()
                case Key.CTRL_G:
                    self.show_help()
                case Key.CTRL_C:
                    self.show_location()
                case Key.CTRL_K:
                    self.cut_line(append=was_cut)
                    self.last_was_cut = True
                case Key.CTRL_U:
                    self.paste()
                case Key.NEWLINE | Key.RETURN | curses.KEY_ENTER:
                    self.insert_newline()
                case Key.TAB:
                    self.insert_text(" " * TAB_WIDTH)
                case Key.BACKSPACE_H | Key.DELETE_ASCII | curses.KEY_BACKSPACE:
                    self.backspace()
                case curses.KEY_DC:
                    self.delete()
                case curses.KEY_LEFT:
                    self.move_left()
                case curses.KEY_RIGHT:
                    self.move_right()
                case curses.KEY_UP:
                    vertical = True
                    self.move_vertical(-1)
                case curses.KEY_DOWN:
                    vertical = True
                    self.move_vertical(1)
                case curses.KEY_PPAGE | Key.CTRL_Y:
                    vertical = True
                    self.move_vertical(-self.page_size)
                case curses.KEY_NPAGE | Key.CTRL_V:
                    vertical = True
                    self.move_vertical(self.page_size)
                case curses.KEY_HOME | Key.CTRL_A:
                    self.col = 0
                case curses.KEY_END | Key.CTRL_E:
                    self.col = len(self.line)
                case _:
                    pass

        if not vertical:
            self.want_col = self.col
        return True

    def run(self) -> None:
        assert self.stdscr is not None
        self.stdscr.keypad(True)
        curses.raw()  # let us see ^C, ^O, ^X, ... as ordinary keys
        self.load()
        running = True
        while running:
            self.draw()
            running = self.handle_key(self.stdscr.get_wch())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A small nano-style text editor.")
    parser.add_argument("file", nargs="?", type=Path, help="file to edit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    os.environ.setdefault("ESCDELAY", "25")
    curses.wrapper(lambda stdscr: Editor(stdscr, args.file).run())


if __name__ == "__main__":
    main()
