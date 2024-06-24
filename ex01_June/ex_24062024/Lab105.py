letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u


def vowel_giver(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


# result  = filter_vowel('p')
# print(result)

filtered_words = filter(vowel_giver,letters_list)
print(list(filtered_words))