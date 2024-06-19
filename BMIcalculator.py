
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os, sys
from tkinter import messagebox as m

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title(" - BMI Calculator --")
root.geometry("500x670")
root.resizable(False, False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



meter = ImageTk.PhotoImage(Image.open(resource_path("meter.png")))
meter_img = Label(root, image=meter, bd=0)
meter_img.pack(pady=10)

def clear_screen(Event=None):
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text="")

def get_bmi(*args):
    our_height = float(h_entry.get())
    our_weight = float(w_entry.get())
    bmi = our_weight / (our_height ** 2)
    bmi_rounded = round(bmi, 2)

    results.configure(text=f"{str(bmi_rounded)}")

    if bmi_rounded < 18.5:
        results.configure(
            text=f"{str(bmi_rounded)}\nUnderweight", text_color="#54b1e1"
        )
    elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
        results.configure(text=f"{str(bmi_rounded)}\nNormal", text_color="#b3d686")
    elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
        results.configure(
            text=f"{str(bmi_rounded)}\nOverweight", text_color="#fed429"
        )
    elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
        results.configure(text=f"{str(bmi_rounded)}\nObese", text_color="#fbaf42")
    elif bmi_rounded >= 35:
        results.configure(
            text=f"{str(bmi_rounded)}\nExtreme Obese", text_color="#f2535"
        )

h1_label = customtkinter.CTkLabel(master=root, text="", font=("helvetica", 15, "bold"))
h1_label.pack(pady=0)

h_entry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Height In Meters",
    width=200,
    height=30,
    border_width=1,
    corner_radius=10,
)
h_entry.pack(pady=20)
h_entry.bind(
    "<FocusIn>",
    lambda e: h1_label.configure(text="Height in meters", text_color="#8D6F3A"),
)
h_entry.bind("<FocusOut>", lambda e: h1_label.configure(text=""))

h2_label = customtkinter.CTkLabel(master=root, text="", font=("helvetica", 15, "bold"))
h2_label.pack(pady=0)

w_entry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Weight in Kg",
    width=200,
    height=30,
    border_width=1,
    corner_radius=10,
)
w_entry.pack(pady=20)
w_entry.bind(
    "<FocusIn>",
    lambda e: h2_label.configure(text="Weight in kg", text_color="#98FB98"),
)
w_entry.bind("<FocusOut>", lambda e: h2_label.configure(text=""))


button_1 = customtkinter.CTkButton(
    master=root,
    text="Calculate BMI",
    width=190,
    height=40,
    compound="top",
    command=get_bmi,
)
button_1.pack(pady=20)

button_2 = customtkinter.CTkButton(
    master=root,
    text="Clear Screen",
    width=190,
    height=40,
    fg_color="#D35B58",
    hover_color="#C77C78",
    command=clear_screen,
)
button_2.pack(pady=20)
root.bind("<Control-Key-c>", clear_screen)


results = customtkinter.CTkLabel(master=root, text="", font=("Helvetica", 28))
results.pack(pady=50)

def checkempty():
    if h_entry.get() == "" or w_entry.get() == "":
        m.showerror("--BMI--Calculator", "Enter Values first to Calculate")
    else:
        pass

def on_enter(event):
    checkempty()
    get_bmi()

def move_up(event):
    h_entry.focus_set()

def move_down(event):
    w_entry.focus_set()

def end_it(*args):
    root.destroy()


root.mainloop()
