# Obaida Kurea opdracht: Pizza calculator

aantalsmallpizzas = int(input  ("how many small pizza's do you want?"))

aantalmediumpizzas = int(input ("how many medium pizza's do you want?"))

aantallaregepizzas = int(input ("how many large pizza's do you want?"))


pizzasmallprijs = 5
bedragpizzasmall = aantalsmallpizzas * pizzasmallprijs


print ("u heeft " + str (aantalsmallpizzas) + " smallpizza " + " voor "+ str (bedragpizzasmall) + " euro" )


pizzamediumprijs = 8
bedragpizzamedium = aantalmediumpizzas * pizzamediumprijs


print ("u heeft " + str (aantalmediumpizzas) + " mediumpizza " + " voor "+ str (bedragpizzamedium) + " euro" )


pizzalargeprijs = 11
bedragpizzalarge = aantallaregepizzas * pizzalargeprijs


print ("u heeft " + str (aantallaregepizzas) + " largepizza " + " voor "+ str (bedragpizzalarge) + " euro" )


bedragallepizzas = (pizzalargeprijs * aantallaregepizzas) + (pizzamediumprijs * aantalmediumpizzas) + (pizzasmallprijs * aantalsmallpizzas)

print (bedragallepizzas)