import json
import tkinter as tk
import random

def save_flashcards():
    with open("flashcards.json", "w") as f:
        json.dump(flashcards, f)

def load_flashcards():
    try:
        with open("flashcards.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

flashcards = load_flashcards()
current_index = [0]
showing_answer = [False]

def show_card():
    if len(flashcards) == 0:
        question_label.config(text="No flashcards!")
        return
    card = flashcards[current_index[0]]
    question_label.config(text=card["question"])
    showing_answer[0] = False
    score_label.config(text=f"Card {current_index[0]+1} of {len(flashcards)}")

def flip():
    if len(flashcards) == 0:
        return
    card = flashcards[current_index[0]]
    if showing_answer[0]:
        question_label.config(text=card["question"])
        showing_answer[0] = False
    else:
        question_label.config(text=card["answer"])
        showing_answer[0] = True

def next_card():
    if len(flashcards) == 0:
        return
    current_index[0] = (current_index[0] + 1) % len(flashcards)
    show_card()

def prev_card():
    if len(flashcards) == 0:
        return
    current_index[0] = (current_index[0] - 1) % len(flashcards)
    show_card()

def open_editor():
    top = tk.Toplevel(window)
    top.title("Edit Flashcards")
    top.geometry("400x400+500+100")

    def refresh():
        for widget in frame.winfo_children():
            widget.destroy()
        for i, flash in enumerate(flashcards, 0):
            tk.Label(frame, text=f"{i+1}. {flash['question']}").pack()
            tk.Button(frame, text="Delete", command=lambda idx=i: delete_card(idx)).pack()

    def delete_card(idx):
        flashcards.pop(idx)
        save_flashcards()
        show_card()
        refresh()

    def add_card():
        new_question = question_entry.get()
        new_answer = answer_entry.get()
        if new_question and new_answer:
            flashcards.append({"question": new_question, "answer": new_answer})
            save_flashcards()
            question_entry.delete(0, tk.END)
            answer_entry.delete(0, tk.END)
            show_card()
            refresh()

    tk.Label(top, text="Add a new card:").pack(pady=5)
    tk.Label(top, text="Question:").pack()
    question_entry = tk.Entry(top, width=40)
    question_entry.pack()
    tk.Label(top, text="Answer:").pack()
    answer_entry = tk.Entry(top, width=40)
    answer_entry.pack()
    tk.Button(top, text="Add", command=add_card).pack(pady=5)

    tk.Label(top, text="Saved cards:").pack(pady=5)
    frame = tk.Frame(top)
    frame.pack()
    refresh()

window = tk.Tk()
window.title("Flashcard App")
window.geometry("400x300")

score_label = tk.Label(window, text="")
score_label.pack(pady=5)

question_label = tk.Label(window, text="", font=("Arial", 16), wraplength=350)
question_label.pack(pady=40)

flip_button = tk.Button(window, text="Flip", command=flip)
flip_button.pack(pady=5)

nav_frame = tk.Frame(window)
nav_frame.pack(pady=5)
tk.Button(nav_frame, text="← Prev", command=prev_card).pack(side="left", padx=10)
tk.Button(nav_frame, text="Next →", command=next_card).pack(side="left", padx=10)

edit_button = tk.Button(window, text="Edit Cards", command=open_editor)
edit_button.pack(pady=10)

show_card()
window.mainloop()