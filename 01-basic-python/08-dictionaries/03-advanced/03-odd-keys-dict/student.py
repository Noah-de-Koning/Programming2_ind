# Write your code here
def odd_keys_dict(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        if k % 2 != 0:
            new_dict[k] = v
    return new_dict