# at Initial commit of code

# Taking comma Seperated inputs
num = input("enter comma seperated inputs:")
num = list(map(str,num.split(',')))


def addString(num_str):
  if num_str == '':
    return 0
  elif num_str.isdigit():
    return int(num_str)
  

  
  
  
if __name__ == '__main__':
  pass
  
