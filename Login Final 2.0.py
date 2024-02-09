import time
ns = ["nomes_e_senhas.txt"]                              #LISTA DE  NOMES E SENHAS

print ('=' * 55)             #Linhas de Frescura
print ('Seja Bem vindo! Por Favor faça o seu Login logo Abaixo')
print ('=' * 55)             #Linhas de Frescura

n = (input("Nome: "))                   
s = str(input("Senha: "))
if n and s in ns:
    print('=' * 15)
    print('Login Concluido')
    print('=' * 15)

elif n and s not in ns:                                                  #SE O NOME NÃO ESTIVER EM NOMES, IRÁ PEDIR PARA CRIAR
   time.sleep(1)                           #Tempo de Espera
   print ('=' * 60)             #Linhas de Frescura   
   print('Seu nome ou senha não foi encontrado, por favor crie um aqui')  
print ('=' * 60)             #Linhas de Frescura
ni = str(input("Crie seu Nome de Usúario: "))
si = str(input("Crie sua Senha: "))
ns.append(ni)
ns.append(si)

time.sleep(2)                       #Tempo de Espera

print ('=' * 38)           #Linhas de Frescura
print ('Senha e Nome Criados')
print ('=' * 38)             #Linhas de Frescura

time.sleep(2)                           #Tempo de Espera

with open("nomes_e_senhas.txt", "w") as nomes_e_senhas:             # SALVA OS NOME E SENHAS NO ARQUIVO
    for item in ns:
        nomes_e_senhas.write(item + '\n')

print ('   ---  Faça Login novamente  ---')                          #IRÁ PEDIR PARA FAZER O LOGIN NOVAMENTE, AGORA COM O NOME E SENHA CRIADOS ANTERIORMENTE
print ('=' * 38)             #Linhas de Frescura

while True:
    
    no = input('Nome: ')
    se = input('Senha: ')
    
    
    if no in ns and se in ns:
        time.sleep(3)                           #Tempo de Espera
        print('=' * 15)
        print('Login Concluido')
        print('=' * 15)
        
        break                                           # Sai do loop após o login ser concluído
    
    else:
        time.sleep(3)                           #Tempo de Espera
        print('=' * 51)            #Linhas de Frescura
        print('Nome ou Senha incorretos, Por Favor Tente Novamente')
        print('=' * 51)            #Linhas de Frescura