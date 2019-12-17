'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0
def count_th(word):
    print('original word', word)

    if not word or len(word) <= 1:
        return global count
    elif word[0] == 't' and word[1] == 'h':
        print('elif comparison =========')
        print('fist letter', word[0])
        print('second letter', word[1])
        global count += 1
        print('count', count)
        count_th(word[1:])
    else:
        print('else ==========')
        print('fist letter', word[0])
        print('second letter', word[1])
        return count_th(word[1:])
    print('final count', count)
    return global count

print(count_th(''))
print(count_th('abcthxyz'))
print(count_th('abcthefthghith'))
print(count_th('thhtthht'))
print(count_th('THtHThth'))
