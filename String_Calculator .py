# at Initial commit of code

def add(num_str):
  Sum = 0
  flag = 0
  negative_nums = ''
  for i in range(len(num_str)):
    if num_str[i].isdigit():
      Sum += int(num_str[i])
    elif num_str[i].islower():
      Sum += (ord(num_str[i]) - 96)
    elif num_str[i].isupper():
      raise Exception('Only lowercase alphabets allowed')
    elif int(num_str[i]) < 0:
      flag = 1
      negative_nums += num_str[i] + ' '
  if flag == 1:
    # in test case 4 we are already taking note of negative number and showing it in message here we are taking all negative numbers and showing them
      raise Exception('Negative numbers not allowed, negative numbers are' + negative_nums)
  return Sum
