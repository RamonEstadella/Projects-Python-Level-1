# PASSWORD GENERATOR

import random # Importem el mòdul random per generar valors aleatòris
import string # Per accedir a constants de caràcters

def generar_contrasenya(longnitud, inclou_numeros, inclou_majuscules, inclou_minuscules, inclou_symbols):

    caracters = ""

    if inclou_numeros:
        caracters += string.digits
    if inclou_majuscules:
        caracters += string.ascii_uppercase
    if inclou_minuscules:
        caracters += string.ascii_lowercase
    if inclou_symbols:
        caracters += string.punctuation

    if not caracters:
        raise ValueError("Almenys una opció ha de ser seleccionada per generar contrasenyes.")
    
    return ''.join(random.choice(caracters) for _ in range(longnitud))

def main():
    print("Generador de contrasenyes segures")
    
    longitud = int(input("Introdueix la longitud de la contrasenya: "))
    inclou_numeros = input("Incloure números? (s/n): ").lower() == 's'
    inclou_majuscules = input("Incloure majúscules? (s/n): ").lower() == 's'
    inclou_minuscules = input("Incloure minúscules? (s/n): ").lower() == 's'
    inclou_symbols = input("Incloure simbols especials? (s/n): ").lower() == 's'

    contrasenya = generar_contrasenya(longitud, inclou_numeros, inclou_majuscules, inclou_minuscules, inclou_symbols)
    
    print(f"La teva contrasenya generada és: {contrasenya}")

if __name__ == '__main__':
    main()