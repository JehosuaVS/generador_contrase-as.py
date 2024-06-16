import random

caracter = "+-/*!&amp;$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud= int(input("Introduce la longitud de la contraseña: "))

generated_password  = ""

for _ in range(longitud):
    generated_password  += random.choice(caracter)

print("La contraseña es:", generated_password )
