import numpy as np

grade = open('gradeRecord.txt', 'r')
optionGrade = open('optional.txt', 'r')
m = [eval(i) for i in grade]
a = [i[0] for i in m]
b = [i[1] for i in m]

n = [eval(i) for i in optionGrade]

c = [i[0] for i in n]
d = [i[1] for i in n]
compulsoryGrade = np.array(a).dot(np.array(b).transpose()) / sum(b)
optionalGrade = np.array(c).dot(np.array(d).transpose()) * 0.002
total = compulsoryGrade + optionalGrade
optionGrade.close()
grade.close()
print(total)