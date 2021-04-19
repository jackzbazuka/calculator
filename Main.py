from math import sin, cos
from math import log as ln
from math import pi as π
import tkinter as tk

# Custom defined exception to be raised incase of incorrect operator usage
class InvalidOperation(Exception):
    pass

# Application main frame
class MyCal(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master=master)
        self.master = master

        # Tk() object attribute setting
        self.master.title('Calculator')
        self.master.resizable(False, False)
        self.warningTxtVar = tk.StringVar() # declaring warning text variable which can be altered later

        # Button attributes setting
        buttonHeight = 3
        buttonWidth = 6

        # TEXT WIDGET
        self.boxOneEntry = tk.Entry(self.master, font=("Calibri", 16), width=30, bd=2)

        # BUTTON WIDGETS
        self.buttonclear = tk.Button(self.master, text="AC", height=buttonHeight, width=buttonWidth, command=lambda:self.boxOneEntry.delete(0, "end"))
        self.buttoneval = tk.Button(self.master, text="=", height=buttonHeight, width=buttonWidth, command=lambda: self.evalExpression(self.boxOneEntry.get()))

        # yellow buttons
        self.buttonadd = tk.Button(self.master, text="+", height=buttonHeight, width=buttonWidth, highlightbackground="#F5F3B0", fg="#C48000", command=lambda:self.boxOneEntry.insert("end", "+"))
        self.buttonsub = tk.Button(self.master, text="-", height=buttonHeight, width=buttonWidth, highlightbackground="#F5F3B0", fg="#C48000", command=lambda:self.boxOneEntry.insert("end", "-"))
        self.buttonmult = tk.Button(self.master, text="x", height=buttonHeight, width=buttonWidth, highlightbackground="#F5F3B0", fg="#C48000", command=lambda:self.boxOneEntry.insert("end", "*"))
        self.buttondiv = tk.Button(self.master, text="÷", height=buttonHeight, width=buttonWidth, highlightbackground="#F5F3B0", fg="#C48000", command=lambda:self.boxOneEntry.insert("end", "/"))
        self.buttondel = tk.Button(self.master, text="DEL", height=buttonHeight, width=buttonWidth, highlightbackground="#F5F3B0", fg="#C48000", command=lambda: self.boxOneEntry.delete(len(self.boxOneEntry.get())-1,"end"))

        # violet buttons
        self.button0 = tk.Button(self.master, text="0", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "0"))
        self.button1 = tk.Button(self.master, text="1", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "1"))
        self.button2 = tk.Button(self.master, text="2", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "2"))
        self.button3 = tk.Button(self.master, text="3", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "3"))
        self.button4 = tk.Button(self.master, text="4", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "4"))
        self.button5 = tk.Button(self.master, text="5", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "5"))
        self.button6 = tk.Button(self.master, text="6", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "6"))
        self.button7 = tk.Button(self.master, text="7", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "7"))
        self.button8 = tk.Button(self.master, text="8", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "8"))
        self.button9 = tk.Button(self.master, text="9", height=buttonHeight, width=buttonWidth, highlightbackground="#C1BEFC", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "9"))

        # pink buttons
        self.buttonsin = tk.Button(self.master, text="sin", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "sin("))
        self.buttoncos = tk.Button(self.master, text="cos", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "cos("))
        self.buttonlog = tk.Button(self.master, text="ln", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "ln("))
        self.buttonlbrack = tk.Button(self.master, text="(", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "("))
        self.buttonrbrack = tk.Button(self.master, text=")", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", ")"))
        self.buttonpow = tk.Button(self.master, text="x²", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "**2"))
        self.buttondot = tk.Button(self.master, text=".", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "."))
        self.buttonpi = tk.Button(self.master, text="π", height=buttonHeight, width=buttonWidth, highlightbackground="#FCBEDB", fg="#534F9D", command=lambda:self.boxOneEntry.insert("end", "π"))

        # LABEL WIDGET
        self.warningLabel = tk.Label(self.master, textvariable=self.warningTxtVar, fg="red")


        # GRID LAYOUT
        #row0
        self.boxOneEntry.grid(row=0, column=0, columnspan=5, ipadx=10, ipady=10)

        #row1
        self.buttonsin.grid(row=1, column=0, padx=1, pady=2)
        self.buttonlog.grid(row=1, column=1, padx=1, pady=2)
        self.buttonlbrack.grid(row=1, column=2, padx=1, pady=2)
        self.buttonrbrack.grid(row=1, column=3, padx=1, pady=2)
        self.buttonadd.grid(row=1, column=4, padx=1, pady=2)

        #row2
        self.buttoncos.grid(row=2, column=0, padx=1, pady=2)
        self.button9.grid(row=2, column=1, padx=1, pady=2)
        self.button8.grid(row=2, column=2, padx=1, pady=2)
        self.button7.grid(row=2, column=3, padx=1, pady=2)
        self.buttonsub.grid(row=2, column=4, padx=1, pady=2)

        #row3
        self.buttonpi.grid(row=3, column=0, padx=1, pady=2)
        self.button6.grid(row=3, column=1, padx=1, pady=2)
        self.button5.grid(row=3, column=2, padx=1, pady=2)
        self.button4.grid(row=3, column=3, padx=1, pady=2)
        self.buttonmult.grid(row=3, column=4, padx=1, pady=2)

        #row4
        self.buttonpow.grid(row=4, column=0, padx=1, pady=2)
        self.button3.grid(row=4, column=1, padx=1, pady=2)
        self.button2.grid(row=4, column=2, padx=1, pady=2)
        self.button1.grid(row=4, column=3, padx=1, pady=2)
        self.buttondiv.grid(row=4, column=4, padx=1, pady=2)

        #row5
        self.buttondot.grid(row=5, column=0, padx=1, pady=2)
        self.buttonclear.grid(row=5, column=1, padx=1, pady=2)
        self.button0.grid(row=5, column=2, padx=1, pady=2)
        self.buttoneval.grid(row=5, column=3, padx=1, pady=2)
        self.buttondel.grid(row=5, column=4, padx=1, pady=2)


    # COMMAND METHODS
    def evalExpression(self, exp):

        try:
            temp = eval(exp)
            self.boxOneEntry.delete(0, "end")
            self.boxOneEntry.insert("end", temp)
        except NameError:
            self.boxOneEntry.delete(0, "end")
            self.boxOneEntry.config(highlightbackground="red")
            self.boxOneEntry.insert("end", "PLEASE ENTER A NUMBER !")
            self.boxOneEntry.after(2000, lambda: self.errorHandling())
        except ZeroDivisionError:
            self.boxOneEntry.delete(0, "end")
            self.boxOneEntry.config(highlightbackground="red")
            self.boxOneEntry.insert("end", "ZERO DIVISION ERROR !")
            self.boxOneEntry.after(2000, lambda: self.errorHandling())
        except ValueError:
            self.boxOneEntry.delete(0, "end")
            self.boxOneEntry.config(highlightbackground="red")
            self.boxOneEntry.insert("end", "INAPPROPRIATE VALUE PROVIDED !")
            self.boxOneEntry.after(2000, lambda: self.errorHandling())


    def errorHandling(self):  # This method clears and reconfigures text box after warning flash

        self.boxOneEntry.delete(0, "end")
        self.boxOneEntry.config(highlightbackground="black")

# Driver code

if __name__ == "__main__":
    root = tk.Tk()
    gorg = MyCal(master=root)
    root.mainloop()
