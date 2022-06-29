from tkinter import *
from math import *
from idlelib.tooltip import Hovertip
import struct

class SuperCalculator(object):

    # construct the GUI
    def __init__(self):         # consist of : every variable you need
        window = Tk()           # create window
        window.title("Supercalculator [by Alfina Azaria - 2006482773]")

        # Variable yang di-initialize for the calculator's memory
        self.memory = ""                       # untuk menyimpan memory
        self.expr = ""                          # current expression
        self.startOfNextOperand = True         # start of new operand

        # use Entry widget for display
        self.entry = Entry(window, relief = RIDGE, borderwidth = 3,
                            width = 35, bg = "white", fg = "blue",
                            font = ("Helvatica", 18))
        self.entry.grid(row = 0, column = 0, columnspan = 5)
        

        # Calculator button labels in a 2D list
        buttons = [["Clr", "MC", "M+", "M-", "MR"],
                    ["d", "e", "f", "+", "-"],
                    ["a", "b", "c", "/", "*"],
                    ["7", "8", "9", "**","\u221a"],
                    ["4", "5", "6", "sin", "cos"],
                    ["1", "2", "3", "tan", "ln"],
                    ["0", ".", "\u00b1", "~", "2C"],
                    ["x", "o", "^", "|", "&"],
                    ["π", "int", "rad", "//", "exp"],
                    ["→IEEE", "←IEEE", "asin", "acos", "atan"],
                    ["bin", "hex", "oct", "%", "="]]
        # \u221a = akar
        # \u00b1 = +-

        # for Tooltip, list in a list, sesuai dengan button
        toolTip = [["Clear the display field", "Clear memory", "Add to memory", "Subtract from memory", "Recall from memory"],
                    ["Letter d", "Letter e", "Letter f", "Add", "Subtract"],
                    ["Letter a", "Letter b", "Letter c", "Divide", "Multiply"],
                    ["Digit 7", "Digit 8", "Digit 9", "Power", "Sqrt"],
                    ["Digit 4", "Digit 5", "Digit 6", "Sine(radians)", "Cosine(radians)"],
                    ["Digit 1", "Digit 2", "Digit 3", "Tangent(radians)", "Natural log"],
                    ["Digit 0", "Decimal point", "Toggle +- sign", "Bitwise complement", "32-bit 2's complement"],
                    ["Letter x", "Letter o", "Bitwise XOR", "Bitwise OR", "Bitwise AND"],
                    ["The number pi", "Convert float to int", "Convert degrees to radians", "Integer divide", "Power of E (2.718...)"],
                    ["Decimal to 64-bit IEEE 754 representation (in hex)", "64-bit IEEE 754 representation (in hex) to decimal", "Arc sine, in radians","Arc cosine, in radians", "Arc tan, in radians"],
                    ["Convert int to binary", "Convert int to hexadecimal", "Convert int to octal", "Modulus", "Compute to decimal"]]
        

        # Create and place button in appropriate row and column
        for r in range(11):             # untuk mengakses list in a list
            for c in range(5):
                def cmd(x = buttons[r][c]):
                    self.click(x)               # what happens when the buttons are clicked?

                b = Button(window, text = buttons[r][c], width = 7,
                            bg = "blue", fg = "white", 
                            font = ("Helvatica", 18), relief = RAISED, command = cmd)          # cmd() is the handler

                b.grid(row = r + 1, column = c)     # entry is in row 0

                h = Hovertip(b, text = toolTip[r][c])
        
        window.mainloop()
    
    
    def click(self, key):      # sebagai handler : what happens when the buttons are clicked?
        
        # Dari template
        if key == "=":
            # evaluate the expression, including the value displayed in entry
            # and then display the result

            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, result)      # menghapus semua yang di entry dan di replace dengan result
                self.expr = ""                      # mengosongkan kembali self.expr

            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")

            self.startOfNextOperand = True          # kan udah selesai, mau start a new operand

        elif key in "+-**//%|^&":
            self.expr += self.entry.get()
            self.expr += key

            self.startOfNextOperand = True

        elif key == "MC":     # memory clear => mengosongkan isi self.memory
            self.memory = ""        
            self.startOfNextOperand = True

        elif key == "M+":   # menambahkan displayed value di entry ke self.memory
            try:
                if self.memory == "":
                    self.memory = str(eval(self.entry.get()))
                else:                                                               # jika sudah ada value di self.memory
                    self.memory = str(eval(self.memory + "+" + self.entry.get()))   # eval => untuk mengeksekusi apapun yang ada didalam
                    
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")

        elif key == "M-":   # mengurangkan displayed value yang ada di entry dengan apa yang ada di self.memory
            try:
                if self.memory == "":
                    self.entry.delete(0, END)
                    self.entry.insert(END, "Error")
                else:
                    self.memory = str(eval(self.memory + "-" + self.entry.get()))
                
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")

        elif key == "MR":   # memory recall => menampilkan value yang ada di self.memory ke entry
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)

        # +-
        elif key == "\u00b1":
            # switch entry from positive to negative or vice versa
            # kalo gaada value di entry, do nothing
            try:
                if self.entry.get()[0] == "-":     # kalo entry merupakan bilangan negatif, (-) nya diilangin => jadi positive
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, "-")       # kalo gaada (-) which is berarti bilangan positive,
                                                    # ditambahin (-) => jadi negatif
            except IndexError:
                pass                # do nothing
        
        # \u221a = square root
        elif key == "\u221a":
            try:
                result = sqrt(float(self.entry.get()))      # float() agar nanti hasilnya juga bisa dalam bentuk float
                self.entry.delete(0, END)
                self.entry.insert(END, result)              # menghapus semua yang di entry dan di replace dengan result
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True
        
        elif key == "ln":       # returns : natural log
            try:
                result = log(float(self.entry.get()))       # math.log
                self.entry.delete(0, END)
                self.entry.insert(END, result)              # menghapus semua yang di entry dan di replace dengan result
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            self.startOfNextOperand = True
        
        elif key == "π":                        # kalo di click pi, cuma munculin the value of math.pi
                                                # agar bisa dioperasikan dengan yang lain. Contoh = menghitung luas lingkaran
            self.entry.delete(0, END)           # delete dari awal hingga akhir
            self.entry.insert(END, pi)          # math.pi => kan tadi udah import math

            self.startOfNextOperand = True
        

        elif key in ["sin", "cos", "tan", "asin", "acos", "atan"]:
            try :
                if key == "sin":
                    result = sin(float(self.entry.get()))     # karena ingin dihitung, jadi harus dalam bentuk integer
                elif key == "cos":
                    result = cos(float(self.entry.get()))     # karena udah from math import *, jadi langsung aja gausah math.
                elif key == "tan":
                    result = tan(float(self.entry.get()))
                elif key == "asin":
                    result = asin(float(self.entry.get()))
                elif key == "acos":
                    result = acos(float(self.entry.get()))
                elif key == "atan":
                    result = atan(float(self.entry.get()))

                self.entry.delete(0, END)
                self.entry.insert(END, result)      # menghapus semua yang di entry dan di replace dengan result
                    
            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True
        

        elif key in ["bin", "hex", "oct", "int", "rad"]:
            try:
                if key == "bin":
                    result = bin(int(self.entry.get()))     # convert to binary
                elif key == "hex":
                    result = hex(int(self.entry.get()))     # convert to hexadecimal
                elif key == "oct":
                    result = oct(int(self.entry.get()))     # convert to octal
                elif key == "int": 
                    result = int(self.entry.get())          # convert to integer
                elif key == "rad":
                    result = radians(float(self.entry.get()))       # convert degrees to radians
                
                self.entry.delete(0, END)
                self.entry.insert(END, result)      # menghapus semua yang di entry dan di replace dengan result
            
            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True

        # Bitwise complement
        elif key == "~":
            try:
                result = eval("~" + self.entry.get())       # evaluate the given source
                self.entry.delete(0, END)
                self.entry.insert(END, result)              # menghapus semua yang di entry dan di replace dengan result
            
            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True

        # 32-bit 2's complement
        elif key == "2C":
            try:
                temp_entry = self.entry.get()                   # variable temp untuk ngecek entry itu merupakan bilangan apa (decimal, hexadecimal, octal, binary)
                prefix = "0b"
                
                if temp_entry[:2] == prefix:                                # jika entry sudah berupa 2's complement, tetapi bukan 32-bit
                    result = prefix + temp_entry[2:].zfill(32)
                    self.entry.delete(0, END)
                    self.entry.insert(END, result) 
                
                elif temp_entry[:2] == "0o":                                # jika entry merupakan octal
                    result = prefix + bin(int(temp_entry, 8)).zfill(32)
                    self.entry.delete(0, END)
                    self.entry.insert(END, result) 
                
                elif temp_entry[:2] == "0x":                                # jika entry merupakan hexadecimal
                    result = prefix + bin(int(temp_entry, 16)).zfill(32)
                    self.entry.delete(0, END)
                    self.entry.insert(END, result) 

                else:                                                       # jika entry merupakan bilangan biasa (selain kondisi di atas)
                    dec_Int = int(self.entry.get())
                
                    # akan ada 3 kondisi lagi : 
                    if dec_Int == 0 :
                        self.entry.delete(0, END)
                        self.entry.insert(END, (prefix + "0" * 32))     # karena yang diminta 32-bit 2's complement

                    elif dec_Int > 0 :
                        binstr = ""              # bikin variabel untuk hasil conversion
                        temp = dec_Int
                        
                        while temp > 0 :
                            bindigit = temp % 2
                            binstr = str(bindigit) + binstr
                            temp = temp // 2

                        twocomp = binstr.zfill(32)      # hasil conversion

                        self.entry.delete(0, END)
                        self.entry.insert(END, prefix + twocomp)

                    elif dec_Int < 0 :
                        positiveInt = (2 ** 32) + dec_Int       # dari codingan lab04
                        temp = positiveInt
                        binstr = ""
                        
                        while temp > 0 :
                            bindigit = temp % 2
                            binstr = str(bindigit) + binstr
                            temp = temp // 2
        
                        twocomp = binstr.zfill(32)      # hasil 2 compnya

                        self.entry.delete(0, END)
                        self.entry.insert(END, prefix + twocomp)

            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True
        
        # Exp = exponential. Nilai e nya itu berapa
        elif key == "exp":
            try:
                result = exp(float(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(END, result)      # menghapus semua yang di entry dan di replace dengan result
            
            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True
        
        elif key in ["→IEEE", "←IEEE"]:
            try:
                if key == "→IEEE":          # Decimal to 64-bit IEEE 754 representation (in hex)
                    
                    prefix = "0x"
                    self.bytes_IEEE = struct.pack(">d", float(self.entry.get()))      # bytes
                                                                                    # self => agar bisa dipakai untuk membalikan IEEE
                    hexadecimal = self.bytes_IEEE.hex()                 # diubah ke hexadecimal
                    result = prefix + hexadecimal      
                    
                    self.entry.delete(0, END)
                    self.entry.insert(END, result)
                
                elif key == "←IEEE":    # if key == "←IEEE"
                                        # 64-bit IEEE 754 representation (in hex) to decimal
                    backToDec = struct.unpack(">d", self.bytes_IEEE)[0]         # karena hasilnya dlm bentuk tuple,
                                                                                # dan kita hanya butuh elemen pertamanya aja
                    self.entry.delete(0, END)
                    self.entry.insert(END, backToDec)
            
            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
            
            self.startOfNextOperand = True

        elif key == "Clr":             
            self.entry.delete(0, END)   # to clear all entry
            self.expr = ""              # yang tersimpan di self.expr juga harus dihapus
            self.startOfNextOperand = True
        
        else:           # selain buttons (conditional) yang diatas,
                        # dia hanya delete apa yang ada di entry, 
                        # dan menulis lagi sesuai button yang dipencet (setiap startOfNextOperand)
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False     # habis di delete, di reset ke False
        
            self.entry.insert(END, key)


if __name__ == "__main__":
    SuperCalculator()