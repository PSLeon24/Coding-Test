import sys

input = sys.stdin.readline

# def calc_gpa():

if __name__ == "__main__":
    subjects = []
    scores = []
    grade = []

    gpa = {
        "A+": 4.5,
        "A0": 4.0,
        "B+": 3.5,
        "B0": 3.0,
        "C+": 2.5,
        "C0": 2.0,
        "D+": 1.5,
        "D0": 1.0,
        "F": 0.0,
    }

    total = 0
    cnt = 0

    for _ in range(20):
        classes = list(map(str, input().split()))
        subjects.append(classes[0])
        scores.append(float(classes[1]))
        grade.append(classes[2])

    for i in range(20):
        if grade[i] == "P":
            pass
        else:
            total += scores[i] * gpa[grade[i]]
            cnt += int(scores[i])

    print(f"{(total / cnt):.6f}")
