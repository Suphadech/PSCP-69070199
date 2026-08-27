'''BrickBridge'''
def main():
    '''what is this'''
    a = int(input())
    b = int(input())
    goal = int(input())
    use_b = min(b,goal//5)
    remain = goal - (use_b*5)
    if remain <= a:
        print(remain)
    else:
        print(-1)

main()
