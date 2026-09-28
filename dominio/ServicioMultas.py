class ServicioMultas:
    def __init__(self, tarifa_diaria):
        self.tarifa_diaria = tarifa_diaria

    def calcular_multa(self, dias):
        total = dias * self.tarifa_diaria
        return total
  
    