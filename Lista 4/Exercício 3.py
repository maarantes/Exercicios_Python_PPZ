import random

vetor1 = random.sample(range(100), 10)
vetor2 = random.sample(range(100), 10)
vetor3 = []

for x in range(10):
    if x % 2 == 0:
        vetor3.insert(x, vetor1[x])
    else:
        vetor3.insert(x, vetor2[x])

print ("Vetor 1:" , vetor1)
print ("Vetor 2:", vetor2)
print ("Vetor 3:" , vetor3)