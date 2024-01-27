from tkinter import *
from tkinter import ttk
import filters

from dev import nicely_print


# on change dropdown value
def change_dropdown(string_var):
    print( string_var.get() )

class Window:
    def __init__(self, width, height, cities_dict, colors=None):
        if colors is None:
            colors = {
                "bg": "white",
        }
        self._colors = colors
        self._cities_dict = cities_dict
    
        self.__root = Tk()
        self.__root.title("City picker")
        self.__root.geometry(f'{width}x{height}')
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        self.__main_frame = ttk.Frame(self.__root, padding=(8,5))
        self.__main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.__start_month = FilterSet(self.__main_frame, 1, "Start month:", filters.months)
        self.__start_month.set('Select month')
        self.__end_month = FilterSet(self.__main_frame, 2, "End month:", filters.months)
        self.__end_month.set('Select month')
        self.__filter_by = FilterSet(self.__main_frame, 3, "Filter by:", filters.filters_dict.keys())
        self.__filter_by.set('Select filter')

        self.__filter_value_label_text = StringVar()
        self.__filter_value_label_text.set("Filter value:")
        self.__filter_value_label = ttk.Label(self.__main_frame, textvariable=self.__filter_value_label_text)
        self.__filter_value_label.grid(column=1, row=4, sticky=(W, E))

        self.__filter_by.trace('w', lambda *args : self.__filter_value_label_text.set(f'{self.__filter_by.get()} = '))

        self.__filter_value = StringVar()
        self.__filter_value_entry = ttk.Entry(self.__main_frame, textvariable=self.__filter_value, validate='all', validatecommand=(self.validate_entry, '%P'))
        self.__filter_value_entry.grid(column=2, row=4, sticky=(W))

        self.__find_button = ttk.Button(self.__main_frame, text='Find cities', command=self.on_click_find)
        self.__find_button.grid(column=2, row=5)



        for child in self.__main_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=3)
        
        self.__root.mainloop()

    def on_click_find(self):
        filter_name = self.__filter_by.get()
        value = float(self.__filter_value.get())
        use_filter = filters.filters_dict[filter_name]
        start_month = self.__start_month.get()
        end_month = self.__end_month.get()
        months_dict = filters.filter_months(self._cities_dict, start_month, end_month)
        result = use_filter(months_dict, value)
        nicely_print(result)
    
    def validate_entry(self, P):
        return str.isdigit(P) or P == ""



# NOTE: https://tkdocs.com/widgets/index.html
# Ability to add multiple filters
# Dropdown to choose a filter
# TODO: Filter on arbitrary parameters
# Stringvar(s) to enter value(s) for selected filter
# Get Results button
# Text display of results

class FilterSet:
    def __init__(self, parent, row, label_text, options_set):
        label = ttk.Label(parent, text=label_text)
        label.grid(column=1, row=row, sticky=(W))

        self._select_options = StringVar()
        self._select_options.set('')
        select_box = OptionMenu(
            parent,
            self._select_options,
            *options_set
            )
        select_box.grid(column=2, row=row, sticky=(W, E))
    
    def get(self):
        return self._select_options.get()
    
    def set(self, *args):
        return self._select_options.set(*args)

    def trace(self, *args):
        return self._select_options.trace(*args)