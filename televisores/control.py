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
        