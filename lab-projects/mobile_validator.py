'''
    This project about vaidation the mobile number.

    In this project i followed the rules1`

    1) Can contein only numbers and one character ("+") in start
    2) Lenght of mobile number must be in range 10, 12

'''

# main class
class MobileNumberValidator:
    # validator function returned true if the mobile number is valid else returned False
    def validator(self, number):
        if len(number) not in range(10, 13):
            return False

        if '+' in number and number.count('+') != 1:
            return False

        numbers = [str(i) for i in range(10)]

        for el in number[1:]:
            if el not in numbers:
                return False

        return True

