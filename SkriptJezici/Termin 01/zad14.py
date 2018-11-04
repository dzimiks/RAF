def fiver(string):
    f = open('14.txt', 'w')
    words = string.split()

    for word in words:
        if len(word) >= 5:
            print(word)
            f.write(word + '\n')

    f.close()


fiver('text with more than fiver 234897234 testest n')
