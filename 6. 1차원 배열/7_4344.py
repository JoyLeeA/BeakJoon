C = int(input())
for _ in range(C):
    students = list(map(int, input().split()))
    N = students.pop(0)
    avg = sum(students)/N
    cnt = 0
    for student in students:
        if student > avg:
            cnt += 1
    print(f'{(cnt/N)*100:.3f}%')