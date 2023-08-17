palavra = "paralelepípedo"
for letra in palavra:
    print(letra, end="\n")
print("Fim")

aprovados = ["Rafaela", "Renato", "Pedro", "Maria" ]
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f"{posicao + 1})", nome)

dias_semanas = ("Domingo", "Segunda", "Terça",
                "Quarta", "Quinta", "Sexta", "Sabado")
for dia in dias_semanas:
    print(f"Hoje é {dia}")

for numero in {1, 2, 3, 4, 5}:
    print(numero)