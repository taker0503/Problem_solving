import sys
word = list(sys.stdin.readline().rstrip())

cnt = 0
left = 0

while cnt < len(word):
    if word[cnt] == '<':
        cnt +=1
        while word[cnt] != '>':
            cnt += 1
        cnt += 1
    elif word[cnt].isalnum():
        left = cnt
        while cnt < len(word) and word[cnt].isalnum():
            cnt += 1
        words = word[left:cnt]
        words.reverse()
        word[left:cnt] = words
    else:
        cnt += 1
print(''.join(word))