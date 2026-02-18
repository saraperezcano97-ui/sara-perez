Ejercicios básicos de repaso:

#Ejercicio 1 
print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
print (" Sara \n Huelva")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")
print(type(int("12345")))

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
nombre = "midudev"
edad = 36
altura=165
print(f"Hola {nombre} , tu edad es {edad} y mides {altura}")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")
variable_pi=int(round( 3.1416))
print(variable_pi /2)
print(round(variable_pi/2))
#la manera correcta 
resultado = int(round(3.1416) / 2)
