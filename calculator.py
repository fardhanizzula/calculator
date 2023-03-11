import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("ujang calculator")
        master.config(bg='#EDF1D6')

        # Membuat Tampilan Widget 
        self.display = tk.Entry(master, bg='#9DC08B', width=30, justify="right", font=("Helvetica", 20))
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Pembuatan Tombol (Button)
        button_colors = {
            "1": "#6690ad", "2": "#6690ad", "3": "#6690ad", "/": "#bebebe", "C": "#bebebe",
            "4": "#6690ad", "5": "#6690ad", "6": "#6690ad", "*": "#bebebe", "Del": "#bebebe",
            "7": "#6690ad", "8": "#6690ad", "9": "#6690ad", "-": "#bebebe", "Exit": "#bebebe",
            "0": "#6690ad", ".": "#bebebe", "=": "#bebebe", "+": "#bebebe", 
        }
        buttons = [
            "1", "2", "3", "/", "C",
            "4", "5", "6", "*", "Del",
            "7", "8", "9", "-", "Exit",
            "0", ".", "=", "+", 
        ]

        # Menambahkan Tombol (Button) ke tampilan
        row = 1
        col = 0
        for button in buttons:
            if button == "":
                continue
            command = lambda x=button: self.button_click(x)
            tk.Button(master, text=button, width=5, font=('Helvetica', 16), bg=button_colors[button], command=command).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        # mengkonfigurasi layout
        for i in range(5):
            master.grid_columnconfigure(i, weight=1)
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)

    def button_click(self, button):
        if button == "C":
            self.display.delete(0, tk.END)
        elif button == "CE":
            self.display.delete(0, tk.END)
        elif button == "Exit":
            self.master.destroy()
        elif button == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "Del":
            self.display.delete(len(self.display.get())-1, tk.END)
        else:
            self.display.insert(tk.END, button)

# Create the main window and start the event loop
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
calculator = Calculator(root)
root.mainloop()