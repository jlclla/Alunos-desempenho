#Código para  automatizar o cálculo de notas dos alunos de uma escola.

#Boas-vindas ao sistema de cálculo de notas!

def calcular_notas(nome_aluno, nota1, nota2, nota3):


#Calcular a média das notas - Entrada de dados
   
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

#Cálculo da média e verificação de aprovação ou reprovação - Processamento de dados

if media >= 6:
    print(f"Parabéns! Sua média é {media:.2f}. Você foi aprovado(a)!")
else:
    print(f"Sua média é {media:.2f}. Infelizmente, você foi reprovado(a).")  

