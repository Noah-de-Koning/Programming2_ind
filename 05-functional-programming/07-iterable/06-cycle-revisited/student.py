def cycle(xs):
    current = 0
    while True:
        if current >= len(xs):
            current = 0
        yield xs[current]
        current += 1
