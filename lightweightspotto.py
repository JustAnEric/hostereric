try:
  import os, webview
  from tkinter import messagebox
except: return print("Nessacery packages aren't installed. Please run the install script again.")
if messagebox.askokcancel("
                      "Want to launch Spotify? Lightweight Spotify may take up a few bytes of your disk.")
webview.create_window("", "").start()
