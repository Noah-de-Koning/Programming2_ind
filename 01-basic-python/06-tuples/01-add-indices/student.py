# Write your code here
def add_indices(xs):
    indices = []
    for i in range (0, len(xs)):
        indices.append(i)
    return list(zip(indices, xs))