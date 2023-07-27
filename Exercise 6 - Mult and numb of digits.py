#Exercício 6:
#Elabora um programa que receba um inteiro,
#o multiplique por 12 e mostre o seu resultado
#e o número de dígitos do número.

numero = int (input ("introduza um numero"))
calculo1 = numero*12
print (calculo1)
numero_string= str(numero)
cumprimento_numero_string = len(numero_string)
print(cumprimento_numero_string)


