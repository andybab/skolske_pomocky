import random

answers = []

num_exams = int(input("Počet príkladov "))
exam_num = 1
for x in range(num_exams):
  operationAdd = bool(random.getrandbits(1))

  result_should_be = random.randint(11,18)   if operationAdd else random.randint(2,9)
  first_number = random.randint(result_should_be - 9, 9) if operationAdd else random.randint(11, 9 + result_should_be)  
  second_number = result_should_be - first_number if operationAdd else first_number - result_should_be

  base_str = "|{:2d}.|    {:2d} + {:2d} = " if operationAdd else "|{:2d}.|    {:2d} - {:2d} = "

  question_str = base_str.format(exam_num, first_number, second_number)
  student_response = 0
  while True:
    try:
      student_response = int(input(question_str))
      if student_response != result_should_be:
        print("Nesprávne!")
      else: 
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
  
