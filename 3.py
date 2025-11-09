for i in range(1,11):
    number_of_spaces = 11-i
    for j in range(1,number_of_spaces):
        print(end=' ')
    print(i)

for i in range(1,11):
    number_of_spaces = 11-i
    for j in range(1,number_of_spaces):
        print(end=' ')
    for j in range(1,i):
        print(j,end=' ')
    print()
