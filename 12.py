def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    temp = dividend[0:pick]

    while(pick<len(dividend)):
        if temp[0] == '1':
            temp = xor(temp,divisor)+dividend[pick]
        else:
            temp = xor(temp,'0'*pick)+dividend[pick]
        pick = pick+1

    if temp[0] == '1':
       temp = xor(temp,divisor)
    else:
        temp = xor(temp,'0'*pick)

    return temp

def encodeData(data,div):
    div_len = len(div)
    data_send = data+'0'*(div_len-1)
    remainder = mod2div(data_send,div)
    return data+remainder
    
def decodeData(data,div):
    return mod2div(data,div)

data = input("Enter data : ")
div = input("Enter divisor : ")

encoded_data = encodeData(data, div)
print("Data sent :", encoded_data)

received = input("Enter received data : ")
remainder = decodeData(received, div)

if '1' in remainder:
    print("Error detected.")
else:
    print("No error detected.")
