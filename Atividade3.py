print('Atividade 3 - Estrutura de Repetição')

qtdPessoas = 0
qtdSim = 0
qtdNao = 0
qtdMulheresSim = 0
qtdHomensNao = 0

while qtdPessoas <10:
    resposta = input("Digite (S=sim, N=não e I=indiferente para avaliar) o novo jogo: ").upper()
    sexo = input("Digite o seu sexo, H para Homem e M para Mulher: ").upper()
    idade = int(input("Digite a sua idade: "))
    if resposta == 'S':
        qtdSim = qtdSim + 1
    elif resposta == 'N':
        qtdNao = qtdNao + 1

    if sexo == 'M' and resposta == 'S':
        qtdMulheresSim = qtdMulheresSim + 1
    if sexo == 'H' and resposta == 'N':
        qtdHomensNao = qtdHomensNao + 1
    qtdPessoas = qtdPessoas + 1

print('Quantas pessoas foram entrevistadas: %d'%(qtdPessoas))
print('Quantas pessoas disseram Sim: %d'%(qtdSim))
print('Quantas pessoas disseram Não: %d'%(qtdNao))
print(f'Quantas Mulheres disseram Sim: {qtdMulheresSim}')
print(f'Quantos Homens disseram Não: {qtdHomensNao}')