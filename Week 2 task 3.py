def procedure_2(inp_1num,inp_2num,inp_sum):
    FirstN = inp_1num
    SecNum = inp_2num
    FinalNum = inp_sum
    if FinalNum == "A" :
        print(FirstN+SecNum)
    elif FinalNum == "B" :
        print(FirstN-SecNum)
    elif FinalNum == "C" :
        print(FirstN/SecNum)
    elif FinalNum == "D" :
        print(FirstN*SecNum)

FirstN = int(input("What is your first number?"))
SecNum = int(input("What is your second number?"))
FinalNum = input("Enter A to add, B to subtract, C to divide, D to multiply")
procedure_2(FirstN,SecNum,FinalNum)
