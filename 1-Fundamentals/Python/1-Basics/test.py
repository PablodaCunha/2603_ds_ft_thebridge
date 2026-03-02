# print(type(None))

# print(None)

# lista = [1, 2, 3, 4]

# print(lista.append(5))

# print(lista)

# # def apender(x):
# #     y = x.pop()
# #     x.append(y)
# #     x.append(y+1)
# #     print(x)
# #     return x

# def apender_1(list):
#     list = list.append(list[-1]+1)
#     return list

# print(lista)

# apender_1(lista)

# print(lista)

# apender_1(lista)

# print(lista)

# apender_1(lista)

# print(lista)


# apender_1(lista)
# apender_1(lista)
# apender_1(lista)

# print(print(lista))

# formato = 'Vamos a meter estas cosas: %s opcion 1, %s opcion 2, %s opciones 3'
# opciones = ('x1', 'x2', 'x3')

# junto = formato % opciones

# print(junto)

# print('-' * 70)

# print(type('hola'.upper()))

# Binario 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 decimal



def binario_a_decimal(binario_str):
    number = 0
    for i, x in enumerate(binario_str[::-1]):
        if x == '1':
            number += 2 ** i
        else:
            number += 0
        print(f"Paso previo {number}")
    print(number)
    return number

binario_a_decimal('110')

print(list(enumerate('110'[::-1])))
# Menú interactivo
# while True:
#     print("\n1. Binario → Decimal")
#     print("2. Decimal → Binario") 
#     print("3. Salir")
    
#     opcion = input("Elige (1-3): ")
    
#     if opcion == '1':
#         binario = input("Binario: ")
#         resultado = binario_a_decimal(binario)
#         print(f"→ {resultado}")
    
#     elif opcion == '2':
#         decimal = int(input("Decimal: "))
#         resultado = decimal_a_binario(decimal)
#         print(f"→ {resultado}")
    
#     elif opcion == '3':
#         break


