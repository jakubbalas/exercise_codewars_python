"""
Move the first letter of each word to the end of it, then add "ay"
to the end of the word. Leave punctuation marks untouched.
"""

def pigify_word(word: str):
    return word[1:] + word[0] + "ay" if word.isalpha() else word


def pig_it(text: str):
    return " ".join([pigify_word(a) for a in text.split(" ")])


assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
assert pig_it('Using also exclamation !') == 'singUay lsoaay xclamationeay !'