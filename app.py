import tkinter as tk
from tkinter import ttk
from src.genatic_generator import genatic
from src.hill_climbingS_generator import hill_climbing

class NqueensApp:
    def __init__(self,window):
        self.win = window
        self.win.title('Nqueens')

        # define the deminsion of the app
        self.height=800
        self.s_width=250

        self.win.geometry(f'{self.height + self.s_width}x{self.height}')
        
        # make canva to draw board on
        # and frame for buttons, lables, slides
        self.board = tk.Canvas(window,
                               width=self.height,
                               height=self.height)
        self.board.pack(side="left")

        self.sidebar = ttk.Frame(window,
                                width=self.s_width,
                                height=self.height)
        self.sidebar.pack(side="right")

        self.create_sidebar()
        self.board_size = int(self.size.get())


        # draw board on the canva
        self.create_board()

    def create_board(self):
        self.square_size = self.height // self.board_size
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.board.create_rectangle(col * self.square_size, # x square cooirdnant (start)
                                        row * self.square_size,
                                            (col + 1) * self.square_size, # next x square cooirdnant (end)
                                            (row + 1) * self.square_size,
                                                fill=color,tags="square")
                
    # put queens on positions
    def draw_queen(self,queens_positions):
        for row, col in enumerate(queens_positions):
            offset = self.square_size // 2 # draw on square center
            x = col * self.square_size + offset 
            y = row * self.square_size + offset
            self.board.create_text(x, y,text="♛" ,
                                   font=("Arial",offset , "bold"),
                                   tags='queen')

    def draw(self,queens_pos):
        self.board.delete('queen')
        self.draw_queen(queens_pos)


    def change_board_size(self,event):
        self.board.delete("all")
        self.board_size = int(self.size.get())
        self.create_board()


    def create_sidebar(self):

        self.sp = tk.Label(self.sidebar,text='')
        self.sp.pack()

        tk.Label(self.sidebar,text="board size").pack()


        options = [x for x in range(4,16)]
        self.size = ttk.Combobox(self.sidebar,values = options,state='readonly')
        self.size.pack()
        self.size.set(options[0])
        self.size.bind("<<ComboboxSelected>>",self.change_board_size)

        tk.Label(self.sidebar,text="choose algo").pack()

        button2 = ttk.Button(self.sidebar, text='hillclimbing', command=self.start_hillclimbing)
        button2.pack(pady=10)
        self.hillclimbing_button = button2

        button3 = ttk.Button(self.sidebar, text='genatic', command=self.start_genetic_algorithm)
        button3.pack(pady=10)
        self.genatic_button = button3

        stop_button = ttk.Button(self.sidebar, text='Stop Algorithm', command=self.stop_algorithm)
        stop_button.pack(pady=10)


    def disable_algorithm_buttons(self):
        buttons_to_disable = [self.hillclimbing_button, self.genatic_button]
        for button in buttons_to_disable:
            button.configure(state='disabled')

    def enable_algorithm_buttons(self):
        buttons_to_enable = [self.hillclimbing_button, self.genatic_button]
        for button in buttons_to_enable:
            button.configure(state='normal')

    def start_genetic_algorithm(self):
        self.disable_algorithm_buttons() # Disable the two algorithm buttons
        self.gen = genatic(self.board_size)
        self.stop_flag = True
        self.gen_update_progress()

    def stop_algorithm(self):
        self.enable_algorithm_buttons()
        self.stop_flag = False


    def gen_update_progress(self):
        solution = next(self.gen, None)
        if self.stop_flag == False:
            self.gen = None
            self.sp.config(text='!!! STOPED !!!')
            return
        elif solution is None:
            self.enable_algorithm_buttons()
            return
        else:
            self.sp.config(text=solution[1])
            self.draw(solution[0].pos)
            self.win.after(1, self.gen_update_progress)

    def start_hillclimbing(self):
        self.disable_algorithm_buttons()
        self.hill = hill_climbing(self.board_size)
        self.stop_flag = True
        self.hill_update_progress()

    def hill_update_progress(self):
        state = next(self.hill, None)
        if self.stop_flag == False:
            self.hill = None
            self.sp.config(text='!!! STOPED !!!')
            return
        elif state is None:
            self.enable_algorithm_buttons()
            return
        else:
            self.sp.config(text=state[1])
            self.draw(state[0].pos)
            self.win.after(1, self.hill_update_progress)
        



# if it run as main
if __name__ == "__main__":
    window = tk.Tk()
    app = NqueensApp(window)

    window.mainloop()