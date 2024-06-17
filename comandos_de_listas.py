lista = [1,"goku",3] #lista
print (lista)
for pepito in lista:
    lista[1]="richi"
    print (pepito)
    print(lista)
print ("------------")
print (lista[1])
#.append ----> permite agregar elementos al final de la lista
nombre=input("ingrese nombre: ")
lista.append(nombre)
print ("------------")

for x in lista:
    print (x)
print ("------------")

#.insert -----> permite agregar elementos de forma especifica

lista.insert(1,"emma stone")
print ("-------------")

for x in lista:
    print (x)
print ("------------")

#.remove --> eliminar elementos de la lista (remover)
lista.remove("richi")

for x in lista:
    print (x)
print ("------------")
#.pop permite elminar elementos por la posicon de la lista
lista.pop(1)

for x in lista:
    print (x)
print ("------------")

#.clear --> borra todos los elementos de la lista
lista.clear()
print ("------------")

for x in lista:
    print (x)
print ("------------")
#.sort no cacho XD