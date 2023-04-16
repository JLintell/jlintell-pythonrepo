import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# Task 4

grades = data.split(",")

grades = [int(x) for x in data.split(",")]

# Task 5

min_grade = min(grades)
print("Minimum grade:", min_grade)

max_grade = max(grades)
print("Maximum grade:", max_grade)


grades = []

for grade in data.split(","):
    grades.append(int(grade))

min_grade = min(grades)
print("Minimum grade:", min_grade)

max_grade = max(grades)
print("Maximum grade:", max_grade)

grades = list(map(int, data.split(",")))

min_grade = min(grades)
print("Minimum grade:", min_grade)

max_grade = max(grades)
print("Maximum grade:", max_grade)

# Task 11

average_grade = sum(grades) / len(grades)
average_grade = round(average_grade, 2)

print("Average grade: ", average_grade)

# Task 13

mean_grade = round(statistics.mean(grades), 2)

print("Mean grade: {}".format(mean_grade))

# Task 14

median_grade = statistics.median(grades)

print("Median grade: {}".format(median_grade))


# Task 15

min_grade = min(grades)
max_grade = max(grades)
average_grade = sum(grades) / len(grades)
mean_grade = statistics.mean(grades)
median_grade = statistics.median(grades)

output = "Minimum grade: {}\nMaximum grade: {}\nAverage grade: {}\nMean grade: {}\nMedian grade: {}"
print(output.format(min_grade, max_grade, average_grade, mean_grade, median_grade))