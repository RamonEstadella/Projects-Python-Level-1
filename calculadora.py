# CALCULADORA

class Calculadora:
    def __init(self):
        pass

    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "No es pot dividir per zero."
        
    def mostrar_menu(self):
        print("Seleccioneu una operació:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sortir")

    def executar(self):
        while True:
            self.mostrar_menu()
            eleccio = input("Introduïu la vostra elecció (1/2/3/4/5): ")

            if eleccio == '5':
                print("Sortint de l'Aplicació...")
                break

            if eleccio in ['1', '2', '3', '4']:

                '''
                num1 i num2 => Variables Locals: Són variables que es defineixen dins d'un mètode i només 
                existeixen durant l'execució d'aquest mètode. No són accessibles fora del mètode on es defineixen.
                
                '''
                try:
                    num1 = float(input("Introduiu el primer número: "))
                    num2 = float(input("Introduiu el segon número: "))

                except ValueError:
                    print("Si us plau, introduiu números vàlids.")
                    continue

                if eleccio == '1':
                    print(f"Resultat: {num1} + {num2} = {self.sumar(num1, num2)}")
                elif eleccio == '2':
                    print(f"Resultat: {num1} - {num2} = {self.restar(num1, num2)}")
                elif eleccio == '3':
                    print(f"Resultats: {num1} * {num2} = {self.multiplicar(num1, num2)}")
                elif eleccio == '4':
                    resultat = self.dividir(num1, num2)
                    print(f"Resultat: {num1} / {num2} = {resultat}")

            else:
                print("Elecció no vàlida. Si us plau, trieu una opció del 1 al 5.")

if __name__ == '__main__':

    # Creem una instància de la classe Calculadora
    calc = Calculadora()

    # Executem la calculadora
    calc.executar()
                    
