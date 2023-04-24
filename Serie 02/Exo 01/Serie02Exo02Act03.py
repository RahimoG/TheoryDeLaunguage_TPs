# shuffel_symbol(word, symbol):
# ("abc", "?")
# return ["?abc", "a?bc", "ab?c", "abc?"]


def shuffel_word(word, symbol):
    resList = []
    for i in range(len(word)+1):
        resList.append(word[:i]+symbol+word[i:])
    return resList


print(shuffel_word("abc", "?"))