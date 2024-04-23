#DESAFIO DESENVOLVIMENTO WEB 2
def reajuste(salario):
    salarios = [
        (280.00, 20),
        (700.00, 15),
        (1500.00, 10),
        (float('inf'), 5)
    ]

    percentual = 0

    for salarioBase, aumento in salarios:
        if salario <= salarioBase:
            percentual = aumento
            break
    
    aumento = salario * (percentual / 100)
    
    salarioNovo = salario + aumento

    inflacao = 3.8 / 100
    
    aumentoReal = aumento - (salario * inflacao)
    
    ajuste = salarioNovo - (salario * inflacao)
    
    return {
        "Salario antes do reajuste": salario,
        "Percentual de aumento": percentual,
        "Valor do aumento": aumento,
        "Novo salario": salarioNovo,
        "Aumento real apos inflacao": aumentoReal,
        "Novo salario ajustado pela inflacao": ajuste
    }

print(reajuste(800.00))
