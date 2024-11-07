from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y,Z, A, B, Nomes, Colaborador, Projeto')

with open('colaboradores.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(',') 
        +Colaborador(lista[0]) 

with open('projetos.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(',')
        +Projeto(lista[0]) 

print("Colaboradores:")
print(Colaborador(X))

print("\nProjetos:")
print(Projeto(Y))
