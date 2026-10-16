
'''
def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    # This is the one line:     
    # return set(map(lambda doc: doc.upper(), set(filter(lambda doc: not(doc.isdigit()), set(original + backup)))))
    # But split for readibility
    return set(
        map(
            lambda doc: doc.upper(), set(
                filter(
                    lambda doc: not(doc.isdigit()), set(original + backup)
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
               (map(lambda doc: doc.upper(), original + backup)
            )
        )
    )


# Tupls to process
original = ("apple", "bananas", "5026", "oranges", "pears", "plumbs", "395", "cherries", "grapes")
backup   = ("apple", "1234", "oranges", "pears", "apple", "45", "oranges", "1234", "grapes", "blueberries")

print(restore_documents(original, backup))



'''
combine = (original + backup)
#print(combine)

upper = ((map(lambda doc: doc.upper(), combine)))
#print(upper)

filter = (filter(lambda doc: not(doc.isdigit()), upper))
#print(filter)

return_set = set(filter)
print(return_set)

'''
        






