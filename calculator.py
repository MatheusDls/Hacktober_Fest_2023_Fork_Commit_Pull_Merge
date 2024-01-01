import tkinter as tk

class CalculatorGUI:
    def __init__(self):
        # Initialize the calculator GUI
        self.root = tk.Tk()
        self.configure_gui()
        self.create_frames()
        self.initialize_variables()
        self.create_widgets()
        tk.mainloop()

    def configure_gui(self):
        # Configure the main window settings
        self.root.geometry("200x200")
        self.root.resizable(0, 0)
        self.root.title("Calculator")
        self.root.configure(bg="#67bad1")

    def create_frames(self):
        # Create frames for organizing widgets
        self.top_frame = tk.Frame(self.root, bg="#69bad1")
        self.mid_frame = tk.Frame(self.root)
        self.operation_frame = tk.Frame(self.root)
        self.operation_frame2 = tk.Frame(self.root)
        self.top_frame.pack(side="top", fill="both", expand=True)
        self.mid_frame.pack(side="top", fill="both", expand=True)
        self.operation_frame.pack(side="top", fill="both", expand=True)
        self.operation_frame2.pack(side="top", fill="both", expand=True)

    def initialize_variables(self):
        # Initialize variables, such as the display variable
        self.result_disp = tk.StringVar()
        self.result_disp.set("0")

    def create_widgets(self):
        # Create and place widgets on the frames
        self.create_top_widgets()
        self.create_mid_widgets()
        self.create_operation_widgets()

    def create_top_widgets(self):
        # Create and place the label displaying the result
        total_numb = tk.Label(self.top_frame, textvariable=self.result_disp, bg="#69bad1")
        total_numb.pack(side="right")

    def create_mid_widgets(self):
        # Create and place the entry box for user input
        self.enter_box = tk.Entry(self.mid_frame, width=12, bg="#84cce0")
        self.enter_box.pack(side="top")
        self.enter_box.bind("<Return>", lambda event: self.calculate())  # Call calculate when the user presses "Enter"

    def create_operation_widgets(self):
        # Create and place buttons for arithmetic operations, reset, and quit
        buttons = ["+", "-", "*", "/", "="]
        for button in buttons:
            btn = tk.Button(self.operation_frame, text=button, command=lambda b=button: self.handle_button_click(b), bg="#4f8b9c")
            btn.pack(side="left")

        reset_btn = tk.Button(self.operation_frame, text="Reset", command=self.reset, bg="#4f8b9c")
        reset_btn.pack(side="right")

        quit_btn = tk.Button(self.operation_frame2, text="Quit", command=self.quit_program, bg="#ff2121")
        quit_btn.pack(side="right")

    def handle_button_click(self, button):
        # Handle button clicks, either append the button text to the entry box or trigger the calculation
        current_text = self.enter_box.get()
        if button == "=":
            self.calculate()
        else:
            self.enter_box.delete(0, tk.END)
            self.enter_box.insert(tk.END, button)

    def calculate(self):
        # Evaluate the expression in the entry box and display the result
        try:
            expression = self.enter_box.get()
            result = eval(expression)
            self.result_disp.set(round(result, 4))
        except Exception as e:
            # Handle errors, e.g., division by zero
            self.result_disp.set("Error")

    def reset(self):
        # Reset the entry box and result display
        self.enter_box.delete(0, tk.END)
        self.result_disp.set("0")

    def quit_program(self):
        # Close the application
        self.root.destroy()

def main():
    # Create an instance of the CalculatorGUI class
    gui = CalculatorGUI()

if __name__ == "__main__":
    # Run the application
    main()
