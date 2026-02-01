import tkinter  as tk
from tkinter import Entry,Label,Button
import webbrowser

root= tk.Tk()
root.title(" YOUR AI ASSISTANT ")
root.geometry("700x500")

root.configure(bg='#1e1e1e')

def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
        query=entry.get()
        url=f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

def search_instagram():
        username=entry.get().replace('@', '')
        url=f"https://www.instagram.com/{username}/"
        webbrowser.open(url)
 
 
def search_linkden():
    username=entry.get().replace('', '')
    url=f"https://www.linkden.com/ln/{username}/"
    webbrowser.open(url)

def search_github():
    query=entry.get()
    if query.lower().startswith("user "):
         username = query.split("user ", 1)[1].strip()
         url = f"https://github.com/{username}"
    else:
        url = f"https://github.com/search?q={query}"
        webbrowser.open(url)

Label(root,
      text="YOUR AI ASSISTANT ",
      font=("segoe UI",20, "bold"),
      fg="#00ffcc",
      bg="#1e1e1e"
      ).pack(pady=20)

Label(root,
      text="Type your query or username below: ",
      font=("segoe UI",12),
      fg="white",
      bg="#1e1e1e"
      ).pack()
entry =Entry(root,width=60,font=("segoe UI",14))
entry.pack(pady=10)

Button(root,text="Search on youtube",command=search_youtube).pack(pady=5)
Button(root,text="Search on Google",command=search_google).pack(pady=5)
Button(root,text="Search on Instagram",command=search_instagram).pack(pady=5)
Button(root,text="Search on Linkden",command=search_linkden).pack(pady=5)
Button(root,text="Search on Github",command=search_github).pack(pady=5)

Label(root,text="Thanks for visiting...",font="arial",
fg="white",     
bg="black"
).pack( pady=70)

root.mainloop()

