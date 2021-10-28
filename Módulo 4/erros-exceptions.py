#print("ola)

from typing import IO


def numDiv(num1, num2):
    resultado = num1/num2
    print(resultado)

print(numDiv(4,2))
#print(numDiv(4,0))

try:
    8+"a"
except TypeError:
    print("Operação nao permitida")

try:
    f = open("arquivos/testandoerros.txt", "w")
    f.write("Gravando no arquivo")
except IOError:
    print("Erro: arquivo não encontrado ou não pode ser salvo")
else:
    print("COnteudo gravado com sucesso")
    f.close()

try:
    f=open("arquivos/testandoerros.txt", "r")
    f.write("Gravando no arquivo")
except IOError:
    print("Esse arquivo não foi encontradno ou não pode ser lido")
else:
    print("conteudo gravado com sucesso")
    f.close()

try:
    f=open("arquivos/testandoerros.txt", "w")
    f.write("Gravando no arquivo")
except IOError:
    print("Esse arquivo não foi encontradno ou não pode ser lido")
else:
    print("conteudo gravado com sucesso")
    f.close()
finally:
    print("COmando no bloco finally executado")

def askint():
    try:
        val = int((input("Digite um numero: ")))
    except UnboundLocalError:
        print("Voce não digitou um número")
    finally:
        print("Obrigado")
    print(val)

askint()

def askint():
    while True:
        try:
            val = int((input("Digite um numero: ")))
        except:
            print("Voce não digitou um número")
            continue
        else:
            print("Obrigado por digitar um numero'")
            break
        finally:
            print("Fim da execução")
    print(val)

askint()


tuple = (1,2,3,4,5)

try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print("Erro: ", e)
except IOError as e:
    print("Erro de I/O: ", e)






