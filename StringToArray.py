a = "//[***]\n1***22***33"

def String_to_array(str):
    i = 0
    arr = []
    while i < len(str):
        if str[i] == '\n':
            continue
        if str[i].isdigit():
            if i+1 <= len(str)-1 and str[i+1].isdigit():
                arr.append(str[i:i+2])
                i = i + 2
            else:
                arr.append(str[i])
                i += 1
        i += 1
    print(arr)



String_to_array(a)

print('*'.isdigit())
