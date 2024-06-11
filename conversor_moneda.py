# CONVERSOR MONEDA

class ConversorMoneda:
    def __init__(self, tipus_de_canvi, moneda_base="USD"):
        self.tipus_de_canvi = tipus_de_canvi
        self.moneda_base = moneda_base

    def convertir(self, quantitat, moneda_destinacio):
        if moneda_destinacio not in self.tipus_de_canvi:
            raise ValueError("Moneda de destinació no vàlida")
        
        tipus_de_canvi = self.tipus_de_canvi[moneda_destinacio]

        return quantitat * tipus_de_canvi
    

def main():
    tipus_de_canvi = {
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0,
        "CAD": 1.25,
        "AUD": 1.30,
        "CHF": 0.91,
        "CNY": 6.45,
        "INR": 73.50,
        "MXN": 20.00
    }

    conversor = ConversorMoneda(tipus_de_canvi)

    while True:
        try: 
            quantitat = float(input("Introdueix la quantitat a convertir: "))
            moneda_destinacio = input("Introdueix la moneda de destinació (ex. EUR, GBP, JPY, CAD): ").upper()
            resultat = conversor.convertir(quantitat, moneda_destinacio)
            print(f"{quantitat} {conversor.moneda_base} equivalen a {resultat} {moneda_destinacio}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")
        
        continuar = input("Vols fer una altra conversió? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()