def fun(word):
    ans = ""
    for c in word[::-1]:
        ans += c
        print(ans)


fun("EXAMPLE")
