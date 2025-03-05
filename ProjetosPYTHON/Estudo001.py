name = input("Fale seu nome! >> ")
idade = int(input("Fale sua idade! >> "))

print(f"Seu nome é {name}, e sua idade é {idade}")

if idade == 10:
    print("Que legal!")
elif idade <= 18:
    print("lhe falta clt")
elif idade > 18:
    print("Ganhou clt")
else:
    print("Coloque valores válidos")