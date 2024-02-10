__author__ = 'Re'

class City:

#constructor class showing the 6 parameters of the city class
    def __init__(self,code,name,region,population,latitude,longitude):
        self.code=str(code)
        self.name=str(name)
        self.region=str(region)
        self.population=int(population)
        self.latitude=float(latitude)
        self.longitude=float(longitude)


#string to concatenate the name, population, latitude, and longitude
    def __str__(self):
        return str(self.name)+","+str(self.population)+","+str(self.latitude)+","+str(self.longitude)


