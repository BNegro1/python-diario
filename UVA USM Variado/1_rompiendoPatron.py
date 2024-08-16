# Ingreso de números con la condición:
# Si se ingresa un número menor que el anterio, el programa
# Debe finalizar e imprimir cada número ingresado.
# En este caso True, NO debe contar el último ingresado.
l_num = []
suma = 0
while True:
    n = int(input("Ingreseun  número: "))
    l_num.append(n)
    for posicion in l_num:
        
            print(f'Valor verificador dentro de la lista: {suma}')
            print(f'Posicion actual: {l_num[posicion]}')
            print(f'Lista ns: {l_num}')
            
'''        elif l_num[suma] < n:
            suma += 1
            print("Último ingresado es menor")'''
