# find() e index(): ambos retornam o índice da primeira ocorrência 
# de um determinado caractere. Caso o caractere não exista, o find retorna -1 e o index dá erro.


str = "Cena Oculta"
print("----- find() e index()")

indice1 = str.find('a')
indice2 = str.index("a")

print(indice1)
print(indice2)


# upper() e lower(): convertem os elementos da string para maiúsculo e minusculo
print("----- upper() e lower()")
str = "Cena Oculta"
nova_str = str.upper()
print( nova_str )
print( str.lower() )


print("----- capitaliza()")
str = "CONVERGENTE foi o FILME MAIS origGINAL"
print(str.capitalize())