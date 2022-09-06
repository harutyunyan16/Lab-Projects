# necessary libraries
import string


'''
    This project is about vaidation email address.In this project i use cases bellow this.


    If you didn`t knew the email address divided in two parts`

    prefix - Can contein letters(a-z), numbers, underscopes("_"), dots(".") and dashes(".").
             An underscore, period, or dash must be followed by one or more letter or number.
    
    domein - Can conteint letters, numbers and dashes.
             The last portion of the domain must be at least two characters, for example: .com, .org, .cc



    Class EmailValidation consist of the three methods (1)

    mail_validator(mail(type - str)) - This function playe the main() function role (2)
                       calling this function you can knew if the given email
                       addres valid or not.


    prefix_validator(prefix(type  - str)) - This funtion is working with email prefix part. (3)
                                            If prefix is valid it return True.            


    domein_validator(prefix(type  - str)) - This funtion is working with email domein part. (4)
                                            If domein is valid it return True.
    
'''



# class EmailValidation number on documentation - 1
class EmailValidation:
    # mail_validator number on documentation - 2
    def mail_validator(self, mail: str):
        if mail.count('@') != 1:
            return False
        
        prefix = mail.split('@')[0]
        domein = mail.split('@')[1]

        if self.prefix_validator(prefix) and self.domein_validator(domein):
            return True
        

        return False

    # prefix_validator number on documentation - 3

    def prefix_validator(self, prefix: str):
        if prefix[0] not in string.ascii_lowercase:
            return False
        
        for i in range(len(prefix)):
            el = prefix[i]
            try:
                if el in '-_.' and prefix[i + 1] in '-_.' :
                    return False
            except:
                return False

        return True

    # prefix_validator number on documentation - 4
    def domein_validator(self, domein: str):
        if domein.count('.') != 1:
            return False

        if domein[0] not in string.ascii_lowercase:
            return False

        for i in range(len(domein)):
            el = domein[i]
            try:
                if el in '-' and domein[i + 1] in '-' :
                    return False
            except:
                return False

        if len(domein.split('.')[1]) < 2:
            return False

        valid_chars = string.ascii_lowercase + '0123456789' + '-'
        for el in domein.split('.')[0]:
            print(domein.split('.')[0])
            if el not in valid_chars:
                print('this case')
                return False

        return True
