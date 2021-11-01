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

            

