from tkinter import *
from tkinter.ttk import Combobox
import random
import string

root = Tk()
root.geometry("500x500")
root.title("Random Password Generator")
root.config(bg="purple")  # Fixed typo: "purpule" → "purple"

all_no = {"1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "4", "4", "5", "5", "5", "5", "6", "6", "7", "7", "8", "8", "8", "9", "9", "9",
          "10", "10", "10", "11", "11", "11", "12", "12", "13", "13", "14", "14", "14", "15", "15", "16", "16", "16", "17", "17", "18",
          "18", "19", "19", "20", "20", "21", "21", "22", "22", "23", "23", "23", "24", "24", "25", "25", "26", "26", "27", "27", "28",
          "28", "29", "29", "30", "30"}

Title = Label(root, text="Random Password Generator", bg="purple",
              fg="black", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady=20)  # Fixed pady value (removed quotes)

length = Label(root, text="Select the Length of Your Password:-",
               fg="darkred", bg="white", font=("ubuntu", 10))
length.place(x=20, y=70)  # Fixed x/y values (removed quotes)

solidboss = IntVar()
Selector = Combobox(root, textvariable=solidboss, state="readonly")
Selector['values'] = tuple(range(4, 31))  # Length options
Selector.current(4)  # Default selection
Selector.place(x=270, y=72)  # Adjusted position

# Label to show the result
result = Label(root, text="", fg="white", bg="purple", font=("consolas", 12, "bold"))
result.place(x=20, y=200)

# Function to generate password
def generate_password():
    length = solidboss.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    result.config(text=f"Generated Password:\n{password}")

# Button to trigger password generation
btn = Button(root, text="Generate Password", command=generate_password,
             bg="lightblue", fg="black", font=("Arial", 12, "bold"))
btn.place(x=170, y=130)

root.mainloop()
