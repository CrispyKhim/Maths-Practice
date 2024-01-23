# Program created on 07.06.23
# Created by Christopher Khim
# Modules for Problem #3: Maths Practice

# Import Python libraries and external files
from time import *
from timeit import default_timer as timer
import random as rand
import dictionary as dict

def mode(): # User selects a game mode
   global mode
   mode = input("""\nSelect your game mode:
   1 - Predefined questions
   2 - Random questions
   3 - True/False
Please enter either one of these numbers above (1-3): """)
   match mode:
      case '1':
         print("\nPredefined Questions Mode Selected!")
         predefined_questions()
      case '2':
         print("\nRandomized Questions Mode Selected!")
         rand_questions()
      case '3':
         print("\nTrue/False Questions Mode Selected!")
         true_false()
      case other:
         print("\nInvalid entry")

def begin(): # Executed at the start of each game mode
   global correct, count, guess, final_total_time, rand_answer, is_correct, word
   # INITIALISATION
   correct = 0 # Correct is the number of times the user correctly answers the questions. 
   count = 0 # Count is the number of how many questions have been completed. 
   guess = '' # Variable guess is the user's answer to a question.
   final_total_time = 0 # Variable final_total_time has the sum of the time taken and will be outputted in the end.
   rand_answer = 0
   is_correct = 0
   word = ''

   if mode == '1':
      lesson() # Call the lesson module - Predefined Questions Exclusive
      operation() # Call the operation module
      countdown() # Call the countdown module
   else:
      difficulty() # Call the difficulty module
      operation() # Call the operation module
      countdown() # Call the countdown module

def countdown(): # Counting down from 3 before user starts
   print("Get ready!")
   sleep(1)
   for countdown in range(3, 0, -1):
      print(countdown)
      sleep(1)
   print("Start!")
   sleep(1)

def operation(): # User chooses their operation
   global operator
   operator = input("""\nChoose the operation:
   1 - Addition
   2 - Subtraction
Please select the following function number (1-2): """)

def difficulty(): # For random and true/false game mode
   global questions, scale
   level = ''
   while True:
      level = input("""\nSelect a difficulty level:
   1 - Easy          (10 questions, 0-10 range)
   2 - Intermediate  (20 questions, 0-30 range)
   3 - Hard          (50 questions, 0-100 range)
   4 - Expert        (100 questions, 0-500 range)
   5 - Custom        (Your Choice)
Please enter your choice (1-5): """)
      if level == '1':
         questions = 10
         scale = 10
         break
      elif level == '2':
         questions = 20
         scale = 30
         break
      elif level == '3':
         questions = 50
         scale = 100
         break
      elif level == '4':
         questions == 100
         scale = 500
         break
      elif level == '5':
         questions = int(input("How many questions do you want to play? "))
         scale = int(input("What range do you want to play in? "))
         break
      else:
         print("Invalid option.")

def lesson(): # Only for predefined questions game mode
   global questions, level
   level = ''
   while True:
      level = input("""\nSelect a lesson:
   1 - Lesson 1   (Basic Addition & Subtraction with number lines)
   2 - Lesson 2   (Addition & Subtraction with 'carry-over method')
Please enter your choice (1-2): """)
      if level == '1':
         questions = 10
         break
      elif level == '2':
         questions = 10
         break
      else:
         print("Invalid option.")

def game_over(): # Check if the game is over
   global guess, questions, final_total_time
   if count == questions: # Checks if the user has answered the total number of questions
         print("\nCongratulations! You have completed", questions, "sets of questions!")
         if correct == questions:
            print("Great job! All", questions,"were answered correctly.")
         else:
            print("You got", correct, "out of", questions, "correct answers!")
         print("Your total time was", final_total_time, "seconds.")
         input('')

def check_answer(): # Check if user correctly or incorrectly answered the question
   global guess, count, correct, mode, word
   if guess == str(rand_answer) and mode == '2': # User guessed correct answer in random game mode
      print("Correct!")
      count += 1
      correct += 1
      input("Next? ")
   elif guess != str(rand_answer) and mode == '2': # Checks if user has incorrectly answered the question in random mode
      print("Incorrect. The correct answer was", rand_answer)
      count += 1
      input("Next? ")
   elif word == 'true' and bool(is_correct == true_false_answer) and mode == '3': # User guessed correct answer in true/false game mode
      print("Correct!")
      count += 1
      correct += 1
      input("Next? ")
   elif word == 'false' and bool(is_correct != true_false_answer) and mode == '3': # User guessed correct answer in true/false game mode
      print("Correct!")
      count += 1
      correct += 1
      input("Next? ")
   elif word == 'true' and bool(is_correct != true_false_answer) and mode == '3': # Checks if user has incorrectly answered the question in true/false mode
      print("Incorrect. The correct answer was", str(is_correct))
      count += 1
      input("Next? ")
   elif word == 'false' and bool(is_correct == true_false_answer) and mode =='3': # Checks if user has incorrectly answered the question in true/false mode
      print("Incorrect. The correct answer was", str(is_correct))
      count += 1
      input("Next? ")
   else: # If the user enters an unexpected value
      print("Invalid option.")
      count += 1
      input("Next? ")

def total(): # Calculates the total time taken
   global end, start, final_total_time
   total_time = int(end) - int(start)
   final_total_time = final_total_time + total_time

def predefined_questions():
   begin()

   while count != questions:
      predefined_sum()

def predefined_sum():
   global start, guess, end, count, correct
   while operator == '1': # Only for when operator is addition
      if level == '1': # If the user wants to play lesson 1
         for quiz in dict.lesson_1_add:
            start = timer()
            guess = input("What is " + quiz + " ? ") # Output the question
            end = timer()
            total()
            print(dict.lesson_1_add[quiz]) # Feedback
            if count == questions: # If user answered all the questions
               break
            elif guess == dict.lesson_1_add_answer[count]: # If user correctly answered the question
               print("You have correctly answered the question!")
               count += 1
               correct += 1
            else: # If user incorrectly answered the question
               count += 1
            input("Next? ")
         print("Congratulations! You have completed lesson 2 of addition! Make sure to revise on the content!")
         print("You got", correct, "out of", questions, "correct answers!")
         print("Your total time was", final_total_time, "seconds.")
         input('')
         break
      elif level == '2': # If the user wants to play lesson 1
         for quiz in dict.lesson_2_add:
            start = timer()
            guess = input("What is " + quiz + " ? ") # Output the question
            end = timer()
            total()
            print(dict.lesson_2_add[quiz]) # Feedback
            if count == questions: # If user answered all the questions
               break
            elif guess == dict.lesson_2_add_answer[count]: # If user correctly answered the question
               print("You have correctly answered the question!")
               count += 1
               correct += 1
            else: # If user incorrectly answered the question
               count += 1
            input("Next? ")
         print("Congratulations! You have completed lesson 2 of addition! Make sure to revise on the content!")
         print("You got", correct, "out of", questions, "correct answers!")
         print("Your total time was", final_total_time, "seconds.")
         input('')
         break
      else:
         print("Error. An invalid option has been entered.")
   while operator == '2': # Only for when operator is subtraction
      if level == '1': # If the user wants to play lesson 1
         for quiz in dict.lesson_1_sub:
            start = timer()
            guess = input("What is " + quiz + " ? ") # Output the question
            end = timer()
            total()
            print(dict.lesson_1_sub[quiz]) # Feedback
            if count == questions: # If user answered all the questions
               break
            elif guess == dict.lesson_1_sub_answer[count]: # If user correctly answered the question
               print("You have correctly answered the question!")
               count += 1
               correct += 1
            else: # If user incorrectly answered the question
               count += 1
            input("Next? ")
         print("Congratulations! You have completed lesson 2 of addition! Make sure to revise on the content!")
         print("You got", correct, "out of", questions, "correct answers!")
         print("Your total time was", final_total_time, "seconds.")
         input('')
         break
      elif level == '2': # If the user wants to play lesson 1
         for quiz in dict.lesson_2_sub:
            start = timer()
            guess = input("What is " + quiz + " ? ") # Output the question
            end = timer()
            total()
            print(dict.lesson_2_sub[quiz]) # Feedback
            if count == questions: # If user answered all the questions
               break
            elif guess == dict.lesson_2_sub_answer[count]: # If user correctly answered the question
               print("You have correctly answered the question!")
               count += 1
               correct += 1
            else: # If user incorrectly answered the question
               count += 1
            input("Next? ")
         print("Congratulations! You have completed lesson 2 of addition! Make sure to revise on the content!")
         print("You got", correct, "out of", questions, "correct answers!")
         print("Your total time was", final_total_time, "seconds.")
         input('')
         break
      else:
         print("Error. An invalid option has been entered.")

def rand_questions(): # Extension game mode
   global first_number, second_number
   begin()

   while count != questions:
      # Begins the process of getting a random integer for first and second number
      first_number = rand.randint(0, scale)
      second_number = rand.randint(0, scale)
      
      rand_sum()

      check_answer()
      game_over()

def rand_sum(): # Extension game mode
   global rand_answer, start, guess, end, first_number, second_number
   # Gets an operator from the the operation module
   if operator == '1': # If the operator is addition, sum first and second number
      rand_answer = first_number + second_number
      start = timer()
      guess = input("What is " + str(first_number) + " + " + str(second_number) + " ? ")
      end = timer()
      total()
   elif operator == '2': # If the operator is subtraction, minus first and second number
      rand_answer = first_number - second_number
      start = timer()
      guess = input("What is " + str(first_number) + " - " + str(second_number) + " ? ")
      end = timer()
      total()

def true_false(): # Extension game mode
   global first_number, second_number
   begin()

   while count != questions:
      # Begins the process of getting a random integer for first and second number
      first_number = rand.randint(0, scale)
      second_number = rand.randint(0, scale)
      
      true_false_sum()

      check_answer()
      game_over()

def true_false_sum(): # Extension game mode
   global true_false_answer, start, word, end, first_number, second_number, is_correct
   # Gets an operator from the the operation module
   if operator == '1': # If the operator is addition, sum first and second number
      is_correct = first_number + second_number
      answer_list = [is_correct, rand.choice(range(0, questions))]
      true_false_answer = rand.choice(answer_list)
      start = timer()
      word = input("Is " + str(first_number) + " + " + str(second_number) + " = " + str(true_false_answer) + " ? ")
      end = timer()
      total()
   elif operator == '2': # If the operator is subtraction, minus first and second number
      is_correct = first_number - second_number
      answer_list = [is_correct, rand.choice(range(0, questions))]
      true_false_answer = rand.choice(answer_list)
      start = timer()
      word = input("Is " + str(first_number) + " - " + str(second_number) + " = " + str(true_false_answer) + " ? ")
      end = timer()
      total()
