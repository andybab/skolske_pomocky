import random
import builtins

num_exams = 100
max_num = 20
exam_num = 1

with open("priklady.csv", mode='w') as f:
  i = 0
  for x in range(num_exams):
    first_number = random.randint(0,max_num)
    operationAdd = bool(random.getrandbits(1))
  
    (next_top, base_str) = (max_num - first_number, "|{:2d}.|    {:2d} + {:2d} = ") if operationAdd else (first_number, "|{:2d}.|    {:2d} - {:2d} = ")
    second_number = random.randint(0,next_top)
    question_str = base_str.format(exam_num, first_number, second_number)
    f.write(question_str)
    if i % 2 == 0:
      f.write(',')
    else:
      f.write('\n')
    i = i+1
    exam_num += 1