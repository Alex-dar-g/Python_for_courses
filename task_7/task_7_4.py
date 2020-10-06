string_lb_ts = f"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

string_email = 'godunovaleksandr804@gmail.com'
string_join = string_lb_ts + string_email

# подсчёт букв
count_letters = 0
for element in string_join:
    if element.isalpha():
        count_letters += 1
    else:
        continue
print(count_letters)

# подсчёт гласных букв
count_vowels_letters = 0
set_vowels_letters = set('aeyuio')
for element_ in string_join:
    if element_ in set_vowels_letters:
        count_vowels_letters += 1
    else:
        continue
print(count_vowels_letters)

# печать 18-ого символа
count_join_string = 0

while True:
    count_special_element = 18 * count_join_string
    special_element = string_join[count_special_element]
    if not special_element.isalnum():
        count_join_string += 1
        continue
    if special_element.islower():
        print(count_special_element, special_element.upper())
    else:
        print(f'{count_special_element} {special_element.lower()}')
    count_join_string += 1
