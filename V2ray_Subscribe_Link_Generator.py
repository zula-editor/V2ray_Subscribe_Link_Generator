import tkinter as tk
from tkinter import filedialog
import os
import webbrowser

TOKEN_FILE = "token.txt"

def save_token(token):
    with open(TOKEN_FILE, "w") as file:
        file.write(token)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as file:
            return file.read().strip()
    return ""

def clean_input_file(ips_text):
    lines = ips_text.split("\n")
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(cleaned_lines)

def remove_special_characters(text):
    return text.replace("/", "").replace(",", "")

def exit_program():
    root.destroy()

def show_token_entry():
    entry_token.place(x=310, y=110, width=210, height=30)
    token_label.place(x=310, y=85)
    get_token_button.place(x=310, y=150, width=210, height=30)
    get_token_button.configure(bg="#ffe4b2", fg="#000000", font=("Tahoma", 10, "bold"))

def hide_token_entry():
    token = load_token()
    entry_token.delete(0, tk.END)
    entry_token.insert(0, token)
    entry_token.place_forget()
    token_label.place_forget()
    get_token_button.place_forget()

def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("دریافت توکن")
    help_window.geometry("360x175")
    
    help_window.resizable(width=False, height=False)
    
    
    help_text = """
    برای دریافت توکن ربات زیر را استارت کرده
    
    @sansorchi_bezan_gheychi_bot
    
    را برای ربات بفرستید /sub و
    پیام دوم توکن شماست
    
    آن را کپی کرده و وارد کادر کنید
    """
    
    help_label = tk.Label(help_window, text=help_text, padx=90, pady=10, justify="right", anchor="e", font=("Tahoma", 10))
    help_label.place(x=15, y=5)  # تغییر مکان متن پنجره
    
    # Allow copying text
    def copy_text():
        root.clipboard_clear()
        root.clipboard_append("@sansorchi_bezan_gheychi_bot")
        root.update()
        
    copy_button = tk.Button(help_window, text="کپی ایدی ربات", command=copy_text)
    copy_button.place(x=10, y=135)  # تغییر مکان دکمه کپی



def open_zula_editor():
    links = [
        "https://t.me/gheychiamoozesh",
        "https://t.me/Qv2raychannel",
        "https://t.me/Zula_Editor"
    ]
    for link in links:
        webbrowser.open(link)



def q_mode_action():
    result_label.config(text="Q Mode Selected")
    hide_token_entry()

def gheychi_mode_action():
    result_label.config(text="Gheychi Mode Selected")
    token = load_token()
    entry_token.delete(0, tk.END)
    entry_token.insert(0, token)
    show_token_entry()

def start_action():
    mode = result_label.cget("text")
    
    if mode == "Gheychi Mode Selected":
        input_ips = entry_ips.get("1.0", "end-1c")
        token = entry_token.get()

        if not token or not token.isascii():
            result_label.config(text="Error: Invalid Token")
            return

        cleaned_ips_list = clean_input_file(input_ips).split("\n")
        ips_str = ",".join(cleaned_ips_list)
        output_text = f"https://clean.alicivil.workers.dev/?only=14,15,16&ip={ips_str}&url={token}"
        output_filename = "Gheychi_output.txt"
        save_token(token)
    elif mode == "Q Mode Selected":
        input_ips = entry_ips.get("1.0", "end-1c")
        cleaned_ips_list = clean_input_file(input_ips).split("\n")
        ips_str = "/".join(cleaned_ips_list)
        output_text = f"https://test2.sub-channel.workers.dev/{ips_str}"
        output_filename = "Q_output.txt"
    else:
        result_label.config(text="Error: Mode not selected")
        return

    with open(output_filename, "w") as file:
        file.write(output_text)
    result_label.config(text=f"Output saved to {output_filename}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            ips = file.read()
            entry_ips.delete("1.0", "end")
            entry_ips.insert("1.0", ips)



# Create main window
root = tk.Tk()
root.title("Subscribe Link Generator")
root.geometry("530x250")

# Create widgets
q_mode_button = tk.Button(root, text="Q Mode", command=q_mode_action)
gheychi_mode_button = tk.Button(root, text="Gheychi Mode", command=gheychi_mode_action)
get_token_button = tk.Button(root, text="get token", command=show_help)
zula_editor_button = tk.Button(root, text="channels", command=open_zula_editor)  # New button for opening Zula Editor
label_ips = tk.Label(root, text="Enter IP Addresses or click Browse")
entry_ips = tk.Text(root, height=10, width=40)
token_label = tk.Label(root, text="Enter Token (English) :", font=("Helvetica", 10))
entry_token = tk.Entry(root, font=("Helvetica", 10))
browse_button = tk.Button(root, text="Browse", command=browse_file)
start_button = tk.Button(root, text="Start", command=start_action)
exit_button = tk.Button(root, text="Exit", command=exit_program)
result_label = tk.Label(root, text="")

# Arrange widgets
q_mode_button.place(x=310, y=50, width=100, height=30)
q_mode_button.configure(bg="blue", fg="white", font=("Helvetica", 10, "bold"))
gheychi_mode_button.place(x=420, y=50, width=100, height=30)
gheychi_mode_button.configure(bg="orange", fg="white", font=("Helvetica", 10, "bold"))
get_token_button.place(x=310, y=150, width=210, height=30)
zula_editor_button.place(x=310, y=10, width=210, height=30) 
zula_editor_button.configure(bg="gold", fg="black", font=("Helvetica", 11, "bold"))
token_label.place(x=10, y=50)
label_ips.place(x=10, y=15)
entry_ips.place(x=10, y=50, width=290, height=190)
browse_button.place(x=200, y=10, width=100, height=30)
browse_button.configure(bg="yellow", fg="black", font=("Helvetica", 10, "bold"))
start_button.place(x=310, y=190, width=100, height=30)
start_button.configure(bg="green", fg="white", font=("Helvetica", 10, "bold"))
exit_button.place(x=420, y=190, width=100, height=30)
exit_button.configure(bg="red", fg="white", font=("Helvetica", 10, "bold"))
result_label.place(x=310, y=220)

# Load token if available
token = load_token()
entry_token.insert(0, token)

# Hide token entry initially
hide_token_entry()

# Help text for the "دریافت توکن" button
help_text = "برای دریافت توکن ربات زیر رو استارت کرده\n@sansorchi_bezan_gheychi_bot\nو /sub را برای ربات بفرستید\nپیام دوم توکن شماست آن را وارد کنید"

# Disable resizing of the main window
root.resizable(width=False, height=False)

# Start GUI event loop
root.mainloop()