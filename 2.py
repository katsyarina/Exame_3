def palindrom(word):
    if len(word) / 2 != 0 and len(word) != 1:
        for i in range(0, int((len(word)-1)/2+1)):
            if word[i] == word[len(word)-1-i]:
                continue
            else:
                print('Слово не является палиндромом.')
                break
        else:
            print('Слово - палиндром')
    else:
        print('Слово не является палиндромом.')

print(palindrom(input('Введите слово: ')))
