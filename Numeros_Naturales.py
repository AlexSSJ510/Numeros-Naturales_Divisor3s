import math

class CalcularDivisor:
    def __init__(self):
        self.num = None

    def CalcDivisores(self):
        divisores = []
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                divisores.append(i)
        return divisores

    def num_Natural(self):
        while True:
            try:
                N_natural = input("Ingrese un número natural: ")
                self.num = int(N_natural)
                if self.num < 0:
                    raise ValueError("El número debe ser natural (mayor o igual que 0).")
                return self.num
            except ValueError as e:
                print(f"Número no válido: {e}. Inténtelo de nuevo.")

    def Calcular(self):
        self.num_Natural()
        divisores = self.CalcDivisores()
        print(f"Los divisores de {self.num} son: {divisores}")


if __name__ == "__main__":
    Main_Calc = CalcularDivisor()
    Main_Calc.Calcular()
