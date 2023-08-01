from random import choice
from os import system

palabras = ["paloma", "toro", "mono", "jirafa", "elefante", "perro", "conejo", "gato"]

secreta = choice(palabras)
correctas = []
incorrectas = []
vidas = 6
aciertos = 0
letras = "abcdefghijklmnñopqrstuvwxyz"
contador = []
utilizadas = []


def ahorcado(vidas, aciertos):

	cant_secreta = len(secreta)

	print(f"\n\n---------- INICIO DEL JUEGO ------------\n\n")

	while vidas != 0 and cant_secreta != aciertos:

# ------------------- PEDIR UNA LETRA ------------------------

		letra = input("Ingrese una letra: ")
		letra = letra.lower()

# ------------------- VERIFICAR SI LA LETRA ES VALIDA ------------------------

		if letra in letras and letra != "" and letra not in utilizadas:
			utilizadas.append(letra)
# ------------------- VERIFICAR SI LA LETRA COINCIDE CON ALGUNA LETRA DE LA PALABRA SECRETA ------------------------

			if letra in secreta:

				for n in secreta:

					if letra == n:

						aciertos +=1

						print(f"\n---------- ACIERTO ---------\n\n"
							  f"La letra '{letra.upper()}' esta en la palabra\n\n"
							  f"Letras utilizadas: {utilizadas}\n"
							  f"Vidas restantes: {vidas}\n")


			else:

				vidas -= 1

				print(f"\n---------- ERROR ---------\n\n"
					  f"La letra '{letra.upper()}' no esta en la palabra\n\n"
					  f"Letras utilizadas: {utilizadas}\n"
					  f"Vidas restantes: {vidas}\n")

		else:
			print(f"\n---------- ERROR ---------\n\n"
				  f"Ingreso denegado por alguno de los siguientes motivos:\n\n"
				  f"\t* La letra ya fue utilizada anteriormente\n"
				  f"\t* No ha ingresado ningun caracter\n"
				  f"\t* No ha ingresado una letra\n")

# ------------------- SI LA PALABRA ESTA COMPLETA, EL JUEGO FINALIZA ------------------------

	if cant_secreta == aciertos:

		print(f"\n---------- FIN DEL JUEGO ------------\n\n"
			  f"¡FELICIDADES, has ganado el juego!\n\n"
			  f"La palabra es: '{secreta.upper()}'\n"
			  f"Vidas restantes: {vidas}\n")


		respuesta = input("Desea reiniciar el juego? s/n: ")
		respuesta = respuesta.lower()

		return respuesta

# ------------------- SI LAS VIDAS SE ACABAN, EL JUEGO FINALIZA ------------------------

	elif vidas == 0:
		print(f"\n---------- FIN DEL JUEGO ------------\n"
			  f"  ___\n"
			  " |	 |\n"
			  " o	 |\n"
			  "/|\  |\n"
			  "/\  _|_\n\n"
			  f"Te quedaste sin vidas\n\n"
			  f"La palabra era: {secreta}\n")
		respuesta = input("Desea reiniciar el juego? s/n: ")
		respuesta = respuesta.lower()
		return respuesta


respuesta = ahorcado(vidas, aciertos)


def reinicio(respuesta):

# ------------------- FUNCION PARA REINICIAR EL JUEGO ------------------------

	system("cls")
	utilizadas.clear()
	opciones = ["s", "n"]

	if respuesta in opciones:

		while respuesta == "s":

			ahorcado(vidas, aciertos)

		else:

			print("\n---------- JUEGO FINALIZADO ------------\n")

	else:
		print("Opcion invalida. Intente de nuevo")


reinicio(respuesta)
