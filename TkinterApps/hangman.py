from tkinter import *
from tkinter import ttk
import random

# create the visuals
class test_gui():
    def __init__(self):
        def toggle_button(letter):
            buttons_dict = {'A': self.letter_1, 'B': self.letter_2, 'C': self.letter_3, 'D': self.letter_4,
                            'E': self.letter_5, 'F': self.letter_6, 'G': self.letter_7, 'H': self.letter_8,
                            'I': self.letter_9, 'J': self.letter_10, 'K': self.letter_11, 'L': self.letter_12,
                            'M': self.letter_13, 'N': self.letter_14, 'O': self.letter_15, 'P': self.letter_16,
                            'Q': self.letter_17, 'R': self.letter_18, 'S': self.letter_19, 'T': self.letter_20,
                            'U': self.letter_21, 'V': self.letter_22, 'W': self.letter_23, 'X': self.letter_24,
                            'Y': self.letter_25, 'Z': self.letter_26,}
            if letter in self.word:
                for index, char in enumerate(self.word):
                    if letter == char:
                        self.letter_list_copy[index] = char
                        self.displayed_word = ' '.join(self.letter_list_copy)
                        self.disp_word.config(text=self.displayed_word)
            else:
                self.lives -= 1
                self.img.config(image=images[self.lives])
                self.text_counter = f'Lives left: {self.lives}'
                self.counter.config(text=self.text_counter)
                if self.lives == 0:
                    self.exit_text = ttk.Label(self.mainframe, text='You lost the game!', font=('Helvetica', '15'))
                    self.exit_text.grid(column=10, row=12, rowspan=3, sticky='nse')
                    self.exit_btn = Button(self.mainframe, text="Close", command=self.root.destroy)
                    self.exit_btn.grid(column=10, row=16, pady=5)

            if '_' not in self.displayed_word:
                    self.win_text = ttk.Label(self.mainframe, text='You WON!!', font=('Helvetica', '15'))
                    self.win_text.grid(column=10, row=12, rowspan=3, sticky='nse')
                    self.win_btn = Button(self.mainframe, text="Exit", command=self.root.destroy)
                    self.win_btn.grid(column=10, row=16, pady=5)

            buttons_dict[letter]['state'] = DISABLED

        # ACCEPTS WORDS IN UPPERCASE, WRITTEN ON SEPARATE LINES
        with open('tkwords.txt', 'r') as words:
            self.word_list = words.read().splitlines()

        # select random word and count its length and chars
        self.word = random.choice(self.word_list)
        self.letter_list = [letter for letter in self.word]
        self.letter_list_copy = self.letter_list.copy()
        self.word_length = len(self.letter_list)
        self.lives = 6

        # generate the word with only 1st and last letter shown
        for letter in range(1, self.word_length - 1):
            self.letter_list_copy[letter] = '_'

        # Create main frame
        self.root=Tk()
        self.root.title("Hangman Game")
        self.root.geometry('600x400')

        self.mainframe = ttk.Frame(self.root, padding="3 3 6 6")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.title = ttk.Label(self.mainframe, text='Hangman Game', font=('Helvetica', '10')).grid(columnspan=6, row=1, sticky='nse')

        self.displayed_word = ' '.join(self.letter_list_copy)
        self.text = self.displayed_word
        self.disp_word = ttk.Label(self.mainframe, text=self.text, font=('Helvetica', '15'))
        self.disp_word.grid(columnspan=6, row=3, rowspan=2, sticky='nse')

        # create the image files
        self.image0 = PhotoImage(file='Hangman-0.png')
        self.image1 = PhotoImage(file='Hangman-1.png')
        self.image2 = PhotoImage(file='Hangman-2.png')
        self.image3 = PhotoImage(file='Hangman-3.png')
        self.image4 = PhotoImage(file='Hangman-4.png')
        self.image5 = PhotoImage(file='Hangman-5.png')
        self.image6 = PhotoImage(file='Hangman-6.png')

        images = {5: self.image1,
                  4: self.image2,
                  3: self.image3,
                  2: self.image4,
                  1: self.image5,
                  0: self.image6}
        self.img = ttk.Label(self.mainframe, image=self.image0)
        self.img.grid(row=3, column=10, sticky='w')

        self.text_counter = f'Lives left: {self.lives}'
        self.counter = ttk.Label(self.mainframe, text=self.text_counter)
        self.counter.grid(row=10, columnspan=10, sticky='nse')

        # Don't judge my hardcoding, please :D..
        self.letter_1 = ttk.Button(self.mainframe, text="A", command=lambda:toggle_button('A'), width=7)
        self.letter_1.grid(column=1, row=5, sticky=E)
        self.letter_2 = ttk.Button(self.mainframe, text="B", command=lambda:toggle_button('B'), width=7)
        self.letter_2.grid(column=2, row=5, sticky=E)
        self.letter_3 = ttk.Button(self.mainframe, text="C", command=lambda:toggle_button('C'), width=7)
        self.letter_3.grid(column=3, row=5, sticky=E)
        self.letter_4 = ttk.Button(self.mainframe, text="D", command=lambda:toggle_button('D'), width=7)
        self.letter_4.grid(column=4, row=5, sticky=E)
        self.letter_5 = ttk.Button(self.mainframe, text="E", command=lambda:toggle_button('E'), width=7)
        self.letter_5.grid(column=5, row=5, sticky=E)
        self.letter_6 = ttk.Button(self.mainframe, text="F", command=lambda:toggle_button('F'), width=7)
        self.letter_6.grid(column=6, row=5, sticky=E)
        self.letter_7 = ttk.Button(self.mainframe, text="G", command=lambda:toggle_button('G'), width=7)
        self.letter_7.grid(column=7, row=5, sticky=E)
        self.letter_8 = ttk.Button(self.mainframe, text="H", command=lambda:toggle_button('H'), width=7)
        self.letter_8.grid(column=8, row=5, sticky=E)
        self.letter_9 = ttk.Button(self.mainframe, text="I", command=lambda:toggle_button('I'), width=7)
        self.letter_9.grid(column=1, row=6, sticky=E)
        self.letter_10 = ttk.Button(self.mainframe, text="J", command=lambda:toggle_button('J'), width=7)
        self.letter_10.grid(column=2, row=6, sticky=E)
        self.letter_11 = ttk.Button(self.mainframe, text="K", command=lambda:toggle_button('K'), width=7)
        self.letter_11.grid(column=3, row=6, sticky=E)
        self.letter_12 = ttk.Button(self.mainframe, text="L", command=lambda:toggle_button('L'), width=7)
        self.letter_12.grid(column=4, row=6, sticky=E)
        self.letter_13 = ttk.Button(self.mainframe, text="M", command=lambda:toggle_button('M'), width=7)
        self.letter_13.grid(column=5, row=6, sticky=E)
        self.letter_14 = ttk.Button(self.mainframe, text="N", command=lambda:toggle_button('N'), width=7)
        self.letter_14.grid(column=6, row=6, sticky=E)
        self.letter_15 = ttk.Button(self.mainframe, text="O", command=lambda:toggle_button('O'), width=7)
        self.letter_15.grid(column=7, row=6, sticky=E)
        self.letter_16 = ttk.Button(self.mainframe, text="P", command=lambda:toggle_button('P'), width=7)
        self.letter_16.grid(column=8, row=6, sticky=E)
        self.letter_17 = ttk.Button(self.mainframe, text="Q", command=lambda:toggle_button('Q'), width=7)
        self.letter_17.grid(column=1, row=7, sticky=E)
        self.letter_18 = ttk.Button(self.mainframe, text="R", command=lambda:toggle_button('R'), width=7)
        self.letter_18.grid(column=2, row=7, sticky=E)
        self.letter_19 = ttk.Button(self.mainframe, text="S", command=lambda:toggle_button('S'), width=7)
        self.letter_19.grid(column=3, row=7, sticky=E)
        self.letter_20 = ttk.Button(self.mainframe, text="T", command=lambda:toggle_button('T'), width=7)
        self.letter_20.grid(column=4, row=7, sticky=E)
        self.letter_21 = ttk.Button(self.mainframe, text="U", command=lambda:toggle_button('U'), width=7)
        self.letter_21.grid(column=5, row=7, sticky=E)
        self.letter_22 = ttk.Button(self.mainframe, text="V", command=lambda:toggle_button('V'), width=7)
        self.letter_22.grid(column=6, row=7, sticky=E)
        self.letter_23 = ttk.Button(self.mainframe, text="W", command=lambda:toggle_button('W'), width=7)
        self.letter_23.grid(column=7, row=7, sticky=E)
        self.letter_24 = ttk.Button(self.mainframe, text="X", command=lambda:toggle_button('X'), width=7)
        self.letter_24.grid(column=8, row=7, sticky=E)
        self.letter_25 = ttk.Button(self.mainframe, text="Y", command=lambda:toggle_button('Y'), width=7)
        self.letter_25.grid(column=4, row=9, sticky=E)
        self.letter_26 = ttk.Button(self.mainframe, text="Z", command=lambda:toggle_button('Z'), width=7)
        self.letter_26.grid(column=5, row=9, sticky=E)


test = test_gui()
test.root.mainloop()