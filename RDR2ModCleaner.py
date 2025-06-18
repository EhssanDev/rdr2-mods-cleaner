import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# إعدادات المودات
mod_extensions = ['.asi', '.dll', '.log', '.ini', '.txt']
mod_folders = ['scripts', 'mods', 'LML', 'asi']

def delete_mods():
    game_dir = folder_path.get()
    if not game_dir or not os.path.exists(game_dir):
        messagebox.showerror("Error", "Please select the correct RDR2 game folder.")
        return

    deleted_files = []
    deleted_folders = []

    for root, dirs, files in os.walk(game_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in mod_extensions):
                try:
                    full_path = os.path.join(root, file)
                    os.remove(full_path)
                    deleted_files.append(os.path.relpath(full_path, game_dir))
                except Exception as e:
                    deleted_files.append(f"{file} (Error: {e})")

    for folder in mod_folders:
        path = os.path.join(game_dir, folder)
        if os.path.exists(path) and os.path.isdir(path):
            try:
                shutil.rmtree(path)
                deleted_folders.append(folder)
            except Exception as e:
                deleted_folders.append(f"{folder} (Error: {e})")

    result_text.config(state='normal')
    result_text.delete('1.0', tk.END)
    if deleted_files or deleted_folders:
        result_text.insert(tk.END, "✅ Deleted Files:\n")
        for f in deleted_files:
            result_text.insert(tk.END, f" - {f}\n")
        result_text.insert(tk.END, "\n✅ Deleted Folders:\n")
        for f in deleted_folders:
            result_text.insert(tk.END, f" - {f}\n")
    else:
        result_text.insert(tk.END, "✅ No mod files or folders found.")
    result_text.config(state='disabled')

def browse_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def show_about():
    messagebox.showinfo("About This Tool", 
        "I originally created this tool for myself because I genuinely needed it,\n"
        "and I couldn't find anything similar online.\n\n"
        "Now I believe others might benefit from it as well.\n\n"
        "- Ehssandev")

# إنشاء الواجهة
app = tk.Tk()
app.title("RDR2 Mod Cleaner")
app.geometry("680x550")
app.configure(bg="#101820")  # خلفية داكنة مريحة

folder_path = tk.StringVar()

# خطوط وألوان
label_font = ("Segoe UI", 11)
button_font = ("Segoe UI", 10, "bold")
text_font = ("Consolas", 10)

highlight_color = "#00AEEF"  # أزرق جميل
button_color = "#1F2E3D"
text_bg = "#1A1A1A"
text_fg = "#ffffff"

# عناصر الواجهة
tk.Label(app, text="Select your RDR2 game folder:", font=label_font, fg="white", bg="#101820").pack(pady=(15, 5))
tk.Entry(app, textvariable=folder_path, width=60, bg="#2C3E50", fg="white", insertbackground="white", relief="flat").pack(pady=3)
tk.Button(app, text="Browse...", command=browse_folder, font=button_font, bg=button_color, fg="white", activebackground=highlight_color).pack(pady=5)
tk.Button(app, text="Delete Mods", command=delete_mods, font=button_font, bg=highlight_color, fg="white", height=2, width=25, activebackground="#007ACC").pack(pady=10)

result_text = scrolledtext.ScrolledText(app, width=80, height=20, font=text_font, bg=text_bg, fg=text_fg, insertbackground="white", borderwidth=0, relief="flat")
result_text.pack(pady=10)
result_text.config(state='disabled')

# تذييل
footer_frame = tk.Frame(app, bg="#101820")
footer_frame.pack(pady=8)

tk.Label(footer_frame, text="Created by Ehssandev", font=("Segoe UI", 9), fg="#777", bg="#101820").pack(side="left", padx=10)
tk.Button(footer_frame, text="About", command=show_about, font=("Segoe UI", 9), bg=button_color, fg="white", activebackground=highlight_color).pack(side="right", padx=10)

app.mainloop()