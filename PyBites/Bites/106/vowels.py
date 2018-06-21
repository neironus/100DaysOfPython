import re

text = """
The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'


# With regex
def strip_vowels(text=text):
    count = text.count('*')
    text = re.sub(r'[{}]'.format(vowels), '*', text, flags=re.IGNORECASE)
    return text, (text.count('*') - count)

    # With subn return also the count
    # return re.subn('[{}]'.format(vowels), '*', text, flags=re.I)



# With loop
# def strip_vowels(text=text):
#     count = 0
#     copy_text = []
#     for letter in text:
#         if letter.lower() in vowels:
#             count += 1
#             letter = '*'
#
#         copy_text.append(letter)
#
#     return ''.join(copy_text), count

