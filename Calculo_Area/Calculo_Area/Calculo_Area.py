print ("Bem-vindo ao programa de calculo da area de Retangulos e Circulos")
print ("-----------------------------------------------")
print ("Programa criado por Bruno Rafael")
print ("================================")

#Menu de escolha do usuário
print ("Escolha a forma que deseja calcular a area:")
print ("Digite a para calcular area do retangulo")
print ("Digite b para calcular area do circulo")

#escolha do usuário
escolha = input("Digite a opcao desejada: ")

#calculando a area
if escolha =="a":
    altura = int(input("Qual a altura do Retangulo: "))
    largura = int(input("Qual a largura do Retangulo: "))
    area = (altura*largura)
    print(area);
else:
    raio = int(input("Digite o Raio do circulo: "))
    area2 = 3.14 * (raio**2)
    print ("A area do circulo e ", area2)