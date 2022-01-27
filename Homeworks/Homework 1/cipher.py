matrix = [
    "T", "U", "E", "S", "A",
    "B", "C", "D", "F", "G",
    "H", "I", "K", "L", "M",
    "N", "O", "P", "Q", "R",
    "V", "W", "X", "Y", "Z"
]

string = input("Enter word to encrypt: ")
temp = string.upper()
size = len(temp) 
result = ""

if(size % 2 == 1):
	temp += "X"
	temp = temp.replace("J", "I")

for i in range(0, size, 2):
	copy = matrix.index(temp[i])
	copy2 = matrix.index(temp[i+1])

	if(copy % 5 == copy2 % 5):
		if (copy+5) // 5 < 5:
			result += matrix[copy+5] 
		else:
			 matrix[copy % 5]
		if (copy2+5) // 5  < 5:
			result += matrix[copy2+5] 
		else:
			 matrix[copy2 % 5]

	elif(copy // 5  == copy2 // 5):
		if ((copy+1) % 5 > copy % 5):
			result += matrix[copy+1] 
		else:
			 matrix[copy - (copy % 5)]
		if ((copy2+1) % 5 > copy2 % 5):
			result += matrix[copy2+1]  
		else:
			matrix[copy2 - (copy2 % 5)]
	else:
		if(copy2 % 5 < copy % 5):
			result += matrix[copy - (copy % 5 - copy2 % 5)]
			result += matrix[copy2 + (copy % 5 - copy2 % 5)]
		else:
			result += matrix[copy + (copy2 % 5 - copy % 5)]
			result += matrix[copy2 - (copy2 % 5 - copy % 5)]

	result += " "

print(result)