'''Arcade of Time: Store Check'''
def main():
    '''What'''
    num,check = map(int ,input().split())
    open_time = []
    close_time = []
    sum_total = []
    for _ in range(num):
        a,b = map(int ,input().split())
        open_time.append(a)
        close_time.append(b)
    x = input()
    time = [int(t) for t in x.split()]
    for i in range(check):
        count = 0
        for j in range(num):
            if open_time[j] <= time[i] < close_time[j]:
                count += 1
        sum_total.append(count)
    print(*sum_total)
main()
