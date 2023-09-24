pais_a = 80000
pais_b = 200000

anos = 0

while pais_a <= pais_b:
    pais_a = pais_a + pais_a * 3/100
    pais_b = pais_b + pais_b * 1.5/100
    anos = anos + 1

print ("Vai demorar" , anos , "anos para o País A ultrapassar o País B.")