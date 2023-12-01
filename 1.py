file = open('1.txt', 'r').readlines()
totalFile = []
ref = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for line in file:
    digits = []
    word = []
    newword = ''
    for character in line:
        for i in word:
            newword += i
            for key, value in ref.items():
                if key in newword:
                    digits.append(value)
                    # keep last character, may be used for next word
                    newword = i
        word = []
        if character.isalpha():
            word.append(character)
        elif character.isdigit():
            digits.append(character)
    if 'oneight' in line:
        print(line, digits, digits[0] + digits[-1])
    totalFile.append(digits[0] + digits[-1])

sum = 0
for str in totalFile:
    sum += int(str)
print(sum)