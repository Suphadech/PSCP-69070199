'''Bill'''
def main():
    '''main'''
    cash = int(input())
    service = cash / 10
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    vat = ((cash + service) * 7) / 100
    total = cash + service + vat
    print(f"{total:.2f}")

main()
