def repeat_by_list(L1, L2):
    L3 = []
    for index,item in enumerate(L1):
        for i in range(L2[index]):
            L3.append(item)
    return L3

# defenition des lists :
list1 = [6,1]
list2 = [2,4]
# appele de la function repeat_by_list :
resList = repeat_by_list(list1, list2)
print("Resultat de la function : repeat by list est : ", resList)

# List comprehention  :
list_comp = [
    item
    for index,item in enumerate(list1)
        for i in range(list2[index])
]
print("Resultat de la function : List Comprehention : ",list_comp)