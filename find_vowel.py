def solution(s):
    s = s.lower()#全部轉小寫
    num = []#定義位置列表
    vowel = ['a' ,'e' ,'i' ,'o' ,'u']
    for v in vowel:
        while v in s:#當S含有當次搜尋之母音
            num.append(s.find(v))#將該母音位置加入nums
            s = s.replace(v ,'，' ,1)#將該母音以'，'替代
    num.sort()#排序
    return num
