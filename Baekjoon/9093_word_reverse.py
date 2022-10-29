import sys
N = int(sys.stdin.readline())
for i in range(N):
    list_sentence = list(map(str, sys.stdin.readline().split()))
    word_list = []
    for j in list_sentence:
        word_list.append(j[::-1])
    print(' '.join(word_list))  