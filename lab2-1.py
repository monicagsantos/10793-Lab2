#9. Um grupo de pessoas participou num jantar em que todos encomendaram o menu turístico e pretende fazer 
#    um programa para calcular a conta. Para tal, o programa deve começar por ler o número de pessoas 
#    envolvidas no jantar e, de seguida, calcular o valor da conta. O menu custa 15,00 € + IVA por pessoa. 
#   Assuma que o IVA é 23%  e a gorjeta para o empregado é de 10% sobre o montante total com IVA. 
#   O programa deve exibir a despesa total sem IVA e sem gorjeta, o montante de IVA, o valor da gorjeta e a 
#    despesa total fnal.


nPessoas = int(input("Indique o numero de pessoas: "))

totalSemIVA = nPessoas * 15.0

iva = 15.0 * 0.23
menuComIVA = 15.0 + iva
gorjeta = menuComIVA * 0.1
menuTotal = menuComIVA + gorjeta
despesaFinal = menuTotal * nPessoas

print(totalSemIVA)
print(iva)
print(menuComIVA)
print(gorjeta)
print(menuTotal)
print(despesaFinal)

#10. Fazer um programa para calcular a contribuição para Segurança Social, IRS e o sindicato a partir do salário bruto, que é um atributo de entrada. 
#           • SS – 11,5% 
#           • IRS - 25% 
#           • Sindicato – 0,5 %
#   O programa deve imprimir o valor das contribuições e o valor do salário líquido.

bruto = int(input("Indique o salario bruto: "))

ss = bruto * 0.11
salario = bruto - ss

irs = salario * 0.25
salario -= irs

sindicato = salario * 0.05
salario -= sindicato

print("SS: ", ss)
print("IRS: ", irs)
print("Sindicato: ", sindicato)
print("Liquido: ", salario)

#11. Desenvolva um programa a solicitar a entrada de horas, minutos e segundos, calculando depois o tempo total em segundos