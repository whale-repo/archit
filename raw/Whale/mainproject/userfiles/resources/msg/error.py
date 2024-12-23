import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Whale Error Hunter")
root.geometry("500x300")
root.resizable(False, False)  
root.configure(bg='white')  


logo_image = Image.open("whale.png")
logo_image = logo_image.resize((224, 63), Image.LANCZOS) 
logo = ImageTk.PhotoImage(logo_image)


logo_label = tk.Label(root, image=logo, bg='white')  
logo_label.image = logo 
logo_label.pack(pady=(10, 0)) 


root.mainloop()
