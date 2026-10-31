'''FullyPair'''
text = input()
count_text = {}
for i in text:
    count_text[i] = count_text.get(i,0) + 1
answer = ""
for letter, amount in count_text.items():
    if amount % 2:
        answer += letter
print(answer if answer else "fully paired")
