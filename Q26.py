def merge_the_tools(string, k):
    m=0
    n = len(string)
    r = n//k
    for i in range(0,r):
        if i == r-1:
            t = string[k*i:]
        else:
            t = string[k*i : k*i + k]
        
        u = t[0]
        p = u
        for j in range(1,k):
            for kh in range(j):
                if t[j]==t[kh]:
                    m+=1
            if m==0:
                u = p + t[j]
                p = u
            m=0
        print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

