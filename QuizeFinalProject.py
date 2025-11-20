import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk # <--- Naya Import

# --- Questions Data --- 
questions = [
    {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "Delhi"},
    {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Python is a language?", "options": ["Yes", "No", "Maybe", "None"], "answer": "Yes"},
    {"question": "Sun rises in the?", "options": ["East", "West", "North", "South"], "answer": "East"},
    {"question": "Which gas is most abundant in Earth's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"], "answer": "Nitrogen"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Dickens", "Shakespeare", "Hemingway", "Tolkien"], "answer": "Shakespeare"},
    {"question": "The speed of light is approximately:", "options": ["30,000 km/s", "300,000 km/s", "300 million m/s", "3 million m/s"], "answer": "300 million m/s"},
    {"question": "What is the chemical symbol for gold?", "options": ["Go", "Gd", "Au", "Ag"], "answer": "Au"},
    {"question": "What is the primary source of energy for the Earth?", "options": ["Moon", "Sun", "Geothermal", "Wind"], "answer": "Sun"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "South Korea", "Japan", "Thailand"], "answer": "Japan"},
    {"question": "What geometric shape is generally used for a stop sign?", "options": ["Square", "Triangle", "Octagon", "Hexagon"], "answer": "Octagon"},
    {"question": "What gas do plants release during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Oxygen"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "How many days are there in a leap year?", "options": ["364", "365", "366", "367"], "answer": "366"},
    {"question": "What is the largest mammal on Earth?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Blue Whale"},
    {"question": "Which continent is the Sahara Desert located in?", "options": ["Asia", "Africa", "Australia", "Europe"], "answer": "Africa"},
    {"question": "Which organ pumps blood through the body?", "options": ["Lungs", "Brain", "Heart", "Kidneys"], "answer": "Heart"},
    {"question": "What is the freezing point of water?", "options": ["100°C", "0°C", "50°C", "-10°C"], "answer": "0°C"},
    {"question": "Which animal is known as the King of the Jungle?", "options": ["Tiger", "Lion", "Leopard", "Cheetah"], "answer": "Lion"},
    {"question": "Which planet is closest to the Sun?", "options": ["Earth", "Mars", "Mercury", "Venus"], "answer": "Mercury"}, 
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "HO"], "answer": "H2O"},
    {"question": "Which shape has three sides?", "options": ["Square", "Triangle", "Circle", "Rectangle"], "answer": "Triangle"},
    {"question": "How many colors are in a rainbow?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "What do bees produce?", "options": ["Milk", "Honey", "Wax", "Oil"], "answer": "Honey"},
    {"question": "Which ocean is the largest?", "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "answer": "Pacific Ocean"},

]

# ----------------- Global Variables -----------------
score = 0
q_index = 0
time_per_question = 16
timer_id = None
elapsed_time = 0
total_time_taken = 0 
question_times = [] 
canvas = None
result_label = None
result_btn_frame = None 
start_btn = None
intermission_frame = None
quiz_exit_btn = None
feedback_image_label = None # <--- Naya Variable Image ke liye

# ----------------- Functions -----------------

def start_quiz():
    global q_index, score, canvas, result_label, total_time_taken, question_times, result_btn_frame, start_btn, intermission_frame, quiz_exit_btn, feedback_image_label
    
    # Cleanup previous screens
    if canvas:
        canvas.get_tk_widget().destroy()
    if result_label:
        result_label.destroy()
    if result_btn_frame: 
        result_btn_frame.destroy()
    if intermission_frame:
        intermission_frame.destroy()
    if feedback_image_label: # <--- Image ko bhi clean karo
        feedback_image_label.destroy()
        
    # Start button chupao
    if start_btn:
        start_btn.pack_forget()
    
    # Quiz Exit button dikhao
    if quiz_exit_btn:
        quiz_exit_btn.pack(pady=10)
    
    # Reset Logic
    q_index = 0
    score = 0
    total_time_taken = 0 
    question_times = [] 
    random.shuffle(questions)
    
    show_question()

def show_question():
    global elapsed_time, timer_id, q_index
    
    # Widgets ko wapis dikhao
    question_label.pack(pady=20)
    for btn in option_buttons:
        btn.pack(pady=5)
    timer_label.pack(pady=20)
    
    elapsed_time = 0
    
    # Timer ko 16 seconds par set karo
    timer_label.config(text=f"Time: {time_per_question - elapsed_time} sec") 
    
    q = questions[q_index] 
    question_label.config(text=f"Q{q_index+1}: {q['question']}")
    for i, opt in enumerate(q["options"]):
        option_buttons[i].config(text=opt, state=tk.NORMAL)
    
    update_timer()

def show_intermission_options():
    global intermission_frame, timer_id, question_times, score, total_time_taken, quiz_exit_btn
    
    if timer_id:
        root.after_cancel(timer_id)
        
    # Quiz Exit button chupao
    if quiz_exit_btn:
        quiz_exit_btn.pack_forget()
        
    # Calculate Total Time for display in Intermission
    total_time_taken = sum(question_times) 
        
    # 1. Quiz elements ko chupao
    question_label.pack_forget()
    for btn in option_buttons:
        btn.pack_forget()
    timer_label.pack_forget()
    
    # 2. Intermission Frame banao
    intermission_frame = tk.Frame(root)
    intermission_frame.pack(pady=100)
    
    # 3. Message
    minutes = total_time_taken // 60
    seconds = total_time_taken % 60
    time_display = f"{minutes}m {seconds}s"
    
    tk.Label(intermission_frame, 
             text=f"✅ Checkpoint Reached: Q{q_index} Completed!\n\nScore so far: {score}/{q_index}\nTotal Time: {time_display}", 
             font=("Helvetica", 16, "bold"), justify=tk.CENTER).pack(pady=20, padx=20)
    
    # 4. Submit Button
    submit_btn = tk.Button(intermission_frame, text="🛑 Submit & Finish Quiz", font=("Helvetica", 14), 
                           bg="#d9534f", fg="white", command=end_quiz)
    submit_btn.pack(side=tk.LEFT, padx=15)
    
    # 5. Continue Button
    continue_btn = tk.Button(intermission_frame, text="▶️ Continue Quiz", font=("Helvetica", 14), 
                             bg="#5cb85c", fg="white", command=continue_quiz)
    continue_btn.pack(side=tk.RIGHT, padx=15)

def continue_quiz():
    global intermission_frame, quiz_exit_btn
    if intermission_frame:
        intermission_frame.destroy()
        
    # Quiz Exit button wapis dikhao
    if quiz_exit_btn:
        quiz_exit_btn.pack(pady=10)
        
    show_question()

def advance_quiz():
    global q_index
    
    if q_index >= len(questions):
        end_quiz()
    elif q_index > 0 and q_index % 10 == 0:
        show_intermission_options()
    else:
        show_question()

def check_answer(i):
    global score, q_index, timer_id, elapsed_time, question_times
    q = questions[q_index]
    selected = option_buttons[i]["text"]
    
    if selected == q["answer"]:
        score += 1
    
    question_times.append(elapsed_time)
    
    q_index += 1
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    
    if timer_id:
        root.after_cancel(timer_id)
    
    root.after(500, advance_quiz)

def update_timer():
    global elapsed_time, timer_id, question_times
    elapsed_time += 1 
    timer_label.config(text=f"Time: {time_per_question - elapsed_time} sec")
    
    if elapsed_time >= time_per_question:
        question_times.append(time_per_question)
        
        for btn in option_buttons:
            btn.config(state=tk.DISABLED)
        next_question()
    else:
        timer_id = root.after(1000, update_timer)

def next_question():
    global q_index
    q_index += 1
    advance_quiz()

def end_quiz():
    global canvas, result_label, result_btn_frame, intermission_frame, question_times, total_time_taken, quiz_exit_btn, feedback_image_label
    
    if intermission_frame:
        intermission_frame.destroy()
    
    # Quiz Exit button chupao
    if quiz_exit_btn:
        quiz_exit_btn.pack_forget()
        
    # Final Total Time Calculation
    total_time_taken = sum(question_times) 
        
    # 1. Quiz wale widgets hata do
    question_label.pack_forget()
    for btn in option_buttons:
        btn.pack_forget()
    timer_label.pack_forget()
    
    # Time ko Minutes aur Seconds me convert karo
    minutes = total_time_taken // 60
    seconds = total_time_taken % 60
    time_display = f"{minutes}m {seconds}s"
    
    # 2. Score Text aur Total Time Dikhao
    result_label = tk.Label(root, 
                            text=f"Game Over!\nFinal Score: {score}/{q_index}\nTotal Time: {time_display}", 
                            font=("Helvetica", 16, "bold"))
    result_label.pack(pady=10)
    
    # 3. Pie Chart (same as before)
    labels = ['Correct', 'Wrong']
    sizes = [score, q_index - score] 
    colors = ['#4CAF50', '#F44336'] 
    
    fig = Figure(figsize=(4, 3), dpi=100) 
    ax = fig.add_subplot(111)
    if sum(sizes) == 0: sizes = [0, 1] 
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Performance")
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    # --- FEEDBACK IMAGE LOGIC ---
    image_path = ""
    performance_percentage = (score / q_index) * 100 if q_index > 0 else 0

    if performance_percentage >= 50:
        image_path = "thumbs_up.jpeg" # <--- Apni Thumbs Up image ka naam
        #image_path = "star.jpeg"  <--- Apni Thumbs Up image ka naam
    else:
        image_path = "thumbs_down.png" # <--- Apni Thumbs Down image ka naam
    
    try:
        # Image load aur resize karna
        original_image = Image.open(image_path)
        resized_image = original_image.resize((100, 100), Image.LANCZOS) # Size adjust karein
        
        # ImageTk mein convert karna
        tk_image = ImageTk.PhotoImage(resized_image)
        
        # Image ko label mein dikhana
        feedback_image_label = tk.Label(root, image=tk_image)
        feedback_image_label.image = tk_image # Reference store karna
        feedback_image_label.pack(pady=10)
        
    except FileNotFoundError:
        messagebox.showerror("Image Error", f"Image file '{image_path}' not found.\nPlease ensure it's in the same directory as the script.")
    except Exception as e:
        messagebox.showerror("Image Error", f"An error occurred loading image: {e}")
    # ----------------------------
    
    # 4. Play Again aur Exit Button ko ek Frame mein Rakho
    result_btn_frame = tk.Frame(root)
    result_btn_frame.pack(pady=20)

    restart_btn = tk.Button(result_btn_frame, 
                            text="Play Again", 
                            font=("Helvetica", 16), 
                            bg="#5cb85c", 
                            fg="white", 
                            command=start_quiz)
    restart_btn.pack(side=tk.LEFT, padx=15)

    exit_btn = tk.Button(result_btn_frame, 
                         text="Exit Game", 
                         font=("Helvetica", 16), 
                         bg="#d9534f", 
                         fg="white", 
                         command=root.destroy) 
    exit_btn.pack(side=tk.RIGHT, padx=15)

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("GUI Quiz Game")
root.geometry("500x700") # Height badha di taaki image fit aaye

question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=450, justify="left")

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Helvetica", 12), width=20, command=lambda i=i: check_answer(i))
    option_buttons.append(btn)

timer_label = tk.Label(root, text=f"Time: {time_per_question} sec", font=("Helvetica", 12))

quiz_exit_btn = tk.Button(root, text="Exit Game", font=("Helvetica", 12), bg="#d9534f", fg="white", command=root.destroy)

start_btn = tk.Button(root, text="Start Quiz", font=("Helvetica", 18, "bold"), bg="#428bca", fg="white", command=start_quiz)
start_btn.pack(pady=200)

root.mainloop()
