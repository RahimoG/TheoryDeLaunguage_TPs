def conditional_replace(s, sub1, sub2, sub3, sub4):
    for i in range(len(s)):
        if s[i] == sub1:
            if i+1 < len(s):
                if s[i+1] == sub2:
                    s = s.replace(s[i] , sub3)
                else: s = s.replace(s[i] , sub4)
    return s


print(conditional_replace("abc=ded", "=", "f", "=e", "=f"))


