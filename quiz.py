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
        "question": "Who was the first President of India?",
        "options": ["Jawaharlal Nehru", "Rajendra Prasad", "Sardar Patel", "Lal Bahadur Shastri"],
        "answer": "Rajendra Prasad"
    },
    {
        "question": "The Battle of Plassey was fought in which year?",
        "options": ["1757", "1764", "1782", "1799"],
        "answer": "1757"
    },
    {
        "question": "Who founded the Maurya Empire?",
        "options": ["Ashoka", "Bindusara", "Chandragupta Maurya", "Bimbisara"],
        "answer": "Chandragupta Maurya"
    },
    {
        "question": "Who discovered the sea route to India?",
        "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Marco Polo"],
        "answer": "Vasco da Gama"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Indira Gandhi", "Sardar Patel"],
        "answer": "Jawaharlal Nehru"
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
        "question": "Who appoints the Prime Minister of India?",
        "options": ["President", "Chief Justice", "Lok Sabha Speaker", "Rajya Sabha Chairperson"],
        "answer": "President"
    },
    {
        "question": "What is the minimum age to become the President of India?",
        "options": ["25 years", "30 years", "35 years", "40 years"],
        "answer": "35 years"
    },
    {
        "question": "Which article deals with the Right to Equality?",
        "options": ["Article 14", "Article 19", "Article 21", "Article 32"],
        "answer": "Article 14"
    },
    {
        "question": "India has a ______ form of government.",
        "options": ["Monarchy", "Dictatorship", "Parliamentary Democracy", "Presidential System"],
        "answer": "Parliamentary Democracy"
    },
    {
        "question": "In India, the Council of Ministers is headed by?",
        "options": ["President", "Prime Minister", "Chief Justice", "Lok Sabha Speaker"],
        "answer": "Prime Minister"
    },
    {
        "question": "Which is the upper house of the Indian Parliament?",
        "options": ["Lok Sabha", "Vidhan Sabha", "Rajya Sabha", "Zila Parishad"],
        "answer": "Rajya Sabha"
    },
    {
        "question": "How many members are nominated by the President to Rajya Sabha?",
        "options": ["2", "8", "10", "12"],
        "answer": "12"
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
        "question": "Who is known as the 'God of Cricket'?",
        "options": ["Virat Kohli", "Sachin Tendulkar", "MS Dhoni", "Ricky Ponting"],
        "answer": "Sachin Tendulkar"
    },
    {
        "question": "How many players are there in a cricket team?",
        "options": ["9", "10", "11", "12"],
        "answer": "11"
    },
    {
        "question": "Which sport uses the term 'Deuce'?",
        "options": ["Football", "Basketball", "Tennis", "Hockey"],
        "answer": "Tennis"
    },
    {
        "question": "In which country were the first Olympic Games held?",
        "options": ["Italy", "France", "Greece", "USA"],
        "answer": "Greece"
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
        "question": "How many minutes are there in a football match?",
        "options": ["60", "80", "90", "100"],
        "answer": "90"
    },
    {
        "question": "Which athlete is known as the fastest man in the world?",
        "options": ["Usain Bolt", "Carl Lewis", "Tyson Gay", "Yohan Blake"],
        "answer": "Usain Bolt"
    },
    {
        "question": "Which sport is Michael Jordan famous for?",
        "options": ["Cricket", "Basketball", "Baseball", "Athletics"],
        "answer": "Basketball"
    },
#Economics Quiz Questions

    {
        "question": "What is the study of how people use limited resources to satisfy unlimited wants?",
        "options": ["Sociology", "Economics", "Geography", "Psychology"],
        "answer": "Economics"
    },
    {
        "question": "What does GDP stand for?",
        "options": ["Gross Domestic Product", "Government Development Plan", "General Domestic Policy", "Gross Demand Percentage"],
        "answer": "Gross Domestic Product"
    },
    {
        "question": "Which of the following is a 'want' and not a 'need'?",
        "options": ["Food", "Water", "Clothing", "Smartphone"],
        "answer": "Smartphone"
    },
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
    "question": "4, 7, 12, 19, 28, ?",
    "options": ["39", "40", "42", "44"],
    "answer": "40"
},
{
    "question": "2, 5, 10, 17, 26, ?",
    "options": ["35", "38", "40", "42"],
    "answer": "37"
},
{
    "question": "1, 4, 9, 16, 25, ?",
    "options": ["30", "32", "36", "40"],
    "answer": "36"
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


# ---- Add more questions and make list 100 ----


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
