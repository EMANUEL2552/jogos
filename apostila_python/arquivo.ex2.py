#Listagem 9.1 – Abrindo, escrevendo e fechando um arquivo

arquivo= open('numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write('%d\n' % linha)
arquivo.close()

#Listagem 9.2 – Abrindo, lendo e fechando um arquivo

arquivo=open('numeros.txt','r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()