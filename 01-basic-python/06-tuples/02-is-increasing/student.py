# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    combi = list(zip(ns,ms))
    for (x,y) in combi:
        if x > y:
            return False
    return True