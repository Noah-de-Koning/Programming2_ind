def take_while(xs, condition):
    index = 0
    while index < len(xs) and condition(xs[index]):
        index += 1

    return (xs[:index], xs[index:])