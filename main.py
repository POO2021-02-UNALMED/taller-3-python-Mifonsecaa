from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca

if __name__ == "__main__":
    marca1 = Marca("Semsung")
    marca2 = Marca("Lj")

    tv1 = TV(marca1, True)
    tv2 = TV(marca2, False)

    tv1.setPrecio(2000)
    tv2.setCanal(90)
    tv1.setCanal(121)
    tv2.setVolumen(7)

    control1 = Control()
    control1.enlazar(tv1)
    control1.turnOff()
    control1.setCanal(50)
    control1.turnOn()
    control1.canalUp()
    control1.volumenUp()

    print(tv2.getCanal())
    print(tv1.getPrecio())
    print(tv1.getMarca().getNombre())
    print(tv1.getCanal())

class Marca:
    def __init__(self,nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre
class Tv:
    numTv = 0
    def __init__(self,marca, estado):
        self._marca = marca
        self._estado = False
        self.canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = control
    
    def getMarca(self):
        return self._marca
    def getControl(self):
        return control
    def getCanal(self):
        return self.canal
    def getPrecio(self):
        return self._precio
    def getVolumen(self):
        return self._volumen
    
    def setMarca(self, marca):
        self._marca = marca
    def setControl(self, control):
        self._control = control
    def setPrecio(self, precio):
        self._precio = precio
    def setVolumen(self, volumen):
        self._volumen = volumen

    @classmethod
    def getCantidadTv():
        return Tv.numTv
        
    def turnOn (self, estado):
        self._estado = True
    def turnOff(self, estado):
        self._estado = False

    def getEstado(self):
        return self._estado
    

    def canalUp(self,canal):
        lista = []
        for i in range(1,121):
            lista.append(i)
        if self._estado == True:
            if self.canal in lista:
                canal +=1
                return self.canalUp 
            else:
                pass
        else:
            pass
    def canalDown(self, canal):
        lista = []
        for i in range(1,121):
            lista.append(i)
        if self._estado == True:
            if self.canal in lista:
                canal -=1
                return self.canal  
            else:
                pass
        else:
            pass

    def volumenUp(self,volumen):
        lista = [1,2,3,4,5,6,7]
        if self._estado == True:
            if self._volumen in lista:
                volumen +=1
                return self._volumen
            else:
                pass
        else:
            pass
    def volumenDown(self,volumen):
        lista = [1,2,3,4,5,6,7]
        if self._estado == True:
            if self._volumen in lista:
                volumen -=1
                return self._volumen
            else:
                pass
        else:
            pass
class Control:
    def __init__(self,tv):
        self.tv = tv
    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv

    def enlazar(self,televisor):
        self.televisor = televisor
        self.tv._control = televisor