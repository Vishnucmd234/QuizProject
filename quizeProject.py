import random


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
     },

]

score = 0
total_attempted = 0  
print("********** Welcome to Random Quiz Game **********\n")

# ---- Make a copy so we don't lose original questions ----
available_questions = questions.copy()

while True:

    # If questions finish
    if len(available_questions) == 0:
        print("\nNo more questions available!")
        print(f"Your FINAL SCORE is: {score}/{total_attempted}")
        break

    # ---- Pick 10 random questions ----
    block_size = 10 if len(available_questions) >= 10 else len(available_questions)
    random_questions = random.sample(available_questions, block_size)

    # ---- Ask each question ----
    for i, q in enumerate(random_questions, start=1):
        print(f"Q{i}. {q['question']}")
        
        for idx, opt in enumerate(q["options"], start=1):
            print(f"{idx}. {opt}")
        
        user_ans = input("Enter option number: ")
        total_attempted += 1 

        try:
            user_ans = int(user_ans)
            if q["options"][user_ans - 1] == q["answer"]:
                print("✔ Correct!\n")
                score += 1
            else:
                print(f"✘ Wrong! Correct answer: {q['answer']}\n")
        except:
            print("✘ Invalid input\n")

        # Remove asked question so it doesn't repeat
        available_questions.remove(q)

    # ---- After every 10 questions show menu ----
    print("\n--------------------------------------------")
    print("10 Questions completed!")
    print("What would you like to do next?")
    print("1. Show my score")
    print("2. Continue solving more questions")
    print("--------------------------------------------")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\n=====================================")
        print(f"Your FINAL SCORE is: {score}/{total_attempted}")
        print(f"---------->you win: {score}crore Rs. - {score}crore Rs.")

        print("=====================================\n")
        
        break
    elif choice == "2":
        print("\nStarting next set of questions...\n")
        continue
    else:
        print("\nInvalid choice! Exiting game.\n")
        print(f"Your current score is: {score}/{total_attempted}\n")
       
        break

print("Thanks for playing!")