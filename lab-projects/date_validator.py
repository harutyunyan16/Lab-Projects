import string


class DateValidator:
    def date(self, date):
        if self.validator(date) or self.validator2(date):
            return True
        return False

    def validator(self, date: str):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        valid_chs = string.ascii_letters

        if date.count(' ') != 2:
            return False

        mdy = date.split(' ')

        for el in mdy[0]:
            if el not in valid_chs:
                return False
        
        if mdy[0].title() not in months:
            return False

        if mdy[1][-2] + mdy[1][-1] != 'nd':
            return False

        day = mdy[1][:-2]

        if not day.isnumeric():
            return False

        if int(day) not in range(1, 32):
            return False


        if mdy[0].title() == months[1] and int(day) not in range(1, 29):
            return False

        
        return True

        
    def validator2(self, date: str):
        chs = [str(i) for i in range(10)]
        chs.append('.')

        if date.count('.') != 2 and date.count('/') != 2:
            return False

        mdy = []

        try:
            if '/' not in date:
                mdy = [int(el) for el in date.split('.')]
            else:
                mdy = [int(el) for el in date.split('/')]
        except:
            return False
        
        if mdy[0] not in range(1, 32):
            return False

        if mdy[1] not in range(1, 13):
            return False

        if mdy[1] == 2 and mdy[0] not in range(1, 30):
            return False

        return True


obj = DateValidator()
print(obj.validator2('32/1/2022'))
