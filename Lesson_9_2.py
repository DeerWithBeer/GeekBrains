class Road:
    def __init__(self,width=0,lenght=0):
        self._width=width
        self._lenght=lenght
    def CalculateMass(self,weight_of_sqare=1,thikness=1):
        return self._width*self._lenght*weight_of_sqare*thikness
main_road=Road(5,100)
print(main_road.CalculateMass(5,10))