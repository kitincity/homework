# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


def remove_exclamation_marks(s):
    s = s.replace('!','')
    return s      


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
  if s[len(s)-1]=='!':
    remove_last = s[:-1]
    return remove_last
  else:
     return s


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    split = s.split(' ')
    for i in range(len(split)):
       count = 0
       for j in range(len(split[i])):
          if split[i][j]=='!':
             count+=1
       if count!=1:
          print(split[i])
       else:
          print('')   

  
print('А. Введите строку:')
str = input()
print(remove_exclamation_marks(str))


print('B. Введите строку:')
str = input()
print(remove_last_em(str))

print('C. Введите строку:')
str = input()
remove_word_with_one_em(str)