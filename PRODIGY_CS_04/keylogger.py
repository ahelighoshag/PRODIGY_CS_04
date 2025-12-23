import tkinter as tk
import os

# Create file path in same folder as program
FILE_PATH = os.path.join(os.getcwd(), "key_log.txt")

def key_pressed(event):
    key = event.char if event.char else f"[{event.keysym}]"

    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(key)
        file.flush()

    status_label.config(text=f"Logging to: {FILE_PATH}")

# Window
window = tk.Tk()
window.title("Simple Keylogger (Educational)")
window.geometry("550x250")

tk.Label(window, text="Type below (keys will be logged)").pack(pady=5)

text_box = tk.Text(window, height=5, width=60)
text_box.pack()
text_box.focus_set()

text_box.bind("<KeyPress>", key_pressed)

status_label = tk.Label(window, text="", fg="green")
status_label.pack(pady=10)

window.mainloop()
