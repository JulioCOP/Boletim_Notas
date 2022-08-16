from time import sleep

lista=[]
print()
print("#"*7 ,"\033[1;33mBOLETIM DE NOTAS\033[m", "#"*10)
sleep(1)
while True:
    nome=(str(input('NOME DO ALUNO: ')))
    nota1=float(input("1° NOTA DO ALUNO(A): "))
    nota2=float(input("2º NOTA DO ALUNO(A): "))
    nota3=float(input("3º NOTA DO ALUNO: "))
    while nota1>40 or nota2>40 or nota3>20:
        print()
        print("\033[7;31;40mNOTAS LANÇADAS MAIOR DO QUE O PERMITIDO.\033[m"
              "\033[1m\nLANCE NOVAMENTE OS VALORES CORRETOS.\033[m")
        nota1 = float(input("1° NOTA DO ALUNO(A): "))
        nota2 = float(input("2º NOTA DO ALUNO(A): "))
        nota3 = float(input("3º NOTA DO ALUNO: "))
        print()
    if nota1<=40 or nota2<=40 or nota3<=20:
        print("\033[7;33;40mCADASTRANDO NOTAS NO SISTEMA\033[m")
        sleep(0.5)
        print("\033[7;33m.\033[m", end="")
        sleep(0.5)
        print("\033[7;33m.\033[m", end="")
        sleep(0.5)
        print("\033[7;33m.\033[m", end="")
        sleep(0.5)
        print("\033[7;33m.\033[m", end="")
        pass
    nota_final=nota1+nota2+nota3
    media = ((nota1 + nota2 + nota3 )/ 2)
    lista.append([nome,[nota1,nota2, nota3],nota_final, media])
    print()
    resp= str(input("\033[1;37m\nVocê deseja adicionar mais algum aluno ? [S] / [N] \033[m")).strip().upper()
    while resp not in 'SN':
        resp = str(input("\033[7;31;40mRESPOTA INCORRETA !\033[m"
                         "\033[1m\nVocê deseja adicionar mais algum aluno ? [S] / [N]\033[m ")).strip().upper()
    if resp=='N':
        break
print()
print(f"\033[7;40m{'Nº':<10} {'ALUNO':<10} {'TOTAL':>10} {'MÉDIA':>10}\033[m")
sleep(0.5)
for numero, aluno in enumerate (lista):
    print(f"\033[1m{numero:<10} {aluno[0]:<10} {aluno[2]:>10.2f} {aluno[3]:>10.2f}\033[m")
print()
sleep(0.5)
print("\033[1;30;46mSITUAÇÃO DOS ALUNOS:\033[m")
for nota_final in lista:
    if nota_final[2]>=60:
        print(f"\033[1;32m\n{nota_final[0]} APROVADO\033[m",end=" ")
    elif nota_final[2]<40:
        print(f"\033[1;31m\n{nota_final[0]} REPROVADO\033[m",end=" ")
    else:
        print(f"\033[1;33m\n{nota_final[0]} EXAME ESPECIAL\033[m", end=" ")
print()
print()
while True:
    print("\033[7;35;40m=-\033[m"*50)
    sleep(1)
    print("\033[1mUsuário, quais notas e média você deseja ver , de acordo com os Nºs? \033[m"
          "OU \n\033[1mDIGITE \033[1;34m-1\033[m SE DESEJAR FINALIZAR O PROGRAMA.\033[m")
    nota_aluno=int(input())
    if nota_aluno==-1:
        break
    if nota_aluno<= len(lista)-1:
# len(ficha) é a quantidade de alunos cadastrados ou inseridos na lista
#para este comando =  o usuário selecina um valor de 0 até o determinando números de itens que possui a lista
# e assim é mostrado as notas do aluno desejado, de acordo com a posição escolhida.
# ex: Se o usuário estiver digitado Pedro na 2º posição (1 para o python), será mostrado suas duas notas
        print(f"Notas de \033[1;35m{lista[nota_aluno][0]}\033[m são \033[1;35m{lista[nota_aluno][1]}\033[m")

sleep(1)
print("\033[4;31mPROGRAMA ENCERRADO\033[m")