class Calculo_imc:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura / 100
        self.imc = peso / (self.altura ** 2)

        if peso < 0 or altura < 0:
            raise ValueError("Peso e altura devem ser valores positivos.")

        
        if self.imc < 18.5:
            self.classificacao = "Abaixo do peso"
        elif self.imc < 25:
            self.classificacao = "Peso normal"
        elif self.imc < 30:
            self.classificacao = "Sobrepeso"
        else:
            self.classificacao = "Obesidade"


        print(f"IMC: {self.imc:.2f}")

        print(f"IMC: {self.imc:.2f} - Classificação: {self.classificacao}")


peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em cm: "))

imc_calculator = Calculo_imc(peso, altura)
