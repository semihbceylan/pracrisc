import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
from simulator import RISC_Simulator


def load_json_file(filename):
    """Load JSON data from a file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load {filename}: {e}")
        return []


class RISC_Simulator_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RISC Simulator")
        self.set_application_logo("risc.png")
        self.root.geometry("800x600")
        self.simulator = RISC_Simulator()
        # Load lessons and quizzes from JSON files
        self.LESSONS = load_json_file("lessons.json")
        self.QUIZZES = load_json_file("quizzes.json")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Add tabs
        self.create_simulator_tab()
        self.create_lessons_tab()
        self.create_quizzes_tab()

        # Initialize the display
        self.update_display()


    def set_application_logo(self, logo_path):
        """Set the application logo from a given file path."""
        try:
            # Use a PhotoImage object to set the icon
            icon = tk.PhotoImage(file=logo_path)
            self.root.iconphoto(False, icon)
        except Exception as e:
            print(f"Error setting logo: {e}")

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

        # Configure a tag for highlighting the current line
        self.instruction_entry.tag_configure("current_line", background="yellow")

        # Buttons
        button_frame = tk.Frame(self.input_frame)
        button_frame.pack(fill="x", pady=5)

        self.run_button = tk.Button(button_frame, text="Run Instructions", command=self.run_instructions)
        self.run_button.pack(side="left", padx=5)

        self.step_button = tk.Button(button_frame, text="Step", command=self.step_instruction)
        self.step_button.pack(side="left", padx=5)

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
        """Run all instructions entered by the user."""
        code = self.instruction_entry.get(1.0, tk.END).strip()
        if code:
            self.simulator.pc = 0  # Reset the program counter
            instructions = code.split('\n')
            while not self.simulator.halted and self.simulator.pc < len(instructions):
                # Remove previous highlight
                self.instruction_entry.tag_remove("current_line", "1.0", tk.END)

                # Highlight the current line
                current_line_start = f"{self.simulator.pc + 1}.0"
                current_line_end = f"{self.simulator.pc + 1}.end"
                self.instruction_entry.tag_add("current_line", current_line_start, current_line_end)

                # Scroll to the current line
                self.instruction_entry.see(current_line_start)

                line = instructions[self.simulator.pc].strip()
                if line:
                    try:
                        self.simulator.run_instruction(line)
                        self.simulator.pc += 1  # Move to the next instruction
                        self.update_display()
                        self.root.update()  # Force GUI update to show the highlight
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {e}")
                        break
                else:
                    self.simulator.pc += 1  # Skip empty lines

    def step_instruction(self):
        """Execute the next instruction and update the display."""
        code = self.instruction_entry.get(1.0, tk.END).strip()
        if code:
            instructions = code.split('\n')
            if self.simulator.pc < len(instructions):
                # Remove previous highlight
                self.instruction_entry.tag_remove("current_line", "1.0", tk.END)

                # Highlight the current line
                current_line_start = f"{self.simulator.pc + 1}.0"
                current_line_end = f"{self.simulator.pc + 1}.end"
                self.instruction_entry.tag_add("current_line", current_line_start, current_line_end)

                # Scroll to the current line
                self.instruction_entry.see(current_line_start)

                line = instructions[self.simulator.pc].strip()
                if line:
                    try:
                        self.simulator.run_instruction(line)
                        self.simulator.pc += 1  # Move to the next instruction
                        self.update_display()
                        self.root.update()  # Force GUI update to show the highlight
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred: {e}")
                else:
                    self.simulator.pc += 1  # Skip empty lines
            else:
                messagebox.showinfo("Info", "All instructions have been executed.")

    def create_lessons_tab(self):
        """Create the lessons tab."""
        self.lessons_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.lessons_tab, text="Lessons")

        # Lesson list
        self.lesson_listbox = tk.Listbox(self.lessons_tab, width=50, height=15)
        self.lesson_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Populate the lesson list
        for i, lesson in enumerate(self.LESSONS):
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
            lesson = self.LESSONS[selected_index[0]]
            self.lesson_content.config(state="normal")
            self.lesson_content.delete(1.0, tk.END)
            self.lesson_content.insert(tk.END, lesson["content"].strip())  # Use .strip() to remove leading/trailing whitespace
            self.lesson_content.config(state="disabled")

    def create_quizzes_tab(self):
        """Create the quizzes tab with a scrollable frame for questions."""
        self.quizzes_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.quizzes_tab, text="Quizzes")

        # Create a canvas for the questions frame
        self.quiz_canvas = tk.Canvas(self.quizzes_tab)
        self.quiz_canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar but keep it hidden
        self.quiz_scrollbar = ttk.Scrollbar(self.quizzes_tab, orient="vertical", command=self.quiz_canvas.yview)
        self.quiz_scrollbar.pack(side="right", fill="y")

        # Configure the canvas to work with the scrollbar
        self.quiz_canvas.configure(yscrollcommand=self.quiz_scrollbar.set)
        self.quiz_canvas.bind(
            "<Configure>",
            lambda e: self.quiz_canvas.configure(scrollregion=self.quiz_canvas.bbox("all"))
        )

        # Frame for questions
        self.questions_frame = tk.Frame(self.quiz_canvas)
        self.quiz_canvas.create_window((0, 0), window=self.questions_frame, anchor="nw")

        # Bind mouse wheel scrolling to the canvas
        self.questions_frame.bind(
            "<Enter>",
            lambda event: self.quiz_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        )
        self.questions_frame.bind(
            "<Leave>",
            lambda event: self.quiz_canvas.unbind_all("<MouseWheel>")
        )

        # Dictionary to store user answers
        self.user_answers = {}

        # Load all questions
        self.load_all_questions()

        # Submit button
        self.submit_button = tk.Button(self.quizzes_tab, text="Submit", command=self.show_results)
        self.submit_button.pack(pady=10)

    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling for the canvas."""
        self.quiz_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def load_all_questions(self):
        """Load all questions and options into the scrollable frame."""
        for i, quiz in enumerate(self.QUIZZES):
            # Create a frame for each question to hold the question label and options
            question_frame = tk.Frame(self.questions_frame)
            question_frame.pack(fill="x", pady=(10, 0), anchor="w")

            # Question label with text wrapping
            question_label = tk.Label(
                question_frame,
                text=f"{i + 1}. {quiz['question']}",
                font=("Arial", 12, "bold"),
                wraplength=800,  # Adjust this value based on your frame width
                justify="left",
                anchor="w"
            )
            question_label.pack(fill="x", anchor="w", pady=(0, 5))  # Fill the width and align left

            # Radio buttons for options
            option_var = tk.StringVar(value="NONE")
            for option in quiz["options"]:
                rb = tk.Radiobutton(
                    question_frame,
                    text=option,
                    variable=option_var,
                    value=option[0],
                    wraplength=800,  # Adjust this value based on your frame width
                    justify="left",
                    anchor="w"
                )
                rb.pack(fill="x", anchor="w")  # Fill the width and align left

            # Store the variable for later use
            self.user_answers[i] = option_var

    def show_results(self):
        """Show the results in a pop-up window with a final score."""
        # Create a new Toplevel window for results
        results_window = tk.Toplevel(self.root)
        results_window.title("Quiz Results")
        results_window.geometry("800x600")  # Adjust size as needed

        # Create a scrollable text area for results
        results_text = scrolledtext.ScrolledText(results_window, width=80, height=30, state="normal")
        results_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Initialize score counter
        correct_answers = 0

        # Check each question and display results
        for i, quiz in enumerate(self.QUIZZES):
            selected_option = self.user_answers[i].get()
            if selected_option == quiz["answer"]:
                result = f"Question {i + 1}: Correct!\n\n"
                correct_answers += 1  # Increment score for correct answers
            elif selected_option == "":  # No option selected
                result = f"Question {i + 1}: No answer selected.\n\n"
            else:
                result = f"Question {i + 1}: Incorrect. The correct answer is {quiz['answer']}.\n"
                result += f"Explanation: {quiz['explanation']}\n\n"
            results_text.insert(tk.END, result)

        # Calculate final score
        total_questions = len(self.QUIZZES)
        final_score = (correct_answers / total_questions) * 100  # Calculate percentage

        # Display final score
        results_text.insert(tk.END, f"\nFinal Score: {final_score:.2f}% ({correct_answers}/{total_questions})\n")

        # Disable editing of the results text
        results_text.config(state="disabled")

        # Add a close button
        close_button = tk.Button(results_window, text="Close", command=results_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RISC_Simulator_GUI(root)
    root.mainloop()