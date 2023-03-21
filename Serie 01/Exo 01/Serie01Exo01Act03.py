def symmetric_browse(L):
    resL = []
    if len(L)%2 == 0:
        N = int(len(L)/2)
    else: N = int(len(L)/2 + 1)

    for i in range(N):
        resL.append(L[i])
        if len(L)%2 != 0:
            if i != N-1:
                resL.append(L[len(L)-1 - i])
        else: resL.append(L[len(L)-1 - i])
    return resL

# MAIN 
list1 = [1,3,5,7,9,8,6,4,2]
resList = symmetric_browse(list1)
print("Resultat de la function symmetric browse est : ", resList)
