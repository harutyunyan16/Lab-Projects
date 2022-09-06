# necessary libraries
import string

# custom validators
from email_validator import EmailValidation
from date_validator import DateValidator
from mobile_validator import MobileNumberValidator
from card_validator import BankCardValidator
from number_validator import number




'''
    functions indexing

    mail validation - mail() (1)
    date validation - date() (2)
    mobile number validation - date() (3)
    bank card number validation - card() (4)

'''


class Validators:
    # mail() (1)
    def mail(self, mail):
        EmailValidation().mail_validator(mail)

    # date() (2)
    def date(self, date):
        DateValidator().date(date)

    # mobile() (3)
    def mobile(self, mobile):
        MobileNumberValidator().validator(mobile)

    # card() (4)
    def card(self, card):
        BankCardValidator().valdiator(card)

    # number() (5)
    def card(self, card):
        number(card)

