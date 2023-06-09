import customtkinter as ctk
import time
from tkinter import messagebox


root = ctk.CTk()
root.geometry("300x200")
root.title("Countdown Timer")
root.resizable(False, False)

hour_str = ctk.StringVar()
minute_str = ctk.StringVar()
second_str = ctk.StringVar()

hour_str.set("00")
minute_str.set("00")
second_str.set("00")

hour_entry = ctk.CTkEntry(root, textvariable=hour_str, width=60, font=("Calibri", 40), justify="center", state="normal")
minute_entry = ctk.CTkEntry(root, textvariable=minute_str, width=60, font=("Calibri", 40), justify="center", state="normal")
second_entry = ctk.CTkEntry(root, textvariable=second_str, width=60, font=("Calibri", 40), justify="center", state="normal")
hour_entry.place(x=80, y=70, anchor="center")
minute_entry.place(x=150, y=70, anchor="center")
second_entry.place(x=220, y=70, anchor="center")

x = True


def start():
    global x
    x = True
    total_time = int(hour_str.get()) * 3600 + int(minute_str.get()) * 60 + int(second_str.get())

    hour_entry.configure(state="disabled")
    minute_entry.configure(state="disabled")
    second_entry.configure(state="disabled")

    while (total_time > -1) and (x == True):
        minutes, seconds = divmod(total_time, 60)
        hours = 0
        if minutes > 60:
            hours, minutes = divmod(minutes, 60)

        hour_str.set("{:02d}".format(hours))
        minute_str.set("{:02d}".format(minutes))
        second_str.set("{:02d}".format(seconds))

        root.update()
        time.sleep(1)

        if total_time == 0:
            messagebox.showinfo("", "time is up")
            hour_entry.configure(state="normal")
            minute_entry.configure(state="normal")
            second_entry.configure(state="normal")

        total_time -= 1


def stop():
    global x
    x = False


def reset():
    global x
    x = False
    hour_str.set("00")
    minute_str.set("00")
    second_str.set("00")
    hour_entry.configure(state="normal")
    minute_entry.configure(state="normal")
    second_entry.configure(state="normal")


start_btn = ctk.CTkButton(root, text="start", font=("Calibri", 18), width=50, command=start)
start_btn.place(x=90, y=140, anchor="center")
stop_btn = ctk.CTkButton(root, text="stop", font=("Calibri", 18), width=50, command=stop)
stop_btn.place(x=150, y=140, anchor="center")
reset_btn = ctk.CTkButton(root, text="reset", font=("Calibri", 18), width=50, command=reset)
reset_btn.place(x=210, y=140, anchor="center")

root.mainloop()
