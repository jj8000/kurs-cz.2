
class Walidator:
    def __init__(self, mleko, szkielet, pluca_narodziny, skrzydla, pluca_dorosle, luski):
        self.mleko = mleko
        self.szkielet = szkielet
        self.pluca_narodziny = pluca_narodziny
        self.skrzydla = skrzydla
        self.pluca_dorosle = pluca_dorosle
        self.luski = luski

    def __str__(self):
        if self.mleko == True:
            return "Ssak"
        elif self.szkielet == False:
            return "Owad"
        elif self.pluca_narodziny == True:
            if self.skrzydla == True:
                return "Ptaki"
            else:
                return "Gady"
        elif self.pluca_dorosle == False:
            return "Ryby"
        elif self.luski == True:
            return "Ryby"
        return "Płazy"



# mleko, szkielet, pluca_narodziny, skrzydla, pluca_dorosle, luski

gad = Walidator(0, 1, 1, 0, 1, 1)
print(gad)
żaba = Walidator(0, 1, 0, 0, 1, 0)
print(żaba)
nietoperz = Walidator(1, 1, 1, 1, 1, 0)
print(nietoperz)
mysz = Walidator(1, 1, 1, 0, 1, 0)
print(mysz)