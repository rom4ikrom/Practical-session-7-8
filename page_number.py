def left (a):
    print(a)

def right (a):
    print ("%60s%d" % (" ", a))

b = False
page_number = int(input("Please enter page number: "))
if page_number % 2 == 0:
    b = True
    left(page_number)
else:
    b = False
    right(page_number)





    

