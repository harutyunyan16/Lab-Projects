'''
    This project about vaidation the card number.

    In this project i followed the rules1`

    1) Can contein only numbers
    2) Lenght of card number must be in range 12, 19 (except 17)

'''




class BankCardValidator:
    def valdiator(self, card):
        lens = [el for el in range(12, 20) if el != 17]
        if len(card) not in lens:
            return False

        numbers = [chr(i) for i in range(10)]

        for el in card:
            if el not in numbers:
                return False
        
        return True