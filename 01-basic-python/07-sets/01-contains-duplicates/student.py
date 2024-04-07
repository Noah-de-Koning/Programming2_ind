# Write your code here
def contains_duplicates(xs):
    unique = set(xs)
    return len(xs) != len(unique)