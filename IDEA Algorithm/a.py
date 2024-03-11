import tkinter as tk
from tkinter import messagebox

def string_to_binary(string):
    return ' '.join(format(ord(c), '08b') for c in string)

def simple_encrypt(message, key):
  # Transform the message and key into a list of character codes
  message_codes = [ord(c) for c in message]
  key_codes = [ord(c) for c in key]

  # Simple "encryption" by adding key character codes to message character codes
  encrypted_codes = [(m + k % 256) for m, k in zip(message_codes, key_codes * (len(message_codes) // len(key_codes) + 1))]

  # Convert codes back to characters
  encrypted_message = ''.join(chr(c % 256) for c in encrypted_codes)

  return encrypted_message

def simple_decrypt(encrypted_message, key):
  # Transform the encrypted message and key into a list of character codes
  encrypted_codes = [ord(c) for c in encrypted_message]
  key_codes = [ord(c) for c in key]

  # Simple "decryption" by subtracting key character codes from encrypted character codes
  decrypted_codes = [(e - k % 256) for e, k in zip(encrypted_codes, key_codes * (len(encrypted_codes) // len(key_codes) + 1))]

  # Convert codes back to characters
  decrypted_message = ''.join(chr(c % 256) for c in decrypted_codes)

  return decrypted_message

def perform_operation():
  message = entry_message.get()
  key = entry_key.get()
  operation = var.get()

  if not key.strip():
    messagebox.showerror("Error", "Key cannot be empty.")
    return

  if operation == 'Encrypt':
    encrypted = simple_encrypt(message, key)
    entry_output.delete(0, tk.END)
    entry_output.insert(0, encrypted)
  elif operation == 'Decrypt':
    decrypted = simple_decrypt(message, key)
    entry_output.delete(0, tk.END)
    entry_output.insert(0, decrypted)

def show_help():
  messagebox.showinfo("Help", "This application allows you to encrypt or decrypt a message using a key. Enter your message and key, select the operation (Encrypt or Decrypt), and click 'Perform Operation'.")

def exit_app():
  root.destroy()

# User Interface
root = tk.Tk()
root.title("IDEA Cryptography")

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

# Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu)
menu.add_command(label="Help", command=show_help)
menu.add_separator()
menu.add_command(label="Exit", command=exit_app)

# Message Entry
tk.Label(root, text="Message:", font=("Arial", 12)).grid(row=0, column=0, sticky='w', padx=10, pady=5)
entry_message = tk.Entry(root, font=("Arial", 12))
entry_message.grid(row=0, column=1, padx=10, pady=5)

# Key Entry
tk.Label(root, text="Key:", font=("Arial", 12)).grid(row=1, column=0, sticky='w', padx=10, pady=5)
entry_key = tk.Entry(root, font=("Arial", 12))
entry_key.grid(row=1, column=1, padx=10, pady=5)

# Operation Selection
var = tk.StringVar(root, "Encrypt")
tk.Label(root, text="Operation:", font=("Arial", 12)).grid(row=2, column=0, sticky='w', padx=10, pady=5)
tk.Radiobutton(root, text="Encrypt", variable=var, value="Encrypt", font=("Arial", 12)).grid(row=2, column=1, sticky='w', padx=10, pady=5)
tk.Radiobutton(root, text="Decrypt", variable=var, value="Decrypt", font=("Arial", 12)).grid(row=2, column=1, sticky='e', padx=10, pady=5)

# Output Entry
tk.Label(root, text="Output:", font=("Arial", 12)).grid(row=3, column=0, sticky='w', padx=10, pady=5)
entry_output = tk.Entry(root, font=("Arial", 12))
entry_output.grid(row=3, column=1, padx=10, pady=5)

# Button
tk.Button(root, text="Perform Operation", font=("Arial", 12), command=perform_operation).grid(row=4, column=0, columnspan=2, pady=15)

root.mainloop()
