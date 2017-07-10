def get_num(num):
    return int(raw_input("Please enter a num: "))


my_num=get_num("num")

def get_fact(my_num):
    if my_num == 1:
        return my_num
    else:
        return my_num * get_fact( my_num - 1)


print get_fact(my_num)

