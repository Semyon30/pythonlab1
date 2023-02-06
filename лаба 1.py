import random
from num2words import num2words
i=[random.randint(1,9999999)]
print(i)
g=0
while g<99:
 mas=[random.randint(1,9999999)]
 g=g+1
 print(mas)
def num_to_word(num):
    try:
        print(num2words(num, lang='ru'))
    except NotImplementedError:
        print(num2words(num, lang='en'))
num_to_word(i[0])
num_to_word(mas[0])
