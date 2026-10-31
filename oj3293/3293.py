'''BigFrame'''
def main():
    '''main'''
    text_list = []
    for _ in range(5):
        text = input().strip()
        text_list.append(text)
    most = max(len(text_list[0]),len(text_list[1]),len(text_list[2])
               ,len(text_list[3]),len(text_list[4]))
    print("*" * (most+4))
    for i in range(5):
        print(f"* {text_list[i].ljust(most)} *")
    print("*" * (most+4))

main()
