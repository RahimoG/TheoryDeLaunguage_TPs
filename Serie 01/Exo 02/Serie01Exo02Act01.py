def crange(*cintrev):
    res_list = []
    for my_list in cintrev:
        for i in range(ord(my_list[0]), ord(my_list[1])+1):
            res_list.append(chr(i))
    return "".join(res_list)
print("Crange V1 : "+crange(["a", "z"],["A", "Z"], ["0", "9"]))


def crangeV2(*cintrev):
    ch = ""
    for my_list in cintrev:
        for i in range(ord(my_list[0]), ord(my_list[1])+1):
            ch += chr(i)
    return ch
print("Crange V2 : "+crangeV2(["a", "z"],["A", "Z"], ["0", "9"]))













## Theory : 
# return ascii en entier : ord("A") 
# chr(64)
# function : 
# print(crange(["A", "Z"], ["0", "9"]))

# list comprehention : 
A = ["A", "Z"], ["0", "9"]

res_list = [
    chr(i)
    for my_list in A
        for i in range(ord(my_list[0]), ord(my_list[1])+1)
]
#print("".join(res_list))
















