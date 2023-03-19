# Packages Used
from customtkinter import *
import customtkinter
import os
import urllib.request

# Window Properties
root = customtkinter.CTk()
root.config(bg="black")
root.title("Epic")
root.iconbitmap("images/icons.ico")
root.resizable(width=False, height=False)
#root.attributes("-alpha", 0.9)
#root.attributes("-toolwindow", True)


#Fuctions Used In the Program
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


# Main Function
def main(event):
    values = entry.get()
    entry.delete(0, END)
    label.configure(text=values)
    

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
    
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False


    insertInput(values.capitalize())

    
    if "hi" in values.lower():
        insertResult("Hello there how can i help you, Today!")
    elif "what" in values.lower() or "where" in values.lower() or "when" in values.lower() or "why" in values.lower() or "how" in values.lower() or "who" in values.lower():
        if connect() == True:
            insertResult("Here's A quick Google Search!")
            import webbrowser

            webbrowser.open(f"https://www.google.com/search?q={values}")
        else:
            insertResult("No Internet! Cannot perform Task!")
    else:
        try:
            os.startfile(values)
            
            insertResult("Loading... Plz Wait!")
            name = True
        except:
            insertResult("Unknown Command")
            name = False
        try:
            if name == False:
                try:
                    os.system(values)
                except:
                    insertResult("Sorry Cant help you with that!")
            else:
                pass
        except:
            pass

    


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
