import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def applicationSupportsSecureRestorableState() -> bool:
    return True

import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Timeless")
#root.resizable(False, False)
root.geometry("500x300")

# button = ctk.CTkButton(master=root, text="Start Timer", corner_radius=10)
# button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# frame = ctk.CTkFrame(master=root,
#                     width=400, 
#                     height=150,
#                     corner_radius=15, 
#                     bg_color="white")
# frame.pack(padx=10, pady=10)

# frameButton = ctk.CTkButton(master=frame, text="New Session", corner_radius=10)
# frameButton.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# tabView = ctk.CTkTabview(master=root)
# tabView.pack(padx=5, pady=20)

# tabView.add("Template 1")
# tabView.add("Template 2")
# tabView.add("Template 3")

# tabView.set("Template 1")

# temp1Button = ctk.CTkButton(master=tabView.tab("Template 1"), text="Add Template", corner_radius=10)
# temp1Button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# textBox = tk.Text(master=frame, highlightthickness=1)
# textBox.grid(row = 0, column = 0, sticky="nsew")

# scrollBar = ctk.CTkScrollbar(master=frame, command=textBox.yview)
# scrollBar.grid(row=0, column=1, stick="ns")

# textBox.configure(yscrollcommand=scrollBar.set)


frame = ctk.CTkFrame(master=root, width=500, height=200, corner_radius=15)
frame.pack(padx=20, pady=20)



root.mainloop()
