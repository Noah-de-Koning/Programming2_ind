# Write your code here
def card_value(string):
    if string in (2,3,4,5,6,7,8,9,10):
        return string
    elif string == 'Jack':
        return 11
    elif string == 'Queen':
        return 12
    elif string == 'King':
        return 13
    elif string == 'Ace':
        return 1