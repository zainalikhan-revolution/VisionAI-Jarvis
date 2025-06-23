import tkinter as tk
from vision import capture_and_describe

def run_vision_ai():
    result = capture_and_describe()
    result_label.config(text=f"🧠 AI: {result}")

app = tk.Tk()
app.title("Vision AI Jarvis")
app.geometry("400x300")

title = tk.Label(app, text="👁️ Vision AI Jarvis", font=("Arial", 18))
title.pack(pady=10)

run_btn = tk.Button(app, text="Capture & Describe", command=run_vision_ai)
run_btn.pack(pady=10)

result_label = tk.Label(app, text="", wraplength=300)
result_label.pack(pady=20)

app.mainloop()
