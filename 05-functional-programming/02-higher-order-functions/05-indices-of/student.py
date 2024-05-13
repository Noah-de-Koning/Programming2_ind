def indices_of(xs, condition):
    # result = []
    # for index in range(len(xs)):
    #     if condition(xs[index]):
    #         result.append(index)
    # return result

    return [index for index in range(len(xs)) if condition(xs[index])]