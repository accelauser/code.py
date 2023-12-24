#deveria usar windows ou linux:
import random 

n_opções = int(input('número de opções: '))
while(n_opções <= 0):
    n_opções = int(input('número de opções: '))

count_opções = [0 for x in range(n_opções)]    
l_opções = [(input(f'digite a opção {x+1}: ')) for x in range(n_opções)]
precisão = int(input('precisão(%): '))  

for x in range(precisão*100):
    count_opções[random.randrange(n_opções)] += 1

print(f'A opção escolhida foi {str(l_opções[count_opções.index(max(count_opções))])} com {max(count_opções)} "votos"!!!')
