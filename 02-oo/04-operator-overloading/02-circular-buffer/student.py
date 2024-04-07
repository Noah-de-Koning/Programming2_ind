class CircularBuffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.__items = []
        
    def add(self, item):
        self.__items.append(item)
        if len(self.__items) > self.max_size:
            del self.__items [0]


    def __getitem__(self, index):
        return self.__items[index]


    def __len__(self):
        return len(self.__items)