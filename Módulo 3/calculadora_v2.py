op = int(input("Selecione um tipo de Operação: \n1-Soma\n2-Sub\n3-Multi\n4-Div:\n"))
v1 = (int(input("Digite o valor 1: ")))
v2 = (int(input("Digite o valor 2: ")))

if(op == 1):
    print(v1+v2)
elif(op == 2):
    print(v1-v2)
elif(op == 3):
    print(v1*v2)
else:
    print(v1/v2)

