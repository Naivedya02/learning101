def print_rangoli(size):
    c="-"
    for i in range (0,n):
        print(c*(2*(n-i-1)), end="")
        for j in range(0, i):
            print(chr(ord('a')+ n-1-j), end="-")
        print(chr(ord('a')+ n-1-i), end="")
        for j in range(0, i):
            print(c+chr(ord('a')+ n-i+j ), end="")
        print(c*(2*n-2*i-2))
    for i in range (0,n-1):
        print(c*(2*(i+1)), end="")
        for j in range(0, n-2-i):
            print(chr(ord('a')+ n-1-j), end="-")
        print(chr(ord('a')+ i+1), end="")
        for j in range(0, n-2-i):
            print(c+chr(ord('a')+ i+2+j ), end="")
        print(c*(2*i + 2))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)























