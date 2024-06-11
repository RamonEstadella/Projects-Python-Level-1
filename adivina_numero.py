# ADIVINA EL NÚMERO

import random

class JocEndevinar:
    def __init__(self):
        self.numero_secret = random.randint(1, 10)
        self.intents = 0

    def demanar_numero(self):
        while True:
            try: 
                return int(input("Introdueix el teu número: "))
            except ValueError:
                print("Si us plau, introdueix un número vàlid.")

    def jugar(self):
        print("Endevinar el número entre 1 i 10!")

        while True:
            numero_usuari = self.demanar_numero()
            self.intents += 1

            if numero_usuari < self.numero_secret:
                print("Massa baix!")
            elif numero_usuari > self.numero_secret:
                print("Massa alt!")
            else:
                print(f"Felicitats! Has endevinat el número en {self.intents} intents.")
                break

if __name__ == "__main__":
    joc = JocEndevinar()
    joc.jugar()
