import random 
import matplotlib.pyplot as plt
import numpy as np 

n_indiv = int(input('Quantos individuos existem na amostra:  '))
n_gera = int(input('Quantas gerações existem na amostra:  '))
geração = []
x_axis = []
repetições = []
absoluto = [] #contagem absoluta de genes por geração
n_alelos = n_indiv * 2

for i in range(n_gera): #gera o tamano da matrix
    geração.append([])

for j in range(1, n_alelos + 1): #gera as listas em cara iteração da matrix
    geração[0].append(j)
    repetições.append([]) #gera as listas vazias para a contagem de repetições em cara geração
    absoluto.append([])

for y in range(1, len(geração)): #a partir da 1° geração sorteia números da última e muda a lista
    escolhas = [] #cria a lista das escolhas de cara geração
    for x in range(n_alelos): #sorteia números para cada alelo 
        escolhas.append(random.choice(geração[y-1])) #cria um número aleatório entre os números da última geração
    geração[y] = escolhas #a    diciona na lista 

for g in range(n_gera):
    x_axis.append(g+1) #adiciona na lista do eixo X a quantidade de gerações

    #plt.figure()  # Create a new figure for each generation
    #plt.title(f"Contagem de alelos da geração {g+1}")

    # Count the occurrences of each individual in the current generation
    unique_individuals = list(set(geração[g]))
    count_individuals = [geração[g].count(b) for b in unique_individuals]

    if g == n_gera-1: #se a geração for a última mostra o gráfico
        plt.figure()
        plt.title(f"Contagem de alelos da geração {g+1}")
        plt.bar(unique_individuals, count_individuals, width=0.5)

    #contar quantos de cada tem de cada um  
    for ind in range(n_alelos): #pega os alelos 
        m = geração[g].count(ind+1) #acessa a lista geração e conta o index do alelo q ta no loop
        n = m/n_alelos
        absoluto[ind].append(m) 
        repetições[ind].append(n) #adiciona o número de repetiçções na lista repetição no index do alelo (o ńumero de alelos diz a quantidade de itens na lista repetições, a quantidade de gerações a quantidade de itens na lista repetições[x] matrix ixj)
    
plt.figure()  # Create a new figure for each generatio n 
plt.title(f"Frequência alelica ao longo das gerações")
plt.xlim([1,n_gera+1]) #limita o tamanho do eixo X
plt.ylim([-0.5, 1 ]) #limita o tamanho do eixo y
for x in range(n_alelos): #passa por todas gerações pra gerar individualemnte os gráficos dos alelos 
    plt.plot(x_axis, repetições[x], label = f'Alelo {x+1}') #cria a legenda pra cada linha

plt.figure()  # Create a new figure for each generatio n 
plt.title(f"Quantidade de alelos ao longo das gerações")
plt.xlim([1,n_gera+1]) #limita o tamanho do eixo X
plt.ylim([-1, n_alelos+1]) #limita o tamanho do eixo y
for x in range(n_alelos): #passa por todas gerações pra gerar individualemnte os gráficos dos alelos 
    plt.plot(x_axis, absoluto[x], label = f'Alelo {x+1}') #cria a legenda pra cada linha

#plt.legend(loc='upper left') #mostra a legenda
plt.show() #cria a janela para mostrar o gŕafico 