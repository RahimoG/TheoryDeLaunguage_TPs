def flatten_word(*w_tuple):
    my_string = ""
    for tuple in w_tuple:
        for i in range(tuple[1]):
            my_string += tuple[0]
    return my_string


print("flaten word normal : "+flatten_word(("a",2), ("b", 4), ("a", 2), ("b", 6), ("c", 1)))


def flatten_word1(*w_tuple):
    L = [
        tuple[0]
        for tuple in w_tuple
            for i in range(tuple[1])
    ]
    return "".join(L)
print("flaten word with list comprehention : "+flatten_word(("a",2), ("b", 4), ("a", 2), ("b", 6), ("c", 1)))



