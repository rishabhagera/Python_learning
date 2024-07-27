total_over=2
valid_over=6
wide=1
no_ball=1
one_run=1
two_run=1
four=4
six=6
over_run=0
while(True):
    input_ball=input("your over input")
    for i in range(6):
        input_ball=input("your over input")
        if input_ball == 6:
            over_run+=6
        elif input_ball == four:
            over_run+=4
        elif input_ball == one_run:
            over_run+=1
        elif input_ball == two_run:
            over_run+=2
        else:
            print("wrong input")
    print(over_run)
else:
    print("Wrong inputs")