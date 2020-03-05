s1 = [12,45,78,32]
s2 = [44,23,12,44]
s3 = []
x=0
if len(s1)==len(s2):
    for ss1 in s1:
        sss = (ss1+s2[x])/2
        s3.append(str(sss))
    x=x+1
print(s3)

#moyenne