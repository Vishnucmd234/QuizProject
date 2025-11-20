import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk 
from tkinter import messagebox
import random
import pygame 

# --- PYGAME INITIALIZATION ---
try:
    pygame.mixer.init()
except Exception as e:
    print(f"Warning: Could not initialize pygame mixer: {e}") 
    class DummySound:
        def play(self): pass
    pygame.mixer = type('DummyMixer', (object,), {'Sound': lambda x: DummySound()})


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
feedback_image_label = None # feedback_image_label वापस जोड़ा गया है

# --- AUDIO VARIABLES ---
try:
    # केवल GAMEOVER_MUSIC को लोड करें, WAV फ़ाइल का उपयोग करें
    GAMEOVER_MUSIC = pygame.mixer.Sound("gameover.wav")
    
    class DummySound:
        def play(self): pass
    CORRECT_SOUND = DummySound()
    WRONG_SOUND = DummySound()
    
except Exception as e:
    class DummySound:
        def play(self): pass
    GAMEOVER_MUSIC = DummySound()
    print(f"Audio files could not be loaded. Ensure 'gameover.wav' is present. Error: {e}")

# DUMMY QUESTIONS (आप अपनी प्रश्न सूची से बदलें)
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Picasso", "Da Vinci", "Monet"], "answer": "Da Vinci"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "Nacl"], "answer": "H2O"},
    {"question": "How many days are in a leap year?", "options": ["365", "366", "360", "364"], "answer": "366"},
    {"question": "The study of plants is called?", "options": ["Zoology", "Geology", "Botany", "Physics"], "answer": "Botany"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Dickens", "Shakespeare", "Hemingway", "Austen"], "answer": "Shakespeare"},
    {"question": "What is the square root of 81?", "options": ["8", "9", "7", "11"], "answer": "9"},
    {"question": "Which city hosts the Eiffel Tower?", "options": ["London", "Paris", "New York", "Tokyo"], "answer": "Paris"},
    {"question": "The sun is a:", "options": ["Planet", "Star", "Moon", "Comet"], "answer": "Star"}, 
    {"question": "What is the largest land animal?", "options": ["Giraffe", "Elephant", "Rhinoceros", "Hippopotamus"], "answer": "Elephant"},
    {"question": "The main component of the air we breathe is which gas?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Nitrogen"},
    {"question": "How many seconds are there in one minute?", "options": ["30", "60", "90", "100"], "answer": "60"},
    {"question": "Which fruit is known for being long and yellow?", "options": ["Apple", "Orange", "Grape", "Banana"], "answer": "Banana"},
    {"question": "What is the capital city of Japan?", "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"], "answer": "Tokyo"},
    {"question": "What number comes after ten?", "options": ["Twelve", "Nine", "Eleven", "Twenty"], "answer": "Eleven"},
    {"question": "Which material is a magnet attracted to?", "options": ["Wood", "Plastic", "Iron", "Glass"], "answer": "Iron"},
    {"question": "Who was the first person to walk on the moon?", "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], "answer": "Neil Armstrong"},
    {"question": "A dozen equals how many?", "options": ["6", "10", "12", "20"], "answer": "12"},
    {"question": "Which famous landmark is located in Rome, Italy?", "options": ["Big Ben", "Colosseum", "Taj Mahal", "Eiffel Tower"], "answer": "Colosseum"},
    {"question": "The young one of a cat is called a?", "options": ["Puppy", "Cub", "Kid", "Kitten"], "answer": "Kitten"},
    {"question": "Which color is made by mixing blue and yellow?", "options": ["Red", "Orange", "Green", "Purple"], "answer": "Green"},
    {"question": "What do you call a house made of ice?", "options": ["Hut", "Igloo", "Tent", "Cave"], "answer": "Igloo"}


]

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
    if feedback_image_label: # इमेज लेबल को नष्ट करें यदि वह मौजूद है
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
        
    if quiz_exit_btn:
        quiz_exit_btn.pack_forget()
        
    total_time_taken = sum(question_times) 
        
    question_label.pack_forget()
    for btn in option_buttons:
        btn.pack_forget()
    timer_label.pack_forget()
    
    intermission_frame = tk.Frame(root)
    intermission_frame.pack(pady=100)
    
    minutes = total_time_taken // 60
    seconds = total_time_taken % 60
    time_display = f"{minutes}m {seconds}s"
    
    tk.Label(intermission_frame, 
             text=f"✅ Checkpoint Reached: Q{q_index} Completed!\n\nScore so far: {score}/{q_index}\nTotal Time: {time_display}", 
             font=("Helvetica", 16, "bold"), justify=tk.CENTER).pack(pady=20, padx=20)
    
    submit_btn = tk.Button(intermission_frame, text="🛑 Submit & Finish Quiz", font=("Helvetica", 14), 
                           bg="#d9534f", fg="white", command=end_quiz)
    submit_btn.pack(side=tk.LEFT, padx=15)
    
    continue_btn = tk.Button(intermission_frame, text="▶️ Continue Quiz", font=("Helvetica", 14), 
                             bg="#5cb85c", fg="white", command=continue_quiz)
    continue_btn.pack(side=tk.RIGHT, padx=15)

def continue_quiz():
    global intermission_frame, quiz_exit_btn
    if intermission_frame:
        intermission_frame.destroy()
        
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
    global canvas, result_label, result_btn_frame, intermission_frame, question_times, total_time_taken, quiz_exit_btn, feedback_image_label, q_index
    
    # 📢 Game Over संगीत चलाओ
    GAMEOVER_MUSIC.play() 
    
    if intermission_frame:
        intermission_frame.destroy()
    
    if quiz_exit_btn:
        quiz_exit_btn.pack_forget()
        
    total_time_taken = sum(question_times) 
    
    attempted_questions = q_index
        
    # Quiz widgets hide
    question_label.pack_forget()
    for btn in option_buttons:
        btn.pack_forget()
    timer_label.pack_forget()
    
    minutes = total_time_taken // 60
    seconds = total_time_taken % 60
    time_display = f"{minutes}m {seconds}s"
    
    result_label = tk.Label(root, 
                            text=f"Game Over!\nFinal Score: {score}/{attempted_questions}\nTotal Time: {time_display}", 
                            font=("Helvetica", 16, "bold"))
    result_label.pack(pady=10)
    
    # Pie Chart
    labels = ['Correct', 'Wrong']
    sizes = [score, attempted_questions - score] 
    colors = ['#4CAF50', '#F44336'] 
    
    fig = Figure(figsize=(4, 3), dpi=100) 
    ax = fig.add_subplot(111)
    if sum(sizes) == 0: sizes = [0, 1] 
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Performance")
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    # --- FEEDBACK IMAGE LOGIC (वापस जोड़ा गया) ---
    image_path = ""
    # सुनिश्चित करें कि attempted_questions 0 न हो, अन्यथा डिवीजन बाय जीरो एरर होगा
    if attempted_questions > 0:
        performance_percentage = (score / attempted_questions) * 100 
    else:
        performance_percentage = 0 # यदि कोई प्रश्न हल नहीं हुआ तो 0%
        
    if performance_percentage >= 50:
        image_path = "thumbs_up.jpeg" 
    else:
        image_path = "thumbs_down.png" 
    
    try:
        original_image = Image.open(image_path)
        resized_image = original_image.resize((100, 100), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        
        feedback_image_label = tk.Label(root, image=tk_image)
        feedback_image_label.image = tk_image 
        feedback_image_label.pack(pady=10)
        
    except FileNotFoundError:
        messagebox.showerror("Image Error", f"Feedback image file '{image_path}' not found. Please ensure it is in the same directory as the script.")
    except Exception as e:
        messagebox.showerror("Image Error", f"An error occurred loading feedback image: {e}")
    # ----------------------------
    
    # Play Again and Exit Button Frame
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
root.title("GUI Quiz Game (Final Score & Images)")
root.geometry("500x700") 

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