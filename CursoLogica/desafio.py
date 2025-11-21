class Jogador:
    def __init__(self, Name, Ranking):
        self.Name = Name
        self.Ranking = Ranking

    def VerificarPatente(self):
        if self.Ranking < 1000:
            print("Sua patente é Ferro")
        elif self.Ranking < 2001:
            print("Sua patente é Bronze")
        elif self.Ranking < 5001:
            print("Sua patente é Prata")
        elif self.Ranking < 7001:
            print("Sua patente é Ouro")
        elif self.Ranking < 8001:
            print("Sua patente é Platina")
        elif self.Ranking < 10000:
            print("Sua patente é Ascendente")
        elif self.Ranking > 10001:
            print("Sua patente é Imortal")
        else:
            print("Sua patente é Radiante")


P1 = Jogador('wendell', 6000)  
P1.VerificarPatente()
