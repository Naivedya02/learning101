# Enter your code here. Read input from STDIN. Print output to STDOUT
(n, m) = (input().split())
N = int(n)
M = int(m)
p = ".|."
h = "-"
for i in range((N-1)//2):
    print(h*((M-6*i-3)//2) + p*(2*i+1) + h*((M-6*i-3)//2))
print(h*((M-7)//2) + "WELCOME" + h*((M-7)//2))
for i in range((N-1)//2):
    j = (N-1)//2 - i - 1
    print(h*((M-6*j-3)//2) + p*(2*j+1) + h*((M-6*j-3)//2))

