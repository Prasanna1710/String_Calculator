# at Initial commit of code

def add(num_str):
  # code for test case 3
  sum = 0
  for i in range(len(arr)):
    if arr[i].isdigit():
      sum += int(arr[i])
    elif arr[i].islower():
      sum += (ord(arr[i])-96)
    elif arr[i].isupper():
      raise Exception('Only lowercase alphabets allowed')
