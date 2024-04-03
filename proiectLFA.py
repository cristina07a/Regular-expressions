import tkinter as tk
import re

#creating window
window1 = tk.Tk()
 
#sizing of the interface
width = window1.winfo_screenwidth() 
height = window1.winfo_screenheight()

#setting window size as half screen and adding the window name
window1.geometry("%dx%d" % (width/2, height/2))
window1.title("Regular expression application")

def printPattern(): 
    pattern = inputtxt_pattern.get(1.0, "end-1c")
    try:
        re.compile(pattern)
        lbl_pattern.config(text="Pattern: " + pattern) 
    except re.error as e:
        lbl_pattern.config(text="Invalid pattern: " + str(e)) 

def printText(): 
    pattern = inputtxt_pattern.get(1.0, "end-1c")
    txt1 = inputtxt_text.get(1.0, "end-1c")
    if re.fullmatch(pattern, txt1):
        lbl_text.config(text="Text1 is fully matched with the pattern")
    else:
        lbl_text.config(text="Text1 does not fully match the pattern")

def printText2(): 
    pattern = inputtxt_pattern.get(1.0, "end-1c")
    txt2 = inputtxt_text2.get(1.0, "end-1c")
    matches = re.findall(pattern, txt2)
    lbl_text2.config(text="Matches found in Text2: " + str(matches))



#pattern input
input_label = tk.Label(window1, text="Pattern:")
input_label.pack()

frame_pattern = tk.Frame(window1)
frame_pattern.pack()

inputtxt_pattern = tk.Text(frame_pattern, height=2, width=50) 
inputtxt_pattern.pack() 

printButton_pattern = tk.Button(window1, text="Print Pattern", command=printPattern)
printButton_pattern.place(x=650, y=27) 

lbl_pattern = tk.Label(window1, text=" ") 
lbl_pattern.pack() 

#text1 input
text1_label = tk.Label(window1, text="Text1:")
text1_label.pack()

frame_text = tk.Frame(window1)
frame_text.pack()

inputtxt_text = tk.Text(frame_text, height=2, width=50) 
inputtxt_text.pack() 

printButton_text = tk.Button(window1, text="Check Text1", command=printText)
printButton_text.place(x=650, y=100) 

lbl_text = tk.Label(window1, text=" ") 
lbl_text.pack() 

#text2 input
text2_label = tk.Label(window1, text="Text2:")
text2_label.pack()

frame_text2 = tk.Frame(window1)
frame_text2.pack()

inputtxt_text2 = tk.Text(frame_text2, height=4, width=50) 
inputtxt_text2.pack() 

printButton_text2 = tk.Button(window1, text="Find Matches", command=printText2)
printButton_text2.place(x=650, y=220) 

lbl_text2 = tk.Label(window1, text=" ") 
lbl_text2.pack() 

window1.mainloop()
