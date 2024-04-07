# Write your code here
def word_count(string):
    if len(string) != 0:
        word_count = 1
    else:
        return 0
    for i in string:
        if i == ' ':
            word_count += 1
    return word_count