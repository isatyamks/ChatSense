
#ignore this function ,i made this only to create some random words which i want to remove the stop words

def char_gen():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    with open('comb.txt', 'w') as file:
        for char1 in alphabet:
            for char2 in alphabet:
                for char3 in alphabet:
                     file.write(char1 + char2 + char3 +'\n')

generate_combinations()
