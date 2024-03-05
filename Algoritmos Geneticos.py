
import os
import random

def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2**(len(binario) - 1 - i)
    return decimal

def funcion_a_evaluar(numero):
    resultado = -30 * numero**2 - 23 * numero + 5
    return resultado

def intercambiar_ultimos_cuatro_digitos(numero1, numero2):
    numero1 = list(numero1)
    numero2 = list(numero2)
    
    numero1[-4:], numero2[-4:] = numero2[-4:], numero1[-4:]
    
    return ''.join(numero1), ''.join(numero2)

def main():
    resultados_consolidados = []

    while True:
        numero = 8 if not resultados_consolidados else len(resultados_consolidados)
        resultados = []

        for i in range(numero):
            if resultados_consolidados:
                
                jerarquia, binario, decimal, resultado = resultados_consolidados[i]
            else:
                binario = ''.join(random.choice('01') for _ in range(10))

                es_negativo = random.choice(['0', '1'])  
                tiene_decimal = random.choice(['0', '1'])  

                numero_decimal = binario_a_decimal(binario)
                if es_negativo == '1':
                    numero_decimal = -numero_decimal
                if tiene_decimal == '1':
                    numero_decimal += 0.5

                jerarquia, binario, decimal, resultado = i + 1, binario, numero_decimal, funcion_a_evaluar(numero_decimal)

            resultados.append((jerarquia, binario, decimal, resultado))

        print("\nResultados de la conversión binario a decimal:")
        print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
        for jerarquia, binario, decimal, resultado in resultados:
            print("{:<10} {:<15} {:<15} {:<15}".format(jerarquia, binario, decimal, resultado))

        random.shuffle(resultados)

        parejas = [resultados[i:i+2] for i in range(0, len(resultados), 2)]

        print("\nParejas formadas:")
        for index, pareja in enumerate(parejas, 1):
            print(f"\nPareja {index}:")
            print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
            for p in pareja:
                jerarquia, binario, decimal, resultado = p  
                print("{:<10} {:<15} {:<15} {:<15}".format(jerarquia, binario, decimal, resultado))

            if len(pareja) == 2:
                binario1, binario2 = intercambiar_ultimos_cuatro_digitos(pareja[0][1], pareja[1][1])
                decimal1 = binario_a_decimal(binario1)
                decimal2 = binario_a_decimal(binario2)
                resultado1 = funcion_a_evaluar(decimal1)
                resultado2 = funcion_a_evaluar(decimal2)
                pareja[0] = (pareja[0][0], binario1, decimal1, resultado1)
                pareja[1] = (pareja[1][0], binario2, decimal2, resultado2)
                print("\nDespués de intercambiar los últimos cuatro dígitos:")
                print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
                for p in pareja:
                    jerarquia, binario, decimal, resultado = p 
                    print("{:<10} {:<15} {:<15} {:<15}".format(jerarquia, binario, decimal, resultado))


                resultados_consolidados.extend(pareja)


        if len(resultados_consolidados) >= 2:
            indices = random.sample(range(len(resultados_consolidados)), 2)
            for index in indices:
                binary_str = resultados_consolidados[index][1]
                bit_index = random.randint(0, len(binary_str) - 1)
                mutated_bit = '1' if binary_str[bit_index] == '0' else '0'
                mutated_binary_str = binary_str[:bit_index] + mutated_bit + binary_str[bit_index+1:]
                decimal_value = binario_a_decimal(mutated_binary_str)
                new_result = funcion_a_evaluar(decimal_value)
                resultados_consolidados[index] = (
                    resultados_consolidados[index][0], 
                    mutated_binary_str, 
                    decimal_value, 
                    new_result
                )

        print("\nDespués de la mutación:")
        print("{:<10} {:<15} {:<15} {:<15}".format("Jerarquía", "Número binario", "Número decimal", "Resultado"))
        for p in resultados_consolidados:
            jerarquia, binario, decimal, resultado = p 
            print("{:<10} {:<15} {:<15} {:<15}".format(jerarquia, binario, decimal, resultado))

        continuar = input("\n¿Desea continuar con el ciclo? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
