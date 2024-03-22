import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
         "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Lista para almacenar las letras adivinadas
guessed_letters = []
# Número máximo de intentos permitidos
max_attempts = 10

print("¡Bienvenido al juego de adivinanzas!")
print("Seleccione un nivel de dificultad para jugar! Contamos con 3:")
print("1. Fácil: En la palabra a adivinar se muestran todas las vocales por defecto.")
print("2. Medio: Se muestra la primera y la última letra de la palabra.")
print("3. Difícil: No se muestra ninguna letra de la palabra.")
opc = input("Dificultad: ")

while opc not in ["1", "2", "3"]:
    print("Tipo de dificultad elegida incorrecta. Ingresa una correcta (1, 2, 3).")
    opc = input("Dificultad: ")

opc = int(opc)

if opc == 1:
    word_displayed = ''.join([letter if letter in "aeioóu" else "_" for letter in secret_word])
    guessed_letters.extend("aeioóu")
elif opc == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    guessed_letters.extend([secret_word[0], secret_word[-1]])
elif opc == 3:
    word_displayed = "_" * len(secret_word)

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed}")

failure_count = 0

while failure_count < 3:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter == "" or letter not in secret_word:
        print("Lo siento, la letra no está en la palabra.")
        failure_count += 1
    else:
        print("¡Bien hecho! La letra está en la palabra.")

    # Mostrar la palabra parcialmente adivinada
    word_displayed = ''.join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Te has equivocado {failure_count} veces y no puedes seguir jugando.")
    print(f"La palabra secreta era: {secret_word}")