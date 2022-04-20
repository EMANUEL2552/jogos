class Televisão:


    def __init__(self,):
        self.ligada = False
        self.canal = 2
        self.cmin = 2
        self.cmax = 14

    def muda_canal_para_baixo(self):
        if (self.canal-1>=self.cmin):

           self.canal-=1

    def muda_canal_para_cima(self):
        if (self.canal + 1 <= self.cmax):
            self.canal += 1

tv = Televisão(1,99)
for x in range(0,120):
    print(tv.canal)
for x in range(0, 120):
    tv.muda_canal_para_baixo()
    print(tv.canal)