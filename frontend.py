from tkinter import *
import backend

window = Tk()
#window.configure(background = "grey")

#Labels for each entry field
title_label = Label(window, text="Name: ")
title_label.grid(row = 0, column = 0)

author_label = Label(window, text="Team: ")
author_label.grid(row = 0, column = 2)

pages_label = Label(window, text="Jersey Number: ")
pages_label.grid(row = 1, column = 0)

year_label = Label(window, text="MVP Awards: ")
year_label.grid(row = 1, column = 2)

#Entry fields for each label
title_text = StringVar()
title_entry = Entry(window, textvariable = name_text)
title_entry.grid(row = 0, column = 1)

author_text = StringVar()
author_entry = Entry(window, textvariable = team_text)
author_entry.grid(row = 0, column = 3)

pages_text = StringVar()
pages_entry = Entry(window, textvariable = jersey_text)
pages_entry.grid(row = 1, column = 1)

year_text = StringVar()
year_entry = Entry(window, textvariable = mvp_text)
year_entry.grid(row = 1, column = 3)

#Text field where results are published (List Box)
results_box = Listbox(window, height = 8, width = 38)
results_box.grid(row = 3, column = 0, rowspan = 6, columnspan = 2)
scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 3, column = 2, rowspan = 6)
results_box.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = results_box.yview)

#Buttons 
view_button = Button(window, text = "View All", width = 12)
view_button.grid(row = 3, column = 3)

search_button = Button(window, text = "Search Player", width = 12)
search_button.grid(row = 4, column = 3)

update_button = Button(window, text = "Update Player", width = 12)
update_button.grid(row = 5, column = 3)

add_button = Button(window, text = "Add Player", width = 12)
add_button.grid(row = 6, column = 3)

delete_button = Button(window, text = "Delete Player", width = 12)
delete_button.grid(row = 7, column = 3)

close_button = Button(window, text = "Close App", width = 12)
close_button.grid(row = 8, column = 3)

window.mainloop()