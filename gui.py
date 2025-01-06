import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from simulator import RISC_Simulator
from lessons import LESSONS
from quizzes import QUIZZES

class RISC_Simulator_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RISC Simulator")
        self.root.geometry("800x600")
        self.simulator = RISC_Simulator()

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Add tabs
        self.create_simulator_tab()
        self.create_lessons_tab()
        self.create_quizzes_tab()
        self.create_answers_tab()  # Add the Answers tab

        # Initialize the display
        self.update_display()

    def decimal_to_binary(self, value, bits=32):
        """Convert a decimal value to a binary string with a fixed number of bits."""
        if value < 0:
            # Handle negative values using two's complement
            return bin(value & (2**bits - 1))[2:].zfill(bits)
        else:
            return bin(value)[2:].zfill(bits)

    def create_simulator_tab(self):
        """Create the simulator tab."""
        self.simulator_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.simulator_tab, text="Simulator")

        # Frame for registers, memory, and PC
        self.state_frame = tk.LabelFrame(self.simulator_tab, text="Current State", padx=10, pady=10)
        self.state_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Program counter display
        self.pc_label = tk.Label(self.state_frame, text="Program Counter (PC): 0", font=("Arial", 12, "bold"))
        self.pc_label.pack(anchor="w")

        # Registers display
        self.registers_label = tk.Label(self.state_frame, text="Registers:", font=("Arial", 12, "bold"))
        self.registers_label.pack(anchor="w")
        self.registers_text = scrolledtext.ScrolledText(self.state_frame, width=60, height=7, state="disabled")
        self.registers_text.pack(fill="both", expand=True)

        # Memory display
        self.memory_label = tk.Label(self.state_frame, text="Memory:", font=("Arial", 12, "bold"))
        self.memory_label.pack(anchor="w")
        self.memory_text = scrolledtext.ScrolledText(self.state_frame, width=60, height=7, state="disabled")
        self.memory_text.pack(fill="both", expand=True)

        # Instruction input
        self.input_frame = tk.LabelFrame(self.simulator_tab, text="Enter RISC Instructions", padx=10, pady=10)
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.instruction_entry = scrolledtext.ScrolledText(self.input_frame, width=50, height=4)
        self.instruction_entry.pack(fill="x", expand=True)

        # Buttons
        button_frame = tk.Frame(self.input_frame)
        button_frame.pack(fill="x", pady=5)

        self.run_button = tk.Button(button_frame, text="Run Instructions", command=self.run_instructions)
        self.run_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_simulator)
        self.reset_button.pack(side="left", padx=5)

    def reset_simulator(self):
        """Reset the simulator to its initial state."""
        self.simulator = RISC_Simulator()  # Reinitialize the simulator
        self.instruction_entry.delete(1.0, tk.END)  # Clear the instruction input box
        self.update_display()  # Update the display to show the reset state
        messagebox.showinfo("Reset", "Simulator has been reset to its initial state.")

    def update_display(self):
        """Update the display with the current state of registers, memory, and PC."""
        # Update program counter
        self.pc_label.config(text=f"Program Counter (PC): {self.simulator.pc}")

        # Update registers
        self.registers_text.config(state="normal")
        self.registers_text.delete(1.0, tk.END)
        self.registers_text.insert(tk.END, self.format_registers())
        self.registers_text.config(state="disabled")

        # Update memory
        self.memory_text.config(state="normal")
        self.memory_text.delete(1.0, tk.END)
        self.memory_text.insert(tk.END, self.format_memory())
        self.memory_text.config(state="disabled")

    def format_registers(self):
        """Format the registers for display, showing both decimal and binary values."""
        formatted_registers = []
        for reg, value in self.simulator.registers.items():
            binary_value = self.decimal_to_binary(value)  # Convert to binary
            formatted_registers.append(f"{reg}: {value:10} (0b{binary_value})")
        return "\n".join(formatted_registers)

    def format_memory(self):
        """Format the memory for display, showing both decimal and binary values."""
        formatted_memory = []
        for addr, value in self.simulator.memory.items():
            binary_value = self.decimal_to_binary(value)  # Convert to binary
            formatted_memory.append(f"{addr}: {value:10} (0b{binary_value})")
        return "\n".join(formatted_memory)

    def run_instructions(self):
        """Run the instructions entered by the user."""
        code = self.instruction_entry.get(1.0, tk.END).strip()
        if code:
            self.simulator.pc = 0  # Reset the program counter
            try:
                self.simulator.run(code)
                self.update_display()  # Update the display after running instructions
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def create_lessons_tab(self):
        """Create the lessons tab."""
        self.lessons_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.lessons_tab, text="Lessons")

        # Lesson list
        self.lesson_listbox = tk.Listbox(self.lessons_tab, width=50, height=15)
        self.lesson_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Populate the lesson list
        for i, lesson in enumerate(LESSONS):
            self.lesson_listbox.insert(tk.END, f"{i + 1}. {lesson['title']}")

        # Lesson content display
        self.lesson_content = scrolledtext.ScrolledText(self.lessons_tab, width=50, height=15, state="disabled")
        self.lesson_content.pack(fill="both", expand=True, padx=10, pady=10)

        # Bind lesson selection to display content
        self.lesson_listbox.bind("<<ListboxSelect>>", self.display_lesson_content)

    def display_lesson_content(self, event):
        """Display the content of the selected lesson."""
        selected_index = self.lesson_listbox.curselection()
        if selected_index:
            lesson = LESSONS[selected_index[0]]
            self.lesson_content.config(state="normal")
            self.lesson_content.delete(1.0, tk.END)
            self.lesson_content.insert(tk.END, lesson["content"])
            self.lesson_content.config(state="disabled")

    def create_quizzes_tab(self):
        """Create the quizzes tab."""
        self.quizzes_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.quizzes_tab, text="Quizzes")

        # Quiz list
        self.quiz_listbox = tk.Listbox(self.quizzes_tab, width=50, height=15)
        self.quiz_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Populate the quiz list
        for i, quiz in enumerate(QUIZZES):
            self.quiz_listbox.insert(tk.END, f"{i + 1}. {quiz['question']}")

        # Quiz content display
        self.quiz_content = scrolledtext.ScrolledText(self.quizzes_tab, width=50, height=15, state="disabled")
        self.quiz_content.pack(fill="both", expand=True, padx=10, pady=10)

        # Bind quiz selection to display content
        self.quiz_listbox.bind("<<ListboxSelect>>", self.display_quiz_content)

    def display_quiz_content(self, event):
        """Display the content of the selected quiz."""
        selected_index = self.quiz_listbox.curselection()
        if selected_index:
            quiz = QUIZZES[selected_index[0]]
            self.quiz_content.config(state="normal")
            self.quiz_content.delete(1.0, tk.END)
            self.quiz_content.insert(tk.END, f"{quiz['question']}\n\nOptions:\n")
            for option in quiz["options"]:
                self.quiz_content.insert(tk.END, f"{option}\n")
            self.quiz_content.config(state="disabled")

    def create_answers_tab(self):
        """Create the answers tab."""
        self.answers_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.answers_tab, text="Answers")

        # Answers content display
        self.answers_content = scrolledtext.ScrolledText(self.answers_tab, width=60, height=20, state="normal")
        self.answers_content.pack(fill="both", expand=True, padx=10, pady=10)

        # Populate the answers content
        self.display_all_answers()

    def display_all_answers(self):
        """Display all quiz questions, answers, and explanations."""
        self.answers_content.delete(1.0, tk.END)  # Clear existing content
        for i, quiz in enumerate(QUIZZES):
            self.answers_content.insert(tk.END, f"Question {i + 1}:\n")
            self.answers_content.insert(tk.END, f"  Question: {quiz['question']}\n")
            self.answers_content.insert(tk.END, f"  Answer: {quiz['answer']}\n")
            if "explanation" in quiz:
                self.answers_content.insert(tk.END, f"  Explanation: {quiz['explanation']}\n\n")
            else:
                self.answers_content.insert(tk.END, "\n")
        self.answers_content.config(state="disabled")  # Make the text read-only

if __name__ == "__main__":
    root = tk.Tk()
    app = RISC_Simulator_GUI(root)
    root.mainloop()