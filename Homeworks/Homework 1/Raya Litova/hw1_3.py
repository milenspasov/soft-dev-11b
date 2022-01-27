alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ" #without J
arr=""
keyword = "TUES"
keyword_count=0
alphabet_count=0;
stop=0;
for i in range(5):
    for j in range(5):
        stop=0
        if(keyword_count<len(keyword)):
            while(not stop):
                if(not(keyword[keyword_count] in str(arr))):
                    if(keyword[keyword_count]!="J"):
                        arr+=(keyword[keyword_count])
                        stop=1
                    else:
                        arr+="I"
                        stop=1
            keyword_count+=1
        else:
            while(not stop):
                if(not(alphabet[alphabet_count] in str(arr))):
                    arr+=(alphabet[alphabet_count])
                    stop=1
                alphabet_count+=1
            
message = input("Secret message: ")
result=""
if(len(message)%2!=0):
    message+="X"

i=0  
while(i<(len(message)-1)):
    pair=[]
    pair.append(message[i])
    if(message[i+1]==pair[0]):
        pair.append("X")
        message+="X"
    else:
        i=i+1
        pair.append(message[i])
    pair_index = []
    pair_index.append(int(arr.index(pair[0])))
    pair_index.append(int(arr.index(pair[1])))
    if(int(pair_index[0]/5)==int(pair_index[1]/5)):
        result+=arr[pair_index[0]+1] if (pair_index[0]+1)%5!=0 else arr[pair_index[0]-4]
        result+=arr[pair_index[1]+1] if (pair_index[1]+1)%5!=0 else arr[pair_index[1]-4]
                      
    elif(int(pair_index[0]%5)==int(pair_index[1]%5)):
        result+=arr[pair_index[0]+5] if (pair_index[0]+5)<25 else arr[pair_index[0]-24+pair_index[0]%5]
        result+=arr[pair_index[1]+5] if (pair_index[1]+5)<25 else arr[pair_index[1]-24+pair_index[1]%5]
    else:
        result+=arr[pair_index[0]-(pair_index[0]%5-pair_index[1]%5)] if pair_index[0]%5>pair_index[1]%5 else arr[pair_index[0]+(pair_index[1]%5-pair_index[0]%5)]
        result+=arr[pair_index[1]-(pair_index[1]%5-pair_index[0]%5)] if pair_index[1]%5<pair_index[0]%5 else arr[pair_index[1]+(pair_index[0]%5-pair_index[1]%5)]
    i+=1

print(result)

    

