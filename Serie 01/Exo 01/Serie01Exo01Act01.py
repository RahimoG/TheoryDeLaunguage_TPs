def substract(L1, L2):
    L3 = []
    for item in L1:
        if item not in L2:
            L3.append(item)
    return L3
#defenition des lists : 
list1 = [5,8,12,1,13,17]
list2 = [6,7,12,5,17]

# appele de la function sustract 
listRes = substract(list1, list2)
print("le resultat pour la function sustract est : ", listRes)

#List comprehention :
my_list = [
    item
    for item in list1
        if item not in list2
]

print("le resultat pour la list comprehention : ", my_list)