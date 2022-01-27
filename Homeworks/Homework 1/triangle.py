import random
list = []
results = []

elements = 0
for i in range(0,100):
    elements = elements + i
elements = 4950

for i in range(elements):
    list.append(random.randint(0,100))

j = 0
for i in range(1, 100): # for range from triangle
    if(j < (i*(i/2+0.5))):
        if(list[j]<list[j+1]):
            results.append(list[j+1])
        else:
            results.append(list[j])
        while(j < (i*(i/2+0.5))):
            j=j+1

res = sum(results)
print(res)