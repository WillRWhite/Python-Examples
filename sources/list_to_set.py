
'''
def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    # This is the one line:     
    # return set(map(lambda doc: doc.upper(), set(filter(lambda doc: not(doc.isdigit()), set(originals + backups)))))
    # return set(map(lambda doc: doc.upper(), filter(lambda doc: not(doc.isdigit()), set(originals + backups))))
    # But split for readibility
    return set(
        map(
            lambda doc: doc.upper(), set(
                filter(
                    lambda doc: not(doc.isdigit()), set(originals + backups)
                    )
                )
            )
        )
'''

def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    # This is the one line:
    #return set(filter(lambda doc: not(doc.isdigit()),(map(lambda doc: doc.upper(), original + backup))))
    return set(
        filter(lambda doc: not(doc.isdigit()),
               (map(lambda doc: doc.upper(), originals + backups)
            )
        )
    )


# Tuples to process
my_originals = ("apple", "bananas", "5026", "oranges", "pears", "plumbs", "395", "cherries", "grapes")
my_backups   = ("apple", "1234", "oranges", "pears", "apple", "45", "oranges", "1234", "grapes", "blueberries")

# Using the function restore_documents()
print(restore_documents(my_originals, my_backups))

# One step at a time
combine = (my_originals + my_backups)
#print(combine)

upper = ((map(lambda doc: doc.upper(), combine)))
#print(tuple(upper))

filter = (filter(lambda doc: not(doc.isdigit()), upper))
#print(tuple(filter))

filter_set = set(filter)
print(filter_set)
     






