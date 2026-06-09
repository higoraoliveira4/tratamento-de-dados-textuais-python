lista = [
    "João, 14 anos, Pereira Barreto",
    "Pedro, 20 anos, Ilha Solteira",
    "Airton, 47 anos, Santa Fé do Sul",
    "Pablo, 34 anos, Três Lagoas",
    "Mariana, 29 anos, São Paulo",
    "Carlos, 41 anos, Campinas",
    "Fernanda, 36 anos, Goiânia",
    "Rafael, 22 anos, Brasília",
    "Ana Clara, 18 anos, Rio de Janeiro",
    "Lucas, 25 anos, Belo Horizonte",
    "Beatriz, 31 anos, Curitiba",
    "Gustavo, 27 anos, Porto Alegre",
    "Juliana, 45 anos, Salvador",
    "Ricardo, 39 anos, Recife",
    "Camila, 24 anos, Florianópolis",
    "Eduardo, 52 anos, Ribeirão Preto",
    "Patrícia, 33 anos, Santos",
    "Felipe, 19 anos, Sorocaba",
    "Aline, 28 anos, Uberlândia",
    "Marcelo, 44 anos, Londrina",
    "Larissa, 21 anos, Campo Grande",
    "Bruno, 37 anos, Cuiabá",
    "Natália, 26 anos, Vitória",
    "Henrique, 48 anos, São José do Rio Preto",
    "Priscila, 30 anos, Niterói",
    "Diego, 35 anos, Maceió",
    "Renata, 42 anos, Fortaleza",
    "Vinícius, 23 anos, João Pessoa",
    "Tatiane, 32 anos, Aracaju",
    "André, 40 anos, Manaus"
]

print (f"{'Nome':<10} | {'Idade':<10} | {'Cidade':<10}")

for linha in lista:
    nome,idade,cidade = linha.split(",")

    nome = nome.strip()
    idade = idade.strip()
    cidade = cidade.strip()

    idade = idade.replace("anos","")
    idade = int(idade.strip())

    print (f"{nome:<10} | {idade:<10} | {cidade:<10}")