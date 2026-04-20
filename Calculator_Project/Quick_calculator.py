import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.configure(bg="#0f172a")

# ===== DISPLAY =====
entry = tk.Entry(
    root,
    font=("Arial", 24),
    bg="#111827",
    fg="white",
    insertbackground="white",
    borderwidth=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=20)

# ===== FUNCTIONS =====
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def press(key):
    if key == "=":
        calculate()
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "⌫":
        entry.delete(len(entry.get())-1, tk.END)
    else:
        entry.insert(tk.END, key)

# ===== KEYBOARD SUPPORT (FIXED) =====
def key_event(event):
    if event.char in "0123456789+-*/.":
        entry.insert(tk.END, event.char)
        return "break"

    elif event.keysym == "Return":
        calculate()
        return "break"

    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get())-1, tk.END)
        return "break"

    elif event.keysym == "Escape":
        entry.delete(0, tk.END)
        return "break"

entry.bind("<Key>", key_event)

# ===== BUTTON STYLE =====
btn_bg = "#1e293b"
equal_bg = "#3b82f6"

# ===== BUTTON LAYOUT (FULL 4 COLUMN FIX) =====
buttons = [
    ("C", "⌫", "/", "*"),
    ("7", "8", "9", "-"),
    ("4", "5", "6", "+"),
    ("1", "2", "3", "="),
    ("0", ".", "", "")
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == "":
            continue

        bg = equal_bg if btn == "=" else btn_bg

        tk.Button(
            root,
            text=btn,
            font=("Arial", 16),
            bg=bg,
            fg="white",
            borderwidth=0,
            command=lambda b=btn: press(b)
        ).grid(row=i+1, column=j, sticky="nsew", padx=3, pady=3)

# ===== GRID CONFIG =====
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()