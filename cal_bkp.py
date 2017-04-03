#this is to make a calculator

def sum(num1, num2):
    return  num1 + num2

def mul(num1, num2):
    return num1 * num2


def sub(num1, num2):
    return  num1 - num2

def div(num1, num2):
    return  num1 / num2





def main():
    operation = raw_input("What do you want to do (+,-,/,*): ")
    if(operation != '+' and operation != '-' and operation != '/' and operation != '*'):
        #invalid operation
   	print "you must enter a valid operation"
    else:
   	var1 = int(raw_input("Enter the first number: "))
   	var2 = int(raw_input("Enter the Seconf number: "))
   	if(operation == '+'):
           print sum(var1, var2)
   	elif(operation == '-'):
           print (sub(var1, var2))
  	elif(operation == '/'):
           print (div(var1, var2))
   	else:
           print (mul(var1, var2))

main()
  
