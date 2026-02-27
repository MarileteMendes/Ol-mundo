#entradas/variaveis
preco_amaciante1 = float(input ("Digite o preco do 1º amaciante R$ "))
preco_amaciante2 = float(input("Digite o preço do 2º amaciante R$ "))
#processos
if preco_amaciante1<preco_amaciante2:
    mais_caro = "O primeiro amaciante é o mais barato"
elif preco_amaciante2<preco_amaciante1:
    mais_caro = " O segundo amaciante é o mais barato"
else:
    mais_caro = "Ambos tem o mesmo preço"    
#saidas  
print(mais_caro)
