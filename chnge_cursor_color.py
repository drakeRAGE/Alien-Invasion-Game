# Import library
import tkinter as tk

# Create Tkinter window
frame =tk.Tk()
frame.title("GFG Cursors")
frame.geometry("200x200")

# Specify various cursors icons
# for label and buttons

tk.Button(frame, text="Circle cursor",
        cursor="circle #FF00FF").pack()

tk.Button(frame, text="Plus cursor",
        cursor="plus red").pack()

# Specify cursor icon and color using
# config() method
a = tk.Button(frame, text="Exit")
a.config(cursor="dot greed red")
a.pack()

frame.mainloop()