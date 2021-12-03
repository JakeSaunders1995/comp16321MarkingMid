#rugby
# t=5
# c=2
# p=3
# d=3
# T1&T2
file_path = input('please enter the test file path here ')
f = open( file_path ,'r', encoding='utf-8')
# f = open(r'C:\Users\骁骁\Desktop\midterm_files(1)\midterm_files\Example_inputs\Example_inputs_program1\test_file1.txt')
scores = f.read()
# print(scores)
n = 3
score = [scores[i:i+n] for i in range(0,len(scores),n)]
T1 = []
T2 = []
for each_score in score:
    if each_score.startswith('T1'):
        T1.append(each_score)
    else:
        T2.append(each_score)
# print(T1,T2)
points_t = 5
points_c = 2
points_p = 3
points_d = 3
T1_sum = 0
T2_sum = 0
for i in T1:
    if i.endswith('t'):
        points = points_t
    elif i.endswith('c'):
        points = points_c
    elif i.endswith('p'):
        points = points_p
    else:
        points = points_d
    T1_sum += (points)
print(T1_sum)
for i in T2:
    if i.endswith('t'):
        points = points_t
    elif i.endswith('c'):
        points = points_c
    elif i.endswith('p'):
        points = points_p
    else:
        points = points_d
    T2_sum += (points)
# print(T2_sum)
result = (str(T1_sum) +':' + str(T2_sum))
print(result)
# print(T1_sum, ':' , T2_sum)
output_path = input('please enter the output file path here.')
p = open( output_path ,'w', encoding='utf-8')
p.write(result)
p.close()
