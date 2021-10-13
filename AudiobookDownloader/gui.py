from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import os
import platform
from audioplayer import AudioPlayer
import glob
from PIL import Image, ImageTk
from downloadAudioBook import *


root = Tk()
root.title("Gui for Audiobook player")

root.geometry("500x300")

isWindows = True

if os.name == "nt":
    seperator = "\\"
else:
    seperator = "/"
    isWindows = False


paused = False
playerinitiated = False
currentplaying = 0


def add_book():
    book = filedialog.askdirectory(initialdir="", title="Choose a book")
    global currentplaying
    global player
    global playerinitiated
    global paused
    global isWindows
    audiobook_chapter_box.delete(0, END)
    currentplaying = 0
    if playerinitiated:
        player.stop()
        paused = False
        playerinitiated = False
    books = glob.glob(f"{book}/*.mp3")
    if isWindows:
        for book in books:
            if book != ():
                print(book)
                chaptername = book.split("/")[-1][:-4]
                audiobook_chapter_box.insert(END, chaptername)
    else:
        for book in books:
            if book != ():
                print(book)
                chaptername = (
                    book.split(seperator)[-2]
                    + seperator
                    + book.split(seperator)[-1][:-4]
                )
                audiobook_chapter_box.insert(END, chaptername)


def download_book():
    answer = simpledialog.askstring(
        "Input", "What book do you want to download?", parent=root
    )

    if download(answer) is None:
        messagebox.showerror("Error", "Book not found ;_;")
    else:
        messagebox.showinfo("Information", "Book is downloaded.")


def play():
    global player
    global paused
    global playerinitiated
    global currentplaying
    if paused:
        player.resume()
        paused = False

    else:
        if playerinitiated:
            if (player.filename.split(seperator)[-1]) == (
                audiobook_chapter_box.get(ACTIVE).split(seperator)[-1] + ".mp3"
            ):
                currentplaying = audiobook_chapter_box.curselection()[0]
                return
            else:
                chapter = audiobook_chapter_box.get(ACTIVE)
                print(chapter)
                player = AudioPlayer(chapter + ".mp3")
                playerinitiated = True
                player.play()
                currentplaying = audiobook_chapter_box.curselection()[0]

        else:
            chapter = audiobook_chapter_box.get(currentplaying)
            audiobook_chapter_box.selection_set(currentplaying)
            print(chapter)
            player = AudioPlayer(chapter + ".mp3")
            playerinitiated = True
            player.play()


def forward():
    global currentplaying
    global player
    audiobook_chapter_box.selection_clear(currentplaying)
    currentplaying = currentplaying + 1
    audiobook_chapter_box.selection_set(currentplaying)
    chapter = audiobook_chapter_box.get(currentplaying)
    print(chapter)
    print(currentplaying - audiobook_chapter_box.size())
    if currentplaying == audiobook_chapter_box.size():
        currentplaying = currentplaying - 1
        audiobook_chapter_box.selection_set(currentplaying)
        return
    player = AudioPlayer(chapter + ".mp3")
    playerinitiated = True
    player.play()


def backward():
    global currentplaying
    global player
    audiobook_chapter_box.selection_clear(currentplaying)
    currentplaying = currentplaying - 1
    audiobook_chapter_box.selection_set(currentplaying)
    chapter = audiobook_chapter_box.get(currentplaying)
    print(chapter)
    if currentplaying < 0:
        currentplaying = currentplaying + 1
        audiobook_chapter_box.selection_set(currentplaying)
        return
    player = AudioPlayer(chapter + ".mp3")
    playerinitiated = True
    player.play()


def pause():
    global paused
    player.pause()
    paused = True


def stop():
    global paused
    global player
    global currentplaying
    audiobook_chapter_box.delete(0, END)
    player.stop()
    currentplaying = 0


audiobook_chapter_box = Listbox(
    root, bg="black", fg="white", width=70, selectbackground="blue"
)
audiobook_chapter_box.pack(pady=20)


if platform.system() == "Darwin":
    back_btn_img = ImageTk.PhotoImage(Image.open("img/Left.png"))
    forward_btn_img = ImageTk.PhotoImage(Image.open("img/Forward.png"))
    play_btn_img = ImageTk.PhotoImage(Image.open("img/Play.png"))
    pause_btn_img = ImageTk.PhotoImage(Image.open("img/Pause.png"))
    stop_btn_img = ImageTk.PhotoImage(Image.open("img/Stop.png"))


else:
    back_btn_img = PhotoImage(file="img/Left.png")
    forward_btn_img = PhotoImage(file="img/Forward.png")
    play_btn_img = PhotoImage(file="img/Play.png")
    pause_btn_img = PhotoImage(file="img/Pause.png")
    stop_btn_img = PhotoImage(file="img/Stop.png")


controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(
    controls_frame, image=back_btn_img, borderwidth=0, padx=10, command=backward
)
forward_button = Button(
    controls_frame, image=forward_btn_img, borderwidth=0, padx=10, command=forward
)
play_button = Button(
    controls_frame, image=play_btn_img, borderwidth=0, padx=10, command=play
)
pause_button = Button(
    controls_frame, image=pause_btn_img, borderwidth=0, padx=10, command=pause
)
stop_button = Button(
    controls_frame, image=stop_btn_img, borderwidth=0, padx=10, command=stop
)


back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)


my_menu = Menu(root)
root.config(menu=my_menu)

download_book_menu = Menu(my_menu)
add_book_menu = Menu(my_menu)

my_menu.add_cascade(label="Add Audiobook", menu=add_book_menu)
add_book_menu.add_command(label="Add one book to the playlist", command=add_book)

my_menu.add_cascade(label="Download Audiobook", menu=download_book_menu)
download_book_menu.add_command(
    label="Download one book to the playlist", command=download_book
)


root.mainloop()
