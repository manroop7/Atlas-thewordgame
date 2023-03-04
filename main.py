import tkinter as tk
import pycountry

class Place(tk.Entry):
    def __init__(self, master=None, placeholder="What's on your mind?", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_entry_click)
        self.bind("<FocusOut>", self.on_focus_out)

        self.on_focus_out(None)

    def on_entry_click(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color


def search_country(event):
    search_char = search_entry.get().upper()
    matching_countries = [country.name for country in pycountry.countries if country.name.upper().startswith(search_char)]
    result_list.delete(0, tk.END)
    for country in matching_countries:
        result_list.insert(tk.END, country)



window = tk.Tk()
window.title('ATLAS - The Word Game')
# Calculate the position of the window to be centered
width = 400
height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

search_label = tk.Label(window, text='Enter below', font=("Arial", 14), bg='black', fg='White')
search_label.pack()
search_entry = Place(window, width=50, placeholder="What's on your mind?", bg='black', font='green',fg='white')
search_entry.pack(pady=15, padx=10)

result_frame = tk.Frame(window, width=20, bg='green')
result_frame.pack(pady=10)

result_scrollbar = tk.Scrollbar(result_frame)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_list = tk.Listbox(result_frame, width=30, yscrollcommand=result_scrollbar.set, font=('Helvetica', 12),fg='white',bg='black')
result_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

result_scrollbar.config(command=result_list.yview)

search_entry.bind("<KeyRelease>", search_country)

window.configure(bg='black')

# Add a canvas widget to the window
canvas = tk.Canvas(window, bg='black', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Create a white line on the left edge of the canvas
line_id = canvas.create_line(0, 0, 0, canvas.winfo_height(), fill='white')

def update_line():
    # Get the current position of the line
    x1, y1, x2, y2 = canvas.coords(line_id)
    # Move the line 1 pixel to the right
    canvas.coords(line_id, x1 + 1, y1, x2 + 1, y2)
    # Schedule this function to be called again after 10 milliseconds
    window.after(10, update_line)



update_line()

window.mainloop()
