import random

answers = []

num_exams = int(input("Počet príkladov "))

exam_num = 1
for x in range(num_exams):
  first_number = random.randint(0,10)
  operationAdd = bool(random.getrandbits(1))
  
  (next_top, base_str) = (10 - first_number, "|{:2d}.|    {:2d} + {:2d} = ") if operationAdd else (first_number, "|{:2d}.|    {:2d} - {:2d} = ")
  second_number = random.randint(0,next_top)

  question_str = base_str.format(exam_num, first_number, second_number)
  student_response = 0
  while True:
    try:
      student_response = int(input(question_str))
      break
    except ValueError:
      print("Ešte raz!")
  
  is_ok = (first_number + second_number) == student_response if operationAdd else (first_number - second_number) == student_response
  answers.append( (question_str + str(student_response), is_ok) )
  exam_num += 1
   
good_cnt = 0
bad_cnt  = 0

print("\n")
print("Výsledok:")

for (que_answ_str, result) in answers:
  if result:
    good_cnt += 1
  else:
    bad_cnt += 1
	
  result_str = "OK  :)" if result else "ZLE :("
  print(que_answ_str + " " + result_str)

print("\n")
print("Dobrých {}, Zlých {}".format(good_cnt, bad_cnt))
  
