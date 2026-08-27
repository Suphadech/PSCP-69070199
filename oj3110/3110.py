'''Thunder Express'''
first,last = map(str ,input().split())
weight = float(input())
if first == "BKK" and last == "CNX":
    print(f'{10 + (weight*30):.2f}')
elif first == "CNX" and last == "UBP":
    print(f'{15 + (weight*40):.2f}')
elif first == "UBP" and last == "BKK":
    print(f'{20 + (weight*40):.2f}')
elif first == "BKK" and last == "PKT":
    print(f'{25 + (weight*50):.2f}')
elif first == "PKT" and last == "CNX":
    print(f'{30 + (weight*60):.2f}')
elif first == "UBP" and last == "PKT":
    print(f'{40 + (weight*70):.2f}')
else:
    print("Error")
