a = "//[***]\n1***22***33"

def String_to_array(str):
    arr = []
    for i in range(len(str)):
        a = str[i]
        if str[i] == '\n':
            continue
        if str[i].isdigit():
            if i+1 <= len(str)-1 and str[i+1].isdigit():
                arr.append(str[i:i+2])
                i = i+1
            else:
                arr.append(str[i])
    print(arr)


String_to_array(a)

print('*'.isdigit())
