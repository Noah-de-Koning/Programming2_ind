class LengthConverter:
    FEET_PER_METER = 3.28084
    INCH_PER_METER = 39.3701

    def __init__(self):
        #private distance attribute in meter
        self.dis_M = 0



    @property
    def meter(self):
        return self.dis_M
    
    @meter.setter
    def meter(self, value):
        self.dis_M = value

    

    @property
    def feet(self):
        return self.dis_M * self.FEET_PER_METER
    
    @feet.setter
    def feet(self, value):
        self.dis_M = value / self.FEET_PER_METER


    
    @property
    def inch(self):
        return self.dis_M * self.INCH_PER_METER
    
    @inch.setter
    def inch(self, value):
        self.dis_M = value / self.INCH_PER_METER