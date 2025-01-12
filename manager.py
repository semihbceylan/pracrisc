import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import json
import os

QUIZZES = []
LESSONS = []


class QuizManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz and Lessons Manager")
        self.set_application_logo("risc.png")
        # Create tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create Quiz Manager tab
        self.quiz_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.quiz_tab, text="Quiz Manager")
        self.create_quiz_manager_widgets()

        # Create Lessons Manager tab
        self.lessons_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.lessons_tab, text="Lessons Manager")
        self.create_lessons_manager_widgets()

        # Load data
        self.load_quizzes()
        self.load_lessons()

    def set_application_logo(self, logo_path):
        """Set the application logo from a given file path."""
        try:
            # Use a PhotoImage object to set the icon
            icon = tk.PhotoImage(file=logo_path)
            self.root.iconphoto(False, icon)
        except Exception as e:
            print(f"Error setting logo: {e}")
    
    # --- Quiz Manager ---
    def create_quiz_manager_widgets(self):
        # Question list
        self.quiz_listbox = tk.Listbox(self.quiz_tab, height=15, width=100)
        self.quiz_listbox.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        self.quiz_listbox.bind('<<ListboxSelect>>', self.display_selected_quiz)

        # Buttons
        tk.Button(self.quiz_tab, text="Add Quiz", command=self.add_quiz).grid(row=1, column=0, pady=5)
        tk.Button(self.quiz_tab, text="Update Quiz", command=self.update_quiz).grid(row=1, column=1, pady=5)
        tk.Button(self.quiz_tab, text="Delete Quiz", command=self.delete_quiz).grid(row=1, column=2, pady=5)
        tk.Button(self.quiz_tab, text="Save Changes", command=self.save_quizzes).grid(row=1, column=3, pady=5)

        # Details area
        self.quiz_details_frame = tk.Frame(self.quiz_tab)
        self.quiz_details_frame.grid(row=2, column=0, columnspan=4, pady=10)

        tk.Label(self.quiz_details_frame, text="Question:").grid(row=0, column=0, sticky=tk.W)
        self.question_entry = tk.Entry(self.quiz_details_frame, width=80)
        self.question_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.quiz_details_frame, text="Options (comma-separated):").grid(row=1, column=0, sticky=tk.W)
        self.options_entry = tk.Entry(self.quiz_details_frame, width=80)
        self.options_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.quiz_details_frame, text="Answer:").grid(row=2, column=0, sticky=tk.W)
        self.answer_entry = tk.Entry(self.quiz_details_frame, width=80)
        self.answer_entry.grid(row=2, column=1, pady=5)

        tk.Label(self.quiz_details_frame, text="Explanation:").grid(row=3, column=0, sticky=tk.W)
        self.explanation_entry = tk.Entry(self.quiz_details_frame, width=80)
        self.explanation_entry.grid(row=3, column=1, pady=5)

    def load_quizzes(self):
        self.quiz_listbox.delete(0, tk.END)
        if os.path.exists('quizzes.json'):
            with open('quizzes.json', 'r') as file:
                global QUIZZES
                QUIZZES = json.load(file)
        for quiz in QUIZZES:
            self.quiz_listbox.insert(tk.END, quiz['question'])

    def display_selected_quiz(self, event):
        try:
            selected_index = self.quiz_listbox.curselection()[0]
            selected_quiz = QUIZZES[selected_index]

            self.question_entry.delete(0, tk.END)
            self.question_entry.insert(0, selected_quiz['question'])

            self.options_entry.delete(0, tk.END)
            self.options_entry.insert(0, ", ".join(selected_quiz['options']))

            self.answer_entry.delete(0, tk.END)
            self.answer_entry.insert(0, selected_quiz['answer'])

            self.explanation_entry.delete(0, tk.END)
            self.explanation_entry.insert(0, selected_quiz['explanation'])
        except IndexError:
            pass

    def add_quiz(self):
        new_quiz = {
            "question": self.question_entry.get().strip(),
            "options": [opt.strip() for opt in self.options_entry.get().split(',')],
            "answer": self.answer_entry.get().strip(),
            "explanation": self.explanation_entry.get().strip()
        }
        QUIZZES.append(new_quiz)
        self.load_quizzes()
        messagebox.showinfo("Success", "Quiz added successfully!")

    def update_quiz(self):
        try:
            selected_index = self.quiz_listbox.curselection()[0]
            QUIZZES[selected_index] = {
                "question": self.question_entry.get().strip(),
                "options": [opt.strip() for opt in self.options_entry.get().split(',')],
                "answer": self.answer_entry.get().strip(),
                "explanation": self.explanation_entry.get().strip()
            }
            self.load_quizzes()
            messagebox.showinfo("Success", "Quiz updated successfully!")
        except IndexError:
            messagebox.showerror("Error", "No quiz selected for updating.")

    def delete_quiz(self):
        try:
            selected_index = self.quiz_listbox.curselection()[0]
            del QUIZZES[selected_index]
            self.load_quizzes()
            messagebox.showinfo("Success", "Quiz deleted successfully!")
        except IndexError:
            messagebox.showerror("Error", "No quiz selected for deletion.")

    def save_quizzes(self):
        with open('quizzes.json', 'w') as file:
            json.dump(QUIZZES, file, indent=4)
        messagebox.showinfo("Save Changes", "Quizzes saved successfully!")

    # --- Lessons Manager ---
    def create_lessons_manager_widgets(self):
        # Lesson list
        self.lesson_listbox = tk.Listbox(self.lessons_tab, height=15, width=100)
        self.lesson_listbox.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        self.lesson_listbox.bind('<<ListboxSelect>>', self.display_selected_lesson)

        # Buttons
        tk.Button(self.lessons_tab, text="Add Lesson", command=self.add_lesson).grid(row=1, column=0, pady=5)
        tk.Button(self.lessons_tab, text="Update Lesson", command=self.update_lesson).grid(row=1, column=1, pady=5)
        tk.Button(self.lessons_tab, text="Save Changes", command=self.save_lessons).grid(row=1, column=2, pady=5)

        # Details area
        self.lesson_details_frame = tk.Frame(self.lessons_tab)
        self.lesson_details_frame.grid(row=2, column=0, columnspan=3, pady=10)

        tk.Label(self.lesson_details_frame, text="Title:").grid(row=0, column=0, sticky=tk.W)
        self.title_entry = tk.Entry(self.lesson_details_frame, width=80)
        self.title_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.lesson_details_frame, text="Content:").grid(row=1, column=0, sticky=tk.W)
        self.content_text = tk.Text(self.lesson_details_frame, width=80, height=10)
        self.content_text.grid(row=1, column=1, pady=5)

    def load_lessons(self):
        self.lesson_listbox.delete(0, tk.END)
        if os.path.exists('lessons.json'):
            with open('lessons.json', 'r') as file:
                global LESSONS
                LESSONS = json.load(file)
        for lesson in LESSONS:
            self.lesson_listbox.insert(tk.END, lesson['title'])

    def display_selected_lesson(self, event):
        try:
            selected_index = self.lesson_listbox.curselection()[0]
            selected_lesson = LESSONS[selected_index]

            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, selected_lesson['title'])

            self.content_text.delete(1.0, tk.END)
            self.content_text.insert(tk.END, selected_lesson['content'])
        except IndexError:
            pass

    def add_lesson(self):
        new_lesson = {
            "title": self.title_entry.get().strip(),
            "content": self.content_text.get(1.0, tk.END).strip()
        }
        LESSONS.append(new_lesson)
        self.load_lessons()
        messagebox.showinfo("Success", "Lesson added successfully!")

    def update_lesson(self):
        try:
            selected_index = self.lesson_listbox.curselection()[0]
            LESSONS[selected_index] = {
                "title": self.title_entry.get().strip(),
                "content": self.content_text.get(1.0, tk.END).strip()
            }
            self.load_lessons()
            messagebox.showinfo("Success", "Lesson updated successfully!")
        except IndexError:
            messagebox.showerror("Error", "No lesson selected for updating.")

    def save_lessons(self):
        with open('lessons.json', 'w') as file:
            json.dump(LESSONS, file, indent=4)
        messagebox.showinfo("Save Changes", "Lessons saved successfully!")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizManagerApp(root)
    root.mainloop()
