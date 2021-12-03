def printState():
   
    print(str(Firstnumber) + "+" + str(Secondnumber) + "=" + str(Firstnumber))
    print(str(Firstnumber) + "×" + str(Secondnumber) + "=" + str(Firstnumber * Secondnumber))
    print(str(Firstnumber) + "÷" + "by" + str(Secondnumber) + "=" + str(Firstnumber/Secondnumber))
    print(str(Firstnumber) + "Modulo" + str(Secondnumber) + "=" + str(Firstnumber%Secondnumber))
    print(str(Firstnumber) + "exponent" + str(Secondnumber) + "=" + str(Firstnumber**Secondnumber))	


Firstnumber = 30
Secondnumber = 10

printState()

def printState():
	Temperature = input("What is the temperature in degree Celsius?")
	print("The temperature in Fahrenheit is" + str(Temperature*9/5+32))

