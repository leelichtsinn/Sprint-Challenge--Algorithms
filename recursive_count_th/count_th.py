'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if not word:
        return count
    elif word[0] == 't' and word[1] == 'h':
        count += 1
        return count_th(word[2:])
    else:
        return count_th(word[2:])
