class Cycle:
    def __init__(self, xs):
        self.__xs = list(xs)
        self.__index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__xs)
        return self.__xs[self.__index]












# class Cycle:
#     def __init__(self, xs, amount):
#         self.__xs = list(xs)
#         self.__amount = amount

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         result = []
#         for i in range(self.__amount):
#             if i > len(self.__xs):
#                 i -= len(self.__xs)
#             result.append(self.__xs[i])
#         return result