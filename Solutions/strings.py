def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
"""""""""""""""""""""""""""""""""
def count_substring(string, sub_str):
    counter = 0
    for i in range(0, len(string)-2):
        if string[i:len(sub_str)+i] == sub_str:
            counter+=1
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
