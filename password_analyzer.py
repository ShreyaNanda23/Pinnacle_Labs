import tkinter as tk
from tkinter import ttk

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        entry.config(show='')
        toggle_btn.config(text='Hide')

def analyze_password():
    password = entry.get()
    result_label.config(text="", fg="#333")
    strength_bar['value'] = 0
    strength_label.config(text="", fg="#333")

    if len(password) < 8:
        result_label.config(text="• Password must be at least 8 characters long.", fg="red")
        strength_label.config(text="Weak", fg="red")
        strength_bar['value'] = 20
        return

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "@#!$%&*?" for char in password)

    checks = [
        ("Uppercase letter", has_upper),
        ("Lowercase letter", has_lower),
        ("Digit", has_digit),
        ("Special character", has_special)
    ]

    output = ""
    score = 0

    for label, passed in checks:
        if passed:
            output += f"• {label}: exists\n"
            score += 1
        else:
            output += f"• {label}: missing\n"

    result_label.config(text=output.strip(), fg="#333")

    strength_bar['value'] = score * 25
    if score == 4:
        strength_label.config(text="Strong 💪", fg="green")
    elif score >= 2:
        strength_label.config(text="Moderate ⚠️", fg="orange")
    else:
        strength_label.config(text="Weak ❌", fg="red")

# UI
window = tk.Tk()
window.title("🔐 Password Analyzer")
window.geometry("450x420")
window.configure(bg="#e0f7fa")
window.resizable(True, True)

# Title bar
tk.Label(window, text="Password Analyzer", font=("Verdana", 18, "bold"),
         bg="#e0f7fa", fg="#00796b").pack(pady=15)

# Entry box
frame = tk.Frame(window, bg="#e0f7fa")
frame.pack(pady=10)
entry = tk.Entry(frame, show='*', width=30, font=("Verdana", 12))
entry.pack(side="left", padx=5)
toggle_btn = tk.Button(frame, text="Show", command=toggle_password,
                       bg="#95dae0", font=("Verdana", 10))
toggle_btn.pack(side="left", padx=5)

# Analyze button
tk.Button(window, text="Check Strength", command=analyze_password,
          font=("Verdana", 12, "bold"), bg="#00796b", fg="white", padx=12, pady=6).pack(pady=15)

# Results area
result_label = tk.Label(window, text="", font=("Verdana", 11),
                        justify="left", bg="#e0f7fa", fg="#333")
result_label.pack(pady=5)

# Progress bar
strength_bar = ttk.Progressbar(window, length=300, mode='determinate')
strength_bar.pack(pady=10)

strength_label = tk.Label(window, text="", font=("Verdana", 12, "bold"),
                          bg="#e0f7fa", fg="#333")
strength_label.pack()

window.mainloop()
