from tkinter import *


window = Tk()

canvas = Canvas(window)
# canvas.place(x=0, y=0, relwidth=0.9, relheight=0.9)  # Strict?
canvas.grid()
# canvas

main_frame = Frame(canvas)
main_frame.place(in_=canvas, relwidth=1, relheight=1)  # Strict?
for i in range(3):
    # Button(main_frame, text=str(i)).pack()
    pass

canvas.create_text(50, 200, text="(c) Copyright the student of M-131 ",
                   anchor='w', angle=30, font=("Times New Roman", 14))

canvas2 = Canvas(main_frame)
canvas2.place(in_=main_frame, x=0, y=0, relwidth=0.9, relheight=0.9)  # Strict?
# canvas2.grid()

canvas2.create_text(10, 10, text="(c) Copyright ... Test ",
                   anchor='w', angle=30, font=("Times New Roman", 14))


window.mainloop()
