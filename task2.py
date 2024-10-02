if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the name of the student: ")
    print("{:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))
    print(sum(student_marks[query_name])/len(student_marks[query_name]))
    print(student_marks[query_name])