def get_num(num):
  return int(raw_input("Please enter a number: "))


my_num=get_num("num")
for i in range(2, my_num):
	if my_num % i == 0:
  		print str(my_num) + " is not a prime number"
                break
	else:
  		print str(my_num) + " is  a prime number"
