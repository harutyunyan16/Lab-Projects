def number(number: str):
    number = number.lower()

    if number[0] == 'e':
        return False

    if number.count('+') > 2 and number[0] != '+':
        return False

    if number.count('e') > 1 or number.count('.') > 1:
        return False


    for i in range(len(number)):
        if i == 0:
            continue
        
        if number[i] == '+' or number[i] == '-':
            if number[i - 1] != 'e':
                return False
        
    return True

