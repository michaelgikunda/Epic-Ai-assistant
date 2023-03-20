# Packages Used
from customtkinter import *
import customtkinter
import os
import urllib.request
from textblob import TextBlob
import random

# Window Properties
root = customtkinter.CTk()
root.config(bg="black")
root.title("Epic")
root.iconbitmap("images/icons.ico")
root.resizable(width=False, height=False)

# Window Properties
root = customtkinter.CTk()
root.config(bg="black")
root.title("Epic")
root.iconbitmap("images/icons.ico")
root.resizable(width=False, height=False)
#root.attributes("-alpha", 0.9)
#root.attributes("-toolwindow", True)


# Functions Used In the Program
# --------------------------- # 

# Function for Center Window
def center_window():
    window_height = 550
    window_width = 520

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

center_window()

# Function to scroll both listboxes at the same time
def on_mousewheel(event):
    # Scroll both listboxes
    listbox.yview_scroll(int(-1*(event.delta/120)), "units")
    listbox_results.yview_scroll(int(-1*(event.delta/120)), "units")


# Function for inserting Values into the listboxes

def insertResult(values):
        listbox.configure(state=NORMAL)
        listbox.insert(END, f"\n  {values}\n\n")
        listbox.configure(state=DISABLED)
        listbox.yview_moveto(1.0)

def insertInput(values):
    listbox_results.configure(state=NORMAL)
    listbox_results.insert(END, f"                   {values}\n\n\n")
    listbox_results.configure(state=DISABLED)
    listbox_results.yview_moveto(1.0)

# ----------------------- #

# Function for checking if user is connected to the internet

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

# --------------------- #


# Function for looking for files and opening them

def open_file(file_name):
    folders = ['Downloads', 'Documents', 'Pictures', 'Music', 'Videos', 'Desktop']
    extensions = ['', '.exe', '.bat', '.cmd', '.txt', '.png', '.jpg', '.ico', '.jpeg']  # Add more extensions as needed
    for folder in folders:
        for ext in extensions:
            file_path = os.path.join(os.path.expanduser('~'), folder, file_name + ext)
            if os.path.exists(file_path):
                os.startfile(file_path)
                insertResult("Loading... Plz Wait!")
                return True
            
    insertResult(f"File '{file_name}' not found.")
    return False

# ---------------- #


# Main Function
def main(event):
    values = entry.get()
    entry.delete(0, END)
    label.configure(text=values)


    insertInput(values.capitalize())

     # Process input message using TextBlob
    blob = TextBlob(values)
    # Get the subject of the input message
    subject = blob.subjectivity
    # Get the sentiment of the input message
    sentiment = blob.sentiment.polarity
    # ---------------- #

    # Established to prevent some the search function to be activated when the sentiment is present
    decision = False

    if "hi" in values.lower() or "hello" in values.lower():
        insertResult("Hello there, how can I help you today?")
        decision = True

    elif sentiment > 0.5:
        insertResult("I'm sorry, I didn't quite understand that.")

    elif sentiment > 0.1:
        responses = ["That's great to hear!", "Awesome!", "I'm glad to hear that!"]
        insertResult(random.choice(responses))
        decision = True

    elif sentiment < -0.1:
        responses = ["I'm sorry to hear that.", "That's too bad.", "I hope things get better for you."]
        insertResult(random.choice(responses))
        decision = True

    elif "what" in values.lower() or "where" in values.lower() or "when" in values.lower() or "why" in values.lower() or "who" in values.lower():
        if connect() == True and decision == False:
            insertResult("Here's a quick Google search!")
            import webbrowser

            webbrowser.open(f"https://www.google.com/search?q={values}")
        else:
            insertResult("No internet connection! Cannot perform task.")

    elif "open" in values.lower():

        program = values.lower().replace("open ", "")
        open_file(program)

    else:
        try:
            os.startfile(values)
            insertResult("Loading... Plz Wait!")
            name = True
        except:
            insertResult("Unknown Command")
            name = False
        
    
# ------------------------ #
# End of Functions


# Compnents in the Window
# --------------------- #
 
label = CTkLabel(root, text="", bg_color="black", text_color="white")
label.pack()

entry = CTkEntry(root, width=500, height=40, bg_color="#3F51B5", placeholder_text= "Input Program Name", placeholder_text_color="#FFFFFF", border_width=0, font=("Dosis", 18), fg_color="#3F51B5", text_color="black")
entry.place(x=10, y=500)
entry.focus_force()


listbox = CTkTextbox(root, width=250, height=400, border_width=0, border_color="gray",font=("bahnschrift", 13) ,activate_scrollbars=False, text_color="white", bg_color="#101010", fg_color="#101010")
listbox.place(x=10, y=45)
listbox.configure(state=DISABLED)

listbox_results = CTkTextbox(root, width=250, height=400, border_width=0, border_color="gray",font=("bahnschrift", 13), activate_scrollbars=False, text_color="green", bg_color="#101010", fg_color="#101010")
listbox_results.place(x=260, y=45)
listbox_results.configure(state=DISABLED)

# ------------------- #
# End of components


root.bind('<Return>', main)
# Bind mousewheel event to both listboxes
listbox.bind("<MouseWheel>", on_mousewheel)
listbox_results.bind("<MouseWheel>", on_mousewheel)
root.mainloop()
