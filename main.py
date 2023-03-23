# 209297308

###Q1

def my_func(x1, x2, x3):
    try:
        if not (isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float)):
            return "Error: parameters should be float"
        sum_all_t = x1 + x2 + x3
        if sum_all_t == 0:
            return "Not a number – denominator equals zero"
        return float((sum_all_t * (x2+x3) * x3) / sum_all_t)
    except:
        return None



###Q2


def revword(word):
    word = word[::-1]
    word = word.lower()
    return word


def countword():
    fhand = open('text.txt', 'r')
    count = 1
    word = ""
    for index, line in enumerate(fhand):
        if index == 0:
            word = line.split()
            word = word[0]
        else:
            all_words = line.split()
            for check_word in all_words:
                check_word = revword(check_word)
                if word == check_word:
                    count += 1
    return count
