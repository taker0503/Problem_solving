from itertools import permutations
N = int(input())
A = list(map(int, input().split()))
plus , minus, multiply , divide = map(int,input().split())
sign_num_list = [plus , minus, multiply , divide]
sign_list =['+','-','*','/']
sign_result = []
result = 0
result_list = []

def calculate(eval_list):
    global result
    count = 0
    for i in eval_list:
        if i in sign_list:
            count += 1
    if count == 1:
        result = eval(''.join(eval_list))
    else:
        if eval_list[1] == '/':
            a = int(int(eval_list[0]) / int(eval_list[2]))
            new_str = [str(a)] + eval_list[3:]
        else:
            string = ''.join(eval_list[:3])
            a = eval(string)
            new_str = [str(a)] + eval_list[3:]
        calculate(new_str)
    return result

for i in range(4):
    for _ in range(sign_num_list[i]):
        sign_result.append(sign_list[i])
sign_permutations = list(permutations(sign_result))

for i in sign_permutations:
    eval_str = []
    for idx in range(len(A)):
        if idx != 0:
             eval_str.append(i[idx-1])
             eval_str.append(str(A[idx]))
        else:
            eval_str.append(str(A[idx]))

    result = int(calculate(eval_str))
    result_list.append(result)
minimum = min(result_list)
maximum = max(result_list)
print(minimum, maximum)

