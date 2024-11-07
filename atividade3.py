from pyDatalog import pyDatalog

# Criação dos termos
pyDatalog.create_terms('X, Y, Z, Nome, Idade, Departamento, Colaborador, Senior, DepartamentoColaborador, Contagem')

# Importação dos dados dos colaboradores
with open("colaboradores.txt", "r") as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(",")
        # Armazenando o nome, idade e departamento dos colaboradores
        +Colaborador(lista[0], int(lista[1]), lista[2])  # Idade convertida para inteiro

# Definindo o predicado Senior
Senior(Nome) <= Colaborador(Nome, Idade, Departamento) & (Idade > 30)

# Definindo o predicado DepartamentoColaborador
DepartamentoColaborador(Nome, Departamento) <= Colaborador(Nome, Idade, Departamento)

# Listando todos os colaboradores sêniores e seus departamentos
print("Colaboradores Sêniores e seus Departamentos:")
seniors_departamentos = Senior(X) & DepartamentoColaborador(X, Y)
print(seniors_departamentos)

# Contando colaboradores sêniores por departamento
# Gerar a lista de departamentos e colaboradores sêniores
departamentos_seniors = DepartamentoColaborador(Nome, Departamento) & Senior(Nome)

# Usando uma consulta para contar quantos colaboradores sêniores por departamento
Contagem(Departamento, Count) <= (departamentos_seniors[Y, Departamento] & (Y == Departamento)).count()

# Consultar a quantidade de colaboradores sêniores por departamento
print("Contagem de Colaboradores Sêniores por Departamento:")
print(Contagem(Y, Z))  # Exibe a contagem por departamento
