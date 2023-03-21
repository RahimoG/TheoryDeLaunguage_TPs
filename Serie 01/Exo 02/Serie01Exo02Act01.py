# using Lists :
def crange(*cintrev):
    res_list = []
    for my_list in cintrev:
        for i in range(ord(my_list[0]), ord(my_list[1])+1):
            res_list.append(chr(i))
    return "".join(res_list)
print("Crange V1 : "+crange(["a", "z"],["A", "Z"], ["0", "9"]))


# using String :
def crangeV2(*cintrev):
    ch = ""
    for my_list in cintrev:
        for i in range(ord(my_list[0]), ord(my_list[1])+1):
            ch += chr(i)
    return ch
print("Crange V2 : "+crangeV2(["a", "z"],["A", "Z"], ["0", "9"]))


# using List comperehention : 
A = (["a", "z"],["A", "Z"], ["0", "9"])
res_list = [
    chr(i)
    for my_list in A
        for i in range(ord(my_list[0]), ord(my_list[1])+1)
]
print("Crange V3 : " + "".join(res_list))
