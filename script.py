print("Salário por hora")

salarioMensal = float(input("Qual seu salário mensal?: "))
horasTrabalhada = float(input("Quantas horas voce trabalha por dia?: "))
diasTrabalhado = float(input("Quantos dias você trabalha no mês? "))

horasTrabalhadaPorMes = horasTrabalhada * diasTrabalhado
salarioHora = salarioMensal / horasTrabalhadaPorMes
print(f"Seu salário por hora é: R$ {salarioHora:.2f}")

input()