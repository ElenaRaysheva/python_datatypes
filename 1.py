
# word = 'test'
word = 'testing'

def get_middle_letter(string):
    str_length = len(string)

    if str_length % 2 == 1:
        return string[int(str_length / 2)]
    else:
        string_middle = int(str_length / 2)
        return string[string_middle - 1 : string_middle + 1]

letter1 = get_middle_letter('test')
letter2 = get_middle_letter('testing')

print(letter1)
print(letter2)
