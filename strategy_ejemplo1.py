# Ejemplo 1 de Strategy --> Calcular multas por retraso en una biblioteca

class EstrategiaMulta:
    def calcular_multa(self, dias_retraso):
        pass

class MultaAlumno(EstrategiaMulta):
    def calcular_multa(self, dias_retraso):
        return dias_retraso * 0.50

class MultaProfesor(EstrategiaMulta):
    def calcular_multa(self, dias_retraso):
        return dias_retraso * 0.25

class SinMulta(EstrategiaMulta):
    def calcular_multa(self, dias_retraso):
        return 0

class Prestamo:
    def __init__(self, usuario, estrategia_multa):
        self.usuario = usuario
        self.estrategia_multa = estrategia_multa

    def calcular_multa(self, dias_retraso):
        multa = self.estrategia_multa.calcular_multa(dias_retraso)
        return self.usuario + " tiene que pagar " + str(multa) + " euros de multa."

if __name__ == "__main__":
    prestamo1 = Prestamo("Jaime", MultaAlumno())
    prestamo2 = Prestamo("Raul", MultaProfesor())
    prestamo3 = Prestamo("Laura", SinMulta())

    print(prestamo1.calcular_multa(6))
    print(prestamo2.calcular_multa(6))
    print(prestamo3.calcular_multa(6))
