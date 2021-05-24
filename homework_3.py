final_list = {}

def thesaurus(*args):
    for i in sorted(args):
        if i[0] not in final_list:
            final_list[i[0]] = list(filter(lambda element: element.startswith(i[:1]), args))


thesaurus("Иван", "Мария", "Петр", "Илья")

print(final_list)
