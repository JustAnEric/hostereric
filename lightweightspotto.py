import sys
try:
  import os, webview
  from tkinter import messagebox
except: print("Nessacery packages aren't installed. Please run the install script again."); sys.exit(1)
if messagebox.askokcancel("Spotify",
                      "Want to launch Spotify? Lightweight Spotify may take up a few bytes of your disk."):
  webview.create_window("Spotify", "https://open.spotify.com/__noul__").start()
