# necessary libraries
import string
from os.path import exists


'''
    This project about the analyzing text document. What this program do`

    (All the methods in class named TextAnalyzer (1))

    counting words - get_words_count() (2)
    counting letters - get_letters_count() (3)
    counting sentences - get_sentences_count() (4)
    detecting the most used letter - get_max_letter_count() (5)
    detecting the most used words - get_max_word_count() (6)
    breaking the text to words - tokenaizer() (7)

'''


# TextAnalyzer (1)
class TextAnalyzer:
    path = None

    def __init__(self, path, upload_to=None):
        self.path = path

        data = self.get_words_count() + self.get_letters_count() + self.get_sentences_count() + self.get_max_letter_count() + self.get_max_word_count()
        print(data)

        if upload_to is not None:
            write = ''
            if exists(upload_to):
                write  = input(f'"{upload_to}" is already exist, are you sure to write there this data (y/n): ')
                if write[0] == 'n' or write[0] == 'N':
                    exit()
            with open(upload_to, 'w') as f:
                f.write(data)
            
    # get_words_count (2)
    def get_words_count(self):
        return 'Words: ' + str(len(self.tokkenaizer())) + '\n'

    # get_letter_count (3)
    def get_letters_count(self):
        res = 0
        for el in self.tokkenaizer():
            res += len(el)
        
        return 'Letters: ' + str(res) + '\n'

    # get_sentences_count (4)
    def get_sentences_count(self):
        with open(self.path, 'r') as f:
            count = f.read().count('.')
        return 'Sentences: ' + str(count) + '\n'

    # get_max_letter_count (5)
    def get_max_letter_count(self):
        with open(self.path, 'r') as f:
            letters = [el for el in f.read() if el in string.ascii_letters]
        letter = ''
        count = 0
        for el in letters:
            if letters.count(el) > count:
                count = letters.count(el)
                letter = el
        return 'Word frequency: ' + letter + f'(count: {count})' + '\n'

    # get_max_word_count (6)
    def get_max_word_count(self):
        words = self.tokkenaizer()
        word = ''
        count = 0
        for el in words:
            if words.count(el) > count:
                count = words.count(el)
                word = el
        return 'Word frequency: ' + word + f'(count: {count})'
        
    # tokkenaizer (7)
    def tokkenaizer(self):
        res = []

        tmp = ''
        tokening = '.,?>()< '
        with open(self.path, 'r') as f:
            st = f.read()
            for i in st:
                if i not in tokening:
                    tmp += i
                else:
                    res.append(tmp)
                    tmp = ''

        while '' in res:
            res.remove('')
        return res
            

obj = TextAnalyzer('text.txt', 'about.txt')