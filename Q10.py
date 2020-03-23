
if __name__ == '__main__':
    c=0
    n = int(input())
    arr = []
    for t in range(0,n):
        name = input()
        score = float(input())
        arr.append([name,score])
        
    minscore=10000
    minscore2=10000
    #print(arr)
    for i in range(n+1):
        if i is n:
            if arr[i-1][1]<minscore2 and arr[i-1][1]>minscore:
                minscore2 = arr[i-1][1]
        elif arr[i][1]<minscore:
                minscore = arr[i][1]
                if i==0:
                    continue
        if arr[i-1][1]<minscore2 and arr[i-1][1]>minscore:
                minscore2 = arr[i-1][1]
    aw = []
    for j in range(n):
        if arr[j][1]==minscore2:
            aw.append(arr[j][0])
            c+=1
    for t in range(c):
        for f in range(c-1):
            if aw[f+1]<aw[f]:
                temp = aw[f]
                aw[f] = aw[f+1]
                aw[f+1] = temp 
    for g in range(c):
        print(aw[g])    













