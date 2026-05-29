arquivo = open('arqText', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close

#Leitura do arquivo texto

leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close()