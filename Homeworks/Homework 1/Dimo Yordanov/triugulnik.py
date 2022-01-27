from typing import List
def get_triugulnik(lines:int)->List[List[int]]:
    return [[int(i) for i in input().split(" ")] for i in range(lines)]

def calculate(a:List[int],b:List[int])->List[int]:
    for i in range(0,len(b)):
        k = [a[i]+b[i],a[i+1]+b[i]]
        b[i] = k[k[0]<k[1]]
    return b
def calculate_line(lister:List[List[int]])->List[int]:
    lister.reverse()
    for i in range(1,len(lister)):
        lister[i-1] = calculate(lister[i-1],lister[i])
    return lister[len(lister)-1]
print(calculate_line(get_triugulnik(int(input("Lines: "))))[0])
