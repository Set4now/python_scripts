userinput = raw_input('Please enter numbers between 1 to 10 seperated by space: ')
num = userinput.split()

for a in num:
    if not a.isdigit():
       print 'Please enter a number', a
    elif int(a) < 1:
       print 'Number is less then 1', a
    elif int(a) > 10:
       print 'Number is greater then 10', a
    else:
       print 'Number is vaild', a
