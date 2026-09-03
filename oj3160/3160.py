'''FindPrime'''
def main():
    '''Nigga Prime'''
    first,end = map(int ,input().split())
    prime_list = []
    for i in range(first,end+1):
        if i > 1:
            for j in range(2,i):
                if not i % j:
                    break
            else:
                prime_list.append(i)
    if prime_list:
        print(*prime_list)
    print(f'Total primes: {len(prime_list)}')
main()
