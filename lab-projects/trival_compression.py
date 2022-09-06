# necessary libraries
from os.path import exists


'''
    This project about compressing the text file value.
    Below this you can find algorithm that i use`

    it`s a very simple


    replacing "hellloooo" to "he3l40"

'''


class Compress:
    def compress(self, path, save_to=None):# save_to for uploading the compress version to the other or the same file
        try:
            with open(path, 'r') as f:
                words = f.read().split(' ')
        except:
            raise FileExistsError(f'"{path}" does not exist')

        data = ''
        for el in words:
            data += self.word_compress(el) + ' '

        print('compressing version -', data)

        if save_to == None:
            yn = input(f'Do you sure to overwrite this file "{path}"? (y/n): ')
            yn = yn.lower()
            if yn[0] == 'y':
                with open(path, 'w') as f:
                    f.write(data)
            return

        if exists(path):
            yn = input(f'"{save_to}" already exist do you want to overwrite or cancel? (y/n): ')
            yn = yn.lower()
            if yn[0] == 'y':
                with open(save_to, 'w') as f:
                    f.write(data) 

    
    def word_compress(self, word):
        res = ''
        i = 0
        while i < len(word):
            count = 1
            j = i + 1
            while j < len(word):
                if word[j] != word[i]:
                    break
                count += 1
                j += 1
            if count > 2:
                res += str(count) + word[i]
                i += count
                continue
            res += word[i]
            i += 1
    
        return res

Compress().compress('text.txt')