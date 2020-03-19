"""ex5.py:"""



#title           :ex5.py
#author          :hmed BENABDALLAH
#date            :18/03/2020
#usage           :python ex5.py
import math


value=float(input("Veuillez entrer un nombre flottant :"))
if (value >=0) :
    racineCarre=math.sqrt(value)
    print("la racine carré de "+ str(value) +" est "+ str(racineCarre))
    
else :
    print("Ce n'est pas une nombre positif est supérieur à zéro")


