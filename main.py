from tkinter import *
FONT_NAME = "Courier"


def on_enter_button_click():
    txt = text_str.get(1.0, "end-1c")
    text_str.delete(1.0, "end")
    print(txt)


window = Tk()
window.title("Text-To-Eye-Blink")
window.config(padx=100, pady=50)

canvas = Canvas(width=500, height=400, highlightthickness=0)
canvas.grid(row=1, column=1)

text_canvas = canvas.create_text(250, 75, text="Enter a text: ", font=(FONT_NAME, 32, "bold"))
heading = Label(text="Text to eye blink", font=(FONT_NAME, 50, "bold"))
heading.grid(row=0, column=1)

# text_str = Entry(width=50)
text_str = Text(window, height=10, width=60, font=(FONT_NAME, 12, "normal"))
text_str.grid(row=1, column=0, columnspan=2)
text_str.focus_set()

enter_button = Button(text="Enter", background='grey',  highlightthickness=0, height=3, width=15,
                      font=(FONT_NAME, 12, "bold"), command=on_enter_button_click)
enter_button.grid(row=2, column=0, columnspan=2)


window.mainloop()