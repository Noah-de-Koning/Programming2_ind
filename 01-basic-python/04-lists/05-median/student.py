# Write your code here
def median(ns):
    sorted_ns = sorted(ns)
    middle = len(sorted_ns) // 2
    if len(sorted_ns) % 2 != 0:
        return sorted_ns[middle]
    else:
        return (sorted_ns[middle-1] + sorted_ns[middle]) / 2