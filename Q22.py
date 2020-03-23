def print_formatted(number):
    l = len(format(n,'b'))
    for i in range(1,n+1):
        print("%s %s %s %s" %(str(i).rjust(l),format(i,'o').rjust(l),format(i,'X').rjust(l),format(i, 'b').rjust(l)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

