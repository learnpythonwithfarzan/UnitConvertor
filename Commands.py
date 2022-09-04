class Commands:
    def __init__(self, entry_from, list_box_from, list_box_to):
        self.entryFrom = entry_from
        self.listBoxFrom = list_box_from
        self.listBoxTo = list_box_to

    def __millimeter(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom / 10
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom / 25.4
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom / 304.8
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom / 914.4
        elif self.listBoxTo == 'Meter':
            result = (self.entryFrom / 10) / 100
        elif self.listBoxTo == 'KiloMeter':
            result = ((self.entryFrom / 10)/100)/1000
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 1609344

        return result

    def __centimeter(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 10
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom / 2.54
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom / 30.48
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom / 91.44
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom / 100
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom/100000
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 160934.4

        return result

    def __inch(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 25.4
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom * 2.54
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom / 12
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom / 36
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom / 39.3700787402
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom / 39370.078740157
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 63360
        return result

    def __feet(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 304.8
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom * 30.48
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom * 12
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom / 3
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom / 3.280839895
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom / 3280.8398950131
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 5280
        return result

    def __yard(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 914.4
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom * 91.44
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom * 36
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom * 3
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom / 1.0936132983
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom / 1093.612983377
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 1760
        return result

    def __meter(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 1000
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom * 100
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom * 39.3700787402
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom * 3.280839895
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom * 1.0936232983
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom / 1000
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 1609.344
        return result

    def __kilometer(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 1000000
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom * 100000
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom * 39370.078740157
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom * 3280.8398950131
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom * 1093.6132983377
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom * 1000
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 1.609344
        return result

    def __mile(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 1609344
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom * 160934.4
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom * 63360
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom * 5280
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom * 1760
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom * 1609.344
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom * 1.609344
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom
        return result

    def units(self):
        if self.listBoxFrom == 'MilliMeter':
            return self.__millimeter()
        elif self.listBoxFrom == 'CentiMeter':
            return self.__centimeter()
        elif self.listBoxFrom == 'Inch':
            return self.__inch()
        elif self.listBoxFrom == 'Feet':
            return self.__feet()
        elif self.listBoxFrom == 'Yard':
            return self.__yard()
        elif self.listBoxFrom == 'Meter':
            return self.__meter()
        elif self.listBoxFrom == 'KiloMeter':
            return self.__kilometer()
        elif self.listBoxFrom == 'Mile':
            return self.__mile()
