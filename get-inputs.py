# integer value
n = int(raw_input().strip())

# set of integer values which is typed in different lines
grades = []
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)

# string 2-inputs as a,b
m, n = raw_input().strip().split(' ')

# get inputs to list as integers
apple = map(int, raw_input().strip().split(' '))
