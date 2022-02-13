def credit_card(num):
    str_num = str(num)
    return (len(str_num)-4) * '*' + str_num[-4:len(str_num)]

print(credit_card(int(input('Введите номер карты: '))))