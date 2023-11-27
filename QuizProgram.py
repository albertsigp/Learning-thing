import tkinter as tk
from tkinter import messagebox

# Data:
questions = ["What is the capital of France?", "What is 2 + 2?"]
choices = [["Paris", "London", "Berlin"], ["3", "4", "5"]]
answers = ["Paris", "4"]

# Current question index
current_question = 0

# Check if answer correct or wrong:
def check_answer():
    global current_question
    if var.get() == answers[current_question]:
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect!", "Sorry, that's not correct.")
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("End", "The quiz is over!")

# Display the next question:
def display_question():
    question_label.config(text=questions[current_question])
    for i in range(len(choices[current_question])):
        radio_buttons[i].config(text=choices[current_question][i], value=choices[current_question][i])
        radio_buttons[i].deselect()
    var.set(None)


root = tk.Tk()
root.title("Quiz App")
root.geometry('600x400')


var = tk.StringVar(value=None)

# Create a label for displaying questions
question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

# Create buttons for choices:
radio_buttons = []
for _ in range(3):
    radio_button = tk.Radiobutton(root, text="", variable=var, font=("Arial", 12), value="")
    radio_button.pack(anchor='w')
    radio_buttons.append(radio_button)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=20)

# Display the first question
display_question()

# Loop so it doesnt crash instantly:
root.mainloop()
