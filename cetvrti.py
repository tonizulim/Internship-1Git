
def print_star(num):
    for i in range(num):
        print('*', end="")
    print("")

def print_space(num):
    for i in range(num):
        print(' ', end="")



num=int(input("Unesi broj:"))
space=num-1


for i in range(1,num,2):
    print_space(int(space/2)-int(i/2))
    print_star(i)

if num % 2 == 0: 
    num = num - 1

for i in range(num, 0, -2):
    print_space(int(space/2)-int(i/2))
    print_star(i)

