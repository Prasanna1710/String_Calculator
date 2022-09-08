# at Initial commit of code

# Taking comma Seperated inputs
num = input("enter comma seperated inputs:")
num = list(map(str,num.split(',')))


def addString(num_str):
  if num_str == '':
    return 0
  elif num_str.isdigit():
    return int(num_str)
  else:
    sum = 0
    delimiter = ","  
              
    if num_str.find('\n') != -1 and num_str.find(',') != -1:
      numList = []
      str1 = num_str.split('\n')   
      for s in str1:
        if "," in s:
          x = s.split(',')
            for i in x:
              numList.append(int(i))
        else:
          numList.append(int(s))
            
          return add(numList)
        
    elif num_str.find('\n') != -1:
      delimiter = '\n'    
        
    numbers = num_str.split(delimiter)
    return addNumbers(numbers)
  
  
  
  
  
#  Add numbers function
def add(num_str):
  sum = 0
  flag = 0
  negative_nums = ''
  for i in range(len(num_str)):
    if num_str[i].isdigit():
      if int(num_str[i]) > 1000:
        continue
      else:
        sum += int(num_str[i])
    elif num_str[i].islower():
      sum += (ord(num_str[i]) - 96)
    elif num_str[i].isupper():
      raise Exception('Only lowercase alphabets allowed')
    elif int(num_str[i]) < 0:
      flag = 1
      negative_nums += num_str[i] + ' '
  if flag == 1:
    raise Exception('Negative numbers not allowed, negative numbers are' + negative_nums)
  return sum

  
  
  
if __name__ == '__main__':
  pass
  
