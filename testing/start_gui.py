import tkinter as tk
from subprocess import Popen, PIPE

def run_code():
    process = Popen(['python', 'Testing\\Code.py'], stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    if stderr:
        print("Error:", stderr)
    else:
        print(stdout)

app = tk.Tk()
app.title("Desktopography")

# Set the background color and window size
app.configure(bg="#808080")
app.geometry("400x300")

# Create a label for the title
title_label = tk.Label(app, text="Launcher", font=("Bauhaus 93", 40), bg="#808080")
title_label.pack(pady=20)

# Create buttons with custom styles
button_game = tk.Button(app, text="Begin", command=run_code, bg="#4CAF50", fg="white", font=("Bauhaus 93", 34))
button_game.pack(pady=20)

app.mainloop()