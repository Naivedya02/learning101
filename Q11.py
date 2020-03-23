if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=0
    new_list = student_marks.get(query_name, 0)
    for i in range(len(new_list)):
        total += student_marks[query_name][i]
    average = (total/len(new_list))
    print('%.2f' %average)
