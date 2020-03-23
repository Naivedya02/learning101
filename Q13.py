if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple()
    for i in range(n):
        t = t + (integer_list[i],)
    print(hash(t))

