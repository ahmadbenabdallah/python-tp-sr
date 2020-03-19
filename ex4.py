""" ex4.py """



#title           :ex4.py
#author          :hmed BENABDALLAH
#date            :18/03/2020
#usage           :python ex4.py


liste = eval(input("Entrer la liste du trois nombres : "))
def Reverse(tuples): 
    new_tup = tuples[::-1] 
    return new_tup 


print(Reverse(liste))


