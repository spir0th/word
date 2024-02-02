try:
	from tkinter import *
	from tkinter import messagebox, ttk
except Exception as e:
	print(str(e))
	exit(1)

try:
	import os, sys
except Exception as e:
	messagebox.showerror("Failed to initialize", str(e))
	if __name__ == "__main__": exit(2)

try:
	from PIL import ImageTk, Image
except Exception as e:
	messagebox.showerror("Cannot find image graphics library", str(e))
	if __name__ == "__main__": exit(3)

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # Hide pygame welcome message

try:
	import pygame
	has_pygame = True
except Exception as e:
	print("No music, tryna troll without music..")
	has_pygame = False

window: Tk = None

def get_file(name: str) -> str:
	if getattr(sys, "frozen", False):
		return f"{sys._MEIPASS}/{name}"
	else:
		return f"{os.path.dirname(os.path.abspath(__file__))}/{name}"

def init():
	global window
	window = Tk()
	window.title("eh paano kung")
	window.resizable(False, False)
	window.iconphoto(True, PhotoImage(file=get_file("window.png")))

	if has_pygame:
		pygame.mixer.init()

def loop():
	try:
		window.mainloop()
	except KeyboardInterrupt:
		pass

def play_bgm():
	if not has_pygame: return
	pygame.mixer.music.load(get_file("bgm.mp3"))
	pygame.mixer.music.play(loops=69420)

def display():
	# Put a resizable frame on the window
	frame = ttk.Frame(window)
	frame.grid(row=1, column=0, sticky=E+W+N+S)

	# Configure columns and rows for widgets
	window.columnconfigure(0, weight=1)
	window.rowconfigure(1, weight=1)
	frame.rowconfigure(0, weight=1)
	frame.columnconfigure(0, weight=1)

	# Create content from image using Pillow
	content = Image.open(get_file("content.png"))
	content_image = ImageTk.PhotoImage(content)

	label = ttk.Label(frame, image=content_image)
	label.image = content_image
	label.grid(row=0, column=0, sticky=E+W+N+S)

	# Center the window to finalize
	window.eval("tk::PlaceWindow . center")

if __name__ == "__main__":
	init()
	play_bgm()
	display()
	loop()