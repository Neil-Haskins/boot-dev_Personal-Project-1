from tkinter import *
from tkinter import ttk
import filters


# on change dropdown value
def change_dropdown(string_var):
    print( string_var.get() )

def window(width, height, colors=None):
    if colors is None:
        colors = {
            "bg": "white",
        }
    
    root = Tk()
    root.title("City picker")

    main_frame = ttk.Frame(root, padding=(8,5))
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    month_start_label = ttk.Label(main_frame, text="Start month:")
    month_start_label.grid(column=1, row=1, sticky=(W))

    month_start_select_options = StringVar()
    month_start_select_options.set('jan')
    month_start_select_box = OptionMenu(main_frame, month_start_select_options, *filters.months)
    month_start_select_box.grid(column=2, row=1, sticky=(W))

    # TODO: remove this
    month_start_select_options.trace('w', lambda *args : change_dropdown(month_start_select_options))

    month_end_label = ttk.Label(main_frame, text="End month:")
    month_end_label.grid(column=1, row=2, sticky=(W))

    month_end_select_options = StringVar()
    month_end_select_options.set('jan')
    month_end_select_box = OptionMenu(main_frame, month_end_select_options, *filters.months)
    month_end_select_box.grid(column=2, row=2, sticky=(W))

    # TODO: remove this
    month_end_select_options.trace('w', lambda *args : change_dropdown(month_end_select_options))

    filter_label = ttk.Label(main_frame, text="Filter by:")
    filter_label.grid(column=1, row=3, sticky=(W))

    filter_value_label_text = StringVar()
    filter_value_label_text.set("Filter value:")
    filter_value_label = ttk.Label(main_frame, textvariable=filter_value_label_text)
    filter_value_label.grid(column=1, row=4, sticky=(W))

    filter_value = StringVar()
    filter_value_entry = ttk.Entry(main_frame, textvariable=filter_value)
    filter_value_entry.grid(column=2, row=4, sticky=(W))

    find_button = ttk.Button(main_frame, text='Find cities')
    find_button.grid(column=2, row=5)

    for child in main_frame.winfo_children(): 
        child.grid_configure(padx=2, pady=2)

    # NOTE: https://tkdocs.com/widgets/index.html
    # Ability to add multiple filters
    # Dropdown to choose a filter
    # TODO: Filter on arbitrary parameters
    # Stringvar(s) to enter value(s) for selected filter
    # Get Results button
    # Text display of results

    return root