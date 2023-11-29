#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

def obtener_opcion_aleatoria():
    opciones = ['piedra', 'papel', 'tijeras']
    return random.choice(opciones)

def determinar_ganador(jugador, oponente):
    if jugador == oponente:
        return "Empate"
    elif (jugador == 'piedra' and oponente == 'tijeras') or \
         (jugador == 'tijeras' and oponente == 'papel') or \
         (jugador == 'papel' and oponente == 'piedra'):
        return "¡Has ganado!"
    else:
        return "¡Has perdido!"

def jugar():
    puntos_jugador = 0
    num_rondas = 0

    while True:
        print("\nElige: piedra, papel o tijeras. Para salir, escribe 'salir'.")
        eleccion = input("Tu elección: ").lower()

        if eleccion in ['piedra', 'papel', 'tijeras']:
            opcion_oponente = obtener_opcion_aleatoria()
            resultado = determinar_ganador(eleccion, opcion_oponente)
            print(f"\nElegiste: {eleccion}. El oponente eligió: {opcion_oponente}. {resultado}")
            num_rondas += 1

            if resultado == "¡Has ganado!":
                puntos_jugador += 1
            elif resultado == "¡Has perdido!":
                puntos_jugador -= 1

            print(f"Puntos: {puntos_jugador}")
        elif eleccion == 'salir':
            break
        else:
            print("Opción no válida. Por favor, elige piedra, papel o tijeras.")

    print(f"\n¡Gracias por jugar {num_rondas} ronda(s)!")
    print(f"Tu puntuación final es: {puntos_jugador}")

if __name__ == "__main__":
    jugar()
