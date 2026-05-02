

notaA=float(input("Informe a primeira nota:"))
notaB=float(input("Informe a Segunda Nota:"))

#calcular a media
mediafinal= (notaA+notaB) /2

#verificação
if mediafinal >= 7.0:
    print("A média: %.1f APROVADO"% mediafinal)
else:
    print("A média:%.1f - REPROVADO"%mediafinal)