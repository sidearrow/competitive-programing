S = input()
a = int(S[:2])
b = int(S[2:])

def isMM(num):
    return 1 <= num <= 12 

if isMM(a):
    if isMM(b):
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if isMM(b):
        print('YYMM')
    else:
        print('NA')
