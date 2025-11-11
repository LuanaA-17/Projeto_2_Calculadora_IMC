nome =input("Qual é o seu nome? ")
kg =float(input("Quanto vc pesa? "))
m =float(input("Qual é a sua altura? "))
imc = kg / (m ** 2)

if imc <=18.5:
    print('Voce esta abaixo do peso, procure uma nutricionista urgentemente!')

elif imc <= 24.9:
    print('Parabens, voce esta no seu peso ideal!')

elif imc <= 29.9:
    print('Voce atingiu o seu sobrepeso, manere no fastfood!')

elif imc <= 34.9:
    print('Cuidado voce atingiu o grau 1 da obesidade!')

elif imc <= 39.9:
    print('Voce atingiu o grau de obesidade 2! dois reais ou um infarto misterioso?')

else:
    print(f'{nome} o seu IMC é: {imc}')
    print('Voce atingiu a obesidade morbida! parabens voce ganhou um ou mais infartos misteriosos')
