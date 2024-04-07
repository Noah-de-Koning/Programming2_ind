# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if not 0 <= value <= 23:
            raise ValueError('Invalid Hour value')
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if not 0 <= value <= 59:
            raise ValueError('Invalid Minutes value')
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if not 0 <= value <= 59:
            raise ValueError('Invalid Seconds value')
        self.__seconds = value