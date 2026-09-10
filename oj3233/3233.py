'''สลากกินแบ่ง'''
def main():
    '''PEP8.EXE'''
    lottery = input()
    lottery_buy = input()
    if lottery == lottery_buy:
        print(1000000)
    elif lottery[2:7] == lottery_buy[2:7]:
        print(100000)
    elif lottery[4:7] == lottery_buy[4:7] and lottery_buy[0] == lottery[0]:
        print(2000)
    elif lottery[5:7] == lottery_buy[5:7] and lottery_buy[0] == lottery[0]:
        print(1000)
    elif lottery[4:7] == lottery_buy[4:7]:
        print(200)
    elif lottery[5:7] == lottery_buy[5:7]:
        print(100)
    elif lottery_buy[0] == lottery[0]:
        print(20)
    else:
        print(0)
main()
