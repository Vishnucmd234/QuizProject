import random


questions = [
    
    
    

#Indian History Quiz Questions     
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



#Indian Polity Quiz Questions
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
        "options": ["Prime Minister", "Chief Minister", "President", "Home Minister"],
        "answer": "President"
    },

#Sports Quiz Questions
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
        "question": "Which sport is Michael Jordan famous for?",
        "options": ["Cricket", "Basketball", "Baseball", "Athletics"],
        "answer": "Basketball"
    },
#Economics Quiz Questions

   
    {
        "question": "Which market structure features a single seller?",
        "options": ["Perfect Competition", "Monopoly", "Oligopoly", "Monopolistic Competition"],
        "answer": "Monopoly"
    },
    {
        "question": "What is the term for the cost of the next best alternative that is given up?",
        "options": ["Opportunity Cost", "Fixed Cost", "Marginal Cost", "Average Cost"],
        "answer": "Opportunity Cost"
    },
    #Math Quiz Questions

{
    "question": "3, 9, 27, 81, ?",
    "options": ["243", "162", "324", "200"],
    "answer": "243"
},

{
    "question": "7, 14, 28, 56, ?",
    "options": ["84", "100", "112", "128"],
    "answer": "112"
},
{
    "question": "11, 13, 17, 19, 23, ?",
    "options": ["25", "27", "29", "31"],
    "answer": "29"
},
{
    "question": "8, 16, 24, 32, ?",
    "options": ["36", "40", "44", "48"],
    "answer": "40"
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
        if score == 0:
            print("pad liya kr bhai.... kiu maa baap ke pese duba rha he. kahi jakar pani puri ka thela khod de ya jakar majduri kr. Gr me 2 passa to layega.")

        break
    elif choice == "2":
        print("\nStarting next set of questions...\n")
        continue
    else:
        print("\nInvalid choice! Exiting game.\n")
        print(f"Your current score is: {score}/{total_attempted}\n")
        if score == 0:
            print("bhai tu thik se choice bhi nhi kr sakta to kya hi score krega. time pr majduri pr chalaja kiu maa baap ka pesa barbad kr rha he")
        
        break

print("Thanks for playing!")
