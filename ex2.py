"""ex2.py """



#title           :ex2.py
#author          :Ahmed BENABDALLAH
#date            :18/03/2020
#usage           :python ex2.py
import math


try:
    value=int(input("Veuillez entrer un nombre entier :"))
except ValueError:
    print("Ce n'est pas une nombre")

print("Notre nombre est " + str(value))
print("******************************")
puis2 = pow(value,2)
print("Le carré du nombre " + str(value) +" est " + str(puis2))
print("******************************" + "\n")
racineCarre = math.sqrt(value)
print("La racine carré du nombre " + str(value) +" est " + str(racineCarre))





