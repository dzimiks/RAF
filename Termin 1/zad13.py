with open('12.txt') as file:
    unique = []

    for line in file:
        for word in line:
            for letter in word:
                if letter not in unique and letter != '\n' and letter != ' ':
                    unique.append(letter)

    print(unique)
    print(len(unique))
