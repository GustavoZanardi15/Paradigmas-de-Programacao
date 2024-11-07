from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, A, B, Colaborador, Projeto, ParticipaDe, DepartamentoColaborador')

with open('colaboradores.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(',')
        +Colaborador(lista[0], lista[1], lista[2])

with open('projetos.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(',')
        +Projeto(lista[0], lista[1])

with open('alocacoes.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(',')
        +ParticipaDe(linha[0],linha[1])

ParticipaDe(X, A) <= Colaborador(X, Y, Z) & Projeto(A, Z)
DepartamentoColaborador(X, Z) <= Colaborador(X, Y, Z)

print("Colaboradores, Projetos e Departamentos:")
print(ParticipaDe(X, A) & DepartamentoColaborador(X, Z))