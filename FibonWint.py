while True:
    answer_type=input('вы хотите получить[f]полную строку фибоначчи, только[s]единичное число, или[a]среднее значение выбранной части?')

    if answer_type=='f':
        amount=input('Введите, сколько частей последовательности Фибоначчи вы хотите видеть.')

        if int(amount)==1:
            fibonacci=[0]
            print(fibonacci)
        elif int(amount)==0:
            fibonacci=[]
            print(fibonacci)
        elif int(amount)==2:
            fibonacci=[0,1]
            print(fibonacci)
        else:
            fibonacci=[0,1,1]
            for parts in range(1,int(amount)-2):
                addative=fibonacci[-2]+fibonacci[-1]
                fibonacci.append(addative)
            print(fibonacci)

    elif answer_type=='s':
        single_num=input('Какую часть последовательности Фибоначчи вы хотите увидеть')

        if int(single_num)==1:
            fibonacci=0
            print(fibonacci)
        elif int(single_num)==0:
            fibonacci='Nothing'
            print(fibonacci)
        elif int(single_num)==2:
            fibonacci=1
            print(fibonacci)
        else:
            fibonacci=[0,1,1]
            for parts in range(1,int(single_num)-2):
                addative=fibonacci[-2]+fibonacci[-1]
                fibonacci.append(addative)
            print(fibonacci[int(single_num)-1])

    elif answer_type=='a':
        amount=input('Сколько частей последовательности Фибоначчи вы хотите усреднить?')
        if int(amount)==1:
            fibonacci=0
            print(fibonacci)
        elif int(amount)==0:
            fibonacci=[]
            print(fibonacci)
        elif int(amount)==2:
            fibonacci=[0,1]
            average=.5
            print(average)
        else:
            fibonacci=[0,1,1]
            for parts in range(1,int(amount)-2):
                addative=fibonacci[-2]+fibonacci[-1]
                fibonacci.append(addative)
            average=sum(fibonacci)/len(fibonacci)
            print(average)

    else:
        print('Недействительный ввод.')