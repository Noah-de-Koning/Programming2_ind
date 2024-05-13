def merge_dictionaries(d1, d2,  merge_function):
    d_new = {**d1, **d2}
    for k in d1:
        if k in d2:
            d_new[k] = merge_function(d1[k], d2[k])
    return d_new