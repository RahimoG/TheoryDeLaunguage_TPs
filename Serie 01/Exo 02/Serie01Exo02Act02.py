def replace_many(s, L1, L2):
    my_list = []
    for char in s:
        if char in L1:
            for j in range(len(L1)):
                if char == L1[j]:
                    my_list.append(L2[j])
        else: my_list.append(char)
    return "".join(my_list)
        

L1 = ["a", "b", "c"]
L2 = ["b", "a", "d"]
string = "aabc"

print("le resultat de la function replace_many : " + replace_many(string, L1, L2))
