while True:  
    num = int(input())
    is_Prime = True

    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                is_Prime=False
    else:
        is_Prime= False

    print(is_Prime)