from tkinter import Frame, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib import patheffects
from dashboard import Dashboard
from constants import COLOR_BRITE, COLOR_DARK, COLOR_DARKEST, COLOR_LITE, COLOR_GRID, COLORS


class DashboardPage(Frame):
    def __init__(self, root, loader):
        Frame.__init__(self, root, bg=COLOR_DARK)
        self._root = root
        self._loader = loader
        dboard = Dashboard(**self._loader.load())
        label = ttk.Label(master=self, text=dboard.title, font=("Arial", 25),
                              background=COLOR_DARK, foreground='white')
        label.grid(row=0, column=1, padx=100, pady=10)
        canvas = self.draw_layout(dboard.layout['y'], dboard.layout['x'], dboard.load_all(), self)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 1, column = 0, columnspan=3, sticky ="nsew")

    def draw_graph(self, axl, data):
        """Draw one graph widget"""
        axl.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        axl.grid(color=COLOR_GRID)
        [x.set_color(COLOR_LITE) for x in [
            axl.spines['top'], axl.spines['bottom'], axl.spines['left'], axl.spines['right']]]

        if data is not None:
            axl.set_title(data['title'], fontdict={'color':'white','size':10})
            smallest = min([min(plot[1]) for plot in data['plots'].values()])

            color_gen = (color for color in COLORS)

            for title, plot in data['plots'].items():
                color = next(color_gen, None)
                axl.plot(plot[0], plot[1], marker='', markersize=1.0, linewidth=0.75,
                         path_effects=[patheffects.Normal()], label=title, color=color)
                [axl.plot(plot[0], plot[1], marker='', alpha=0.025, linewidth=2+1.15*n, color=color) for n in range(8)]
                axl.fill_between(x=plot[0], y1=plot[1], y2=smallest, alpha=0.035, color=color)
            axl.legend(loc='lower center', 
                       #bbox_to_anchor=(0.5, -0.35),
                       labelcolor='white', facecolor='black',
                       framealpha=0.5, edgecolor='none', ncol=3)
        return axl

    def draw_layout(self, rows, cols, graphdata, master):
        """Uses a generator to yield one graph at a time to put into the layout"""
        fig = Figure(figsize=(12, 6), dpi=100,
                     facecolor=COLOR_DARK, edgecolor=COLOR_GRID, linewidth=1.0)
        gridspec = fig.add_gridspec(rows, cols, left=0.075, right=0.925, top=0.925, bottom=0.075, wspace=0.20, hspace=0.35)
        graph_gen = (graph for graph in graphdata)
        xformatter = mdates.DateFormatter('%H:%M')

        for y in range(rows):
            for x in range(cols):
                axl = fig.add_subplot(gridspec[y, x], frameon=True, facecolor=COLOR_DARKEST)
                self.draw_graph(axl, next(graph_gen, None))
                axl.xaxis.set_major_formatter(xformatter)
        return FigureCanvasTkAgg(fig, master)
