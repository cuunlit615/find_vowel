
def solution(s):
    s = s.lower()
    num = []
    vowel = ['a' ,'e' ,'i' ,'o' ,'u']
    for v in vowel:
        while v in s:
            num.append(s.find(v))
            s = s.replace(v ,'t' ,1)
    num.sort()
    return num
