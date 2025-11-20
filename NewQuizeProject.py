import random
import time
import threading
import sys

# --- DEMO KE LIYE QUESTIONS GENERATE KAR RAHA HU ---
# Taki aapke paas 10 se jyada questions hon aur aap feature test kar sakein
questions = [

 {
        "question": "Which country invented paper?",
        "options": ["India", "America", "China", "Japan"],
        "answer": "China"
    },

     {
        "question": "Who was the first Mughal Emperor of India?",
        "options": ["Akbar", "Babur", "Shah Jahan", "Humayun"],
        "answer": "Babur"
    },
    {
        "question": "In which year did India get independence?",
        "options": ["1945", "1946", "1947", "1950"],
        "answer": "1947"
    },
    {
        "question": "Who is known as the 'Father of the Nation' in India?",
        "options": ["Subhash Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Bhagat Singh"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "Who built the Taj Mahal?",
        "options": ["Akbar", "Shah Jahan", "Aurangzeb", "Jahangir"],
        "answer": "Shah Jahan"
    },
    {
        "question": "Harappa Civilization is also known as?",
        "options": ["Indus Valley Civilization", "Egyptian Civilization", "Mesopotamian Civilization", "Chinese Civilization"],
        "answer": "Indus Valley Civilization"
    },
    {
        "question": "Who is known as the 'Architect of the Indian Constitution'?",
        "options": ["Jawaharlal Nehru", "B. R. Ambedkar", "Rajendra Prasad", "Sardar Patel"],
        "answer": "B. R. Ambedkar"
    },
    {
        "question": "How many fundamental rights are there in the Indian Constitution?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Who is the head of the Indian State?",
        "options": ["Prime Minister", "Chief Minister", "Home Minister", "President"],
        "answer": "President"
    },
    {
        "question": "Which country has won the most FIFA World Cups?",
        "options": ["Germany", "Italy", "Brazil", "Argentina"],
        "answer": "Brazil"
    },
    
    {
        "question": "Who holds the record for the most goals in international football?",
        "options": ["Pelé", "Lionel Messi", "Cristiano Ronaldo", "Neymar"],
        "answer": "Cristiano Ronaldo"
    },
    {
        "question": "Which country won the ICC Cricket World Cup 2011?",
        "options": ["Sri Lanka", "India", "Australia", "England"],
        "answer": "India"
    },   
    {
        "question": "Which market structure features a single seller?",
        "options": ["Perfect Competition", "Monopoly", "Oligopoly", "Monopolistic Competition"],
        "answer": "Monopoly"
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["Seoul", "Tokyo", "Beijing", "Bangkok"],
        "answer": "Tokyo"
    },
     {
        "question": "What color is the sky on a clear day?",
        "options": ["Blue", "Green", "Red", "Yellow"],
        "answer": "Blue"
    },
    {
        "question": "How many legs does a spider have?",
        "options": ["6", "8", "4", "10"],
        "answer": "8"
    },
    {
        "question": "Which animal says 'Moo'?",
        "options": ["Dog", "Cow", "Cat", "Sheep"],
        "answer": "Cow"
    },
      {
        "question": "Which color do you get by mixing red and white?",
        "options": ["Pink", "Purple", "Orange", "Brown"],
        "answer": "Pink"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Earth", "Mercury", "Mars", "Venus"],
        "answer": "Mercury"
    },

    {
        "question": "What is the term for the cost of the next best alternative that is given up?",
        "options": ["Opportunity Cost", "Fixed Cost", "Marginal Cost", "Average Cost"],
        "answer": "Opportunity Cost"
    },
    {
    "question": "3, 9, 27, 81, ?",
    "options": ["243", "162", "324", "200"],
    "answer": "243"
     }





]

score = 0
total_attempted = 0
total_seconds_taken = 0 

# Questions shuffle karein
random.shuffle(questions)

def timer_display(start_time, stop_event):
    while not stop_event.is_set():
        elapsed = int(time.time() - start_time)
        sys.stdout.write(f"\rTime elapsed: {elapsed} sec  |  Enter your option number: ")
        sys.stdout.flush()
        stop_event.wait(1)

print("********** Welcome to Random Quiz Game **********\n")

# Loop start
for q_number, q in enumerate(questions, start=1):
    print(f"Question {q_number}: {q['question']}")
    for idx, opt in enumerate(q["options"], start=1):
        print(f"{idx}. {opt}")

    print() 

    start_time = time.time()
    stop_event = threading.Event()
    t = threading.Thread(target=timer_display, args=(start_time, stop_event))
    t.start()

    try:
        user_ans = input("") 
    except:
        user_ans = ""

    end_time = time.time()
    stop_event.set()
    t.join()

    time_taken_for_question = int(end_time - start_time)
    total_seconds_taken += time_taken_for_question

    total_attempted += 1
    print() 

    try:
        user_ans = int(user_ans)
        if q["options"][user_ans - 1] == q["answer"]:
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"✘ Wrong! Correct answer: {q['answer']}\n")
    except (ValueError, IndexError):
        print(f"✘ Invalid input! Correct answer: {q['answer']}\n")

    # --- NAYA FEATURE: Har 10 Question ke baad check ---
    # Check karein agar question number 10 ka multiple hai (10, 20, 30...)
    # Aur ye bhi check karein ki ye last question nahi hona chahiye
    if q_number % 10 == 0 and q_number != len(questions):
        print("*************************************************")
        print(f"You have completed {q_number} questions.")
        print("1. Show my score (Exit Game)")
        print("2. Continue solving more questions")
        print("*************************************************")
        
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == '1':
                # Loop tod do, seedha neeche score print hoga
                break 
            elif choice == '2':
                print("\nResuming Quiz...\n")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        
        # Agar user ne 1 chuna tha, toh main 'for' loop ko bhi break karna padega
        if choice == '1':
            break
    # ---------------------------------------------------

# Final Result Calculation
minutes = int(total_seconds_taken // 60)
seconds = int(total_seconds_taken % 60)

print("=====================================")
print(f"Your FINAL SCORE: {score}/{total_attempted}")
print(f"Total Time Taken: {minutes} minutes {seconds} seconds") 
print("=====================================")
print("Thanks for playing!")