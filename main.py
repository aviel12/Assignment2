# A
def reverse(sentence, reverse_word):
    sentence = sentence.split()

    if reverse_word not in sentence:
        return 'no match word found'

    if reverse_word == str:
        return 'invalid input'

    find_index = sentence.index(reverse_word)
    sentence[find_index] = sentence[find_index][::-1]
    return ' '.join(sentence)


# B
def compute_equation(equation):
    for word in equation:
        if word not in '1234567890-+*/.':
            return "invalid input detected"
    x = eval(equation)
    if x % 1 == 0:
        return int(x)
    else:
        return float(x)

