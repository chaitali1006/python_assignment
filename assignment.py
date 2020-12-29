

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
N = len(ALPHABET)
ALPHABET_INDEX = {d: i for i, d in enumerate(ALPHABET, 1)}


def int_to_column_id(num):
    if num == 0:
        return ""
    else:
        q, r = divmod(num, N)
        return int_to_column_id(q) + ALPHABET[r]

def column_id_to_int(string):
    result = 0
    for char in string.lower():
            result = result * N + ALPHABET_INDEX[char]
    return result - 1

final_result=list()
#First Input: Take input for Number of test cases
test_cases = int(input()) 

for x in range(0,test_cases):
        #Second Input: Take input for length of string
        length_str = int(input())
        #Third Input: Take input for String
        string = str(input())


        n = sum([ column_id_to_int(item) for item in string ])
        if string == 'a':
            final_result.append('a')
        else:
            while n>25:
                string = str(int_to_column_id(n))
                n = sum([ column_id_to_int(item) for item in string ])
            a=int_to_column_id(n)

            final_result.append(a)
        
#Print output on given format
for x in final_result:
    print(x)
