from tkinter import ttk
import tkinter as tk
from services.running_service import app_engine


class MenuView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._dataresolution_box = None
        self._seed_box = None
        self._start_box = None
        self._goal_box = None
        self._octaves_box = None
        self._amplitudes_box = None
        self._run_dijkstra_box = 1
        self._run_a_star_box = 1
        self._run_fringe_search_box = 1
        self._draw_results = 1

        self._init()

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(
            master=self._frame,
            text="Pathfinder",
            font=("Noto Mono", 30, 'bold')
        )
        header.pack(anchor='n', pady=10)
        notice_lable = ttk.Label(master=self._frame,
                                 text="Placeholders give guidence to formating of the inputs.", foreground='blue'
                                 )
        notice_lable.pack(anchor='w')
        notice_lable = ttk.Label(master=self._frame,
                                 text="If they are left empy the placeholders will be used", foreground='blue')
        notice_lable.pack(anchor='w')
        notice_lable = ttk.Label(master=self._frame,
                                 text="Start and goal should be given as ints seperated by commas. ", foreground='blue'
                                 )
        notice_lable.pack(anchor='w')
        notice_lable = ttk.Label(master=self._frame,
                                 text="Data_resolution and random_seed should be given as ints.", foreground='blue'
                                 )
        notice_lable.pack(anchor='w')
        notice_lable = ttk.Label(master=self._frame,
                                 text="Amplitudes and octaves are lists of floats and ints respectively seperated by commas.", foreground='blue'
                                 )

        notice_lable.pack(anchor='w')
        self._dataresolution_box = self._draw_text_box("Dataresolution", "75")
        self._seed_box = self._draw_text_box("Random seed", "rnd")
        self._start_box = self._draw_text_box("Start", "rnd, rnd")
        self._goal_box = self._draw_text_box("Goal", "rnd, rnd")

        notice_lable = ttk.Label(master=self._frame,
                                 text="Octaves and amplitudes must have the same number of variables.", foreground='red'
                                 )
        notice_lable.pack(anchor='w', pady=5)
        self._octaves_box = self._draw_text_box("Octaves", "1, 5, 10")
        self._amplitudes_box = self._draw_text_box(
            "Amplitudes", "1, 0.2, 0.05")

        self._run_dijkstra_box = self._draw_check_box("run dijkstra")
        self._run_a_star_box = self._draw_check_box("run = a_star")
        self._run_fringe_search_box = self._draw_check_box("run fringe_search")
        self._draw_results = self._draw_check_box("run draw_results")

        start_button = ttk.Button(
            master=self._frame,
            text="Start",
            command=self._start_command
        )

        start_button.pack()

    def _draw_text_box(self, lable_text, placeholder_text):
        '''
        Draws text box in frame with given placeholder text and lable text.
        The ttk.Entry object will be returned.
        '''
        box_frame = ttk.Frame(master=self._frame)
        lable_obj = ttk.Label(master=box_frame, text=lable_text)
        box_variable = ttk.Entry(master=box_frame, foreground='gray')

        def on_entry_click(event):
            if box_variable.get() == placeholder_text:
                box_variable.delete(0, 'end')
                box_variable.configure(foreground="black")

        def on_focus_out(event):
            if box_variable.get() == "":
                box_variable.insert(0, placeholder_text)
                box_variable.configure(foreground="gray")

        box_variable.insert(0, placeholder_text)

        box_variable.bind("<FocusIn>", on_entry_click)
        box_variable.bind("<FocusOut>", on_focus_out)

        lable_obj.pack(anchor='nw')
        box_variable.pack(anchor='ne')

        box_frame.pack(anchor='w', pady=5)
        return box_variable

    def _draw_check_box(self, lable_text):
        '''
        Draws a checkmark box. The initial value and the variable it controls can be set via variable.
        '''
        v = tk.IntVar(self._frame, 1)
        check_box = ttk.Checkbutton(
            master=self._frame, text=lable_text, variable=v)
        check_box.pack(padx=5, pady=4, anchor='w')

        return v

    def _start_command(self):
        app_engine.data_resolution = int(self._dataresolution_box.get())
        seed = self._seed_box.get()
        if not (seed == "rnd" or not seed.split()[0].isnumeric()):
            app_engine.random_seed = int(seed.split()[0])
        start = self._start_box.get()
        if not start == "rnd, rnd":
            app_engine.set_start_from_string(start)
        goal = self._goal_box.get()
        if not goal == "rnd, rnd":
            app_engine.set_goal_from_string(goal)
        app_engine.set_octaves_from_string(self._octaves_box.get())
        app_engine.set_amplitudes_from_string(self._amplitudes_box.get())
        app_engine.run_dijkstra = self._run_dijkstra_box.get()
        app_engine.run_a_star = self._run_a_star_box.get()
        app_engine.run_fringe_search = self._run_fringe_search_box.get()
        app_engine.draw_results = self._draw_results.get()
        self._root.destroy()
        app_engine.init_empty_values()
        app_engine.execute()
