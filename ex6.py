""" ex6.py """



#title           :ex6.py
#author          :Ahmed BENABDALLAH
#date            :18/03/2020
#usage           :python ex6.py


k=int(input("Entrer un nombre : "))

x = range(1,k,1)

sommePair = 0
sommeImpair =0
for n in x:
  print(n)
  if (n % 2) == 0 :
   sommePair = sommePair + n
  else:
   sommeImpair = sommeImpair + n

print("La somme de nombre pair est " + str(sommePair))
print("La somme de nombre impair est " + str(sommeImpair))