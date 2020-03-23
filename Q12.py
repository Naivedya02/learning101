def insert(arr, i,e):
    arr.insert(i,e)
def printing(arr):
    print(arr)
def remove(arr, a):
    arr.remove(a)
def append(arr, s):
    arr.append(s)
def sort(arr):
    arr.sort()
def pop(arr):
    arr.pop()
def reverse(arr):
    arr.reverse()
if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        nai = list(input().split())
        list1.append(nai)
    plist = []
    for j in range(N):
        if list1[j][0].startswith('insert'):
            insert(plist,int(list1[j][1]),int(list1[j][2]))
        elif list1[j][0].startswith('print'):
            printing(plist)
        elif list1[j][0].startswith('remove'):
            remove(plist, int(list1[j][1]))
        elif list1[j][0].startswith('append'):
            append(plist, int(list1[j][1]))
        elif list1[j][0].startswith('sort'):
            sort(plist)
        elif list1[j][0].startswith('pop'):
            pop(plist)
        elif list1[j][0].startswith('reverse'):
            reverse(plist)

