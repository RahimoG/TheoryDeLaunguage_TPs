def factors(word):
    resList = []
    ch = ""
    for i in range(len(word)+1):
        ch = word[:i]
        for j in range(len(ch)+1):
            if ch[j:] not in resList: resList.append(ch[j:])
    return resList


print(factors("hello"))
