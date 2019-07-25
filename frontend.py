from tkinter import *
import backend

def view_players():
    results_box.delete(0, END)
    for data in backend.view():
        results_box.insert(END, data)

def search_players():
    results_box.delete(0, END)
    for data in backend.search(name_text.get(), team_text.get(), jersey_text.get(), mvp_text.get()):
        results_box.insert(END, data)
    
def add_player():
    backend.insert(name_text.get(), team_text.get(), jersey_text.get(), mvp_text.get())
    results_box.delete(0, END)
    results_box.insert(END, (name_text.get(), team_text.get(), jersey_text.get(), mvp_text.get()))

window = Tk()
#window.configure(background = "grey")

#Labels for each entry field
name_label = Label(window, text="Name: ")
name_label.grid(row = 0, column = 0)

team_label = Label(window, text="Team: ")
team_label.grid(row = 0, column = 2)

jersey_label = Label(window, text="Jersey Number: ")
jersey_label.grid(row = 1, column = 0)

mvp_label = Label(window, text="MVP Awards: ")
mvp_label.grid(row = 1, column = 2)

#Entry fields for each label
name_text = StringVar()
name_entry = Entry(window, textvariable = name_text)
name_entry.grid(row = 0, column = 1)

team_text = StringVar()
team_entry = Entry(window, textvariable = team_text)
team_entry.grid(row = 0, column = 3)

jersey_text = StringVar()
jersey_entry = Entry(window, textvariable = jersey_text)
jersey_entry.grid(row = 1, column = 1)

mvp_text = StringVar()
mvp_entry = Entry(window, textvariable = mvp_text)
mvp_entry.grid(row = 1, column = 3)

#Text field where results are published (List Box)
results_box = Listbox(window, height = 8, width = 38)
results_box.grid(row = 3, column = 0, rowspan = 6, columnspan = 2)
scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 3, column = 2, rowspan = 6)
results_box.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = results_box.yview)

#Buttons 
view_button = Button(window, text = "View All", width = 12, command = view_players)
view_button.grid(row = 3, column = 3)

search_button = Button(window, text = "Search Player", width = 12, command = search_players)
search_button.grid(row = 4, column = 3)

update_button = Button(window, text = "Update Player", width = 12)
update_button.grid(row = 5, column = 3)

add_button = Button(window, text = "Add Player", width = 12, command = add_player)
add_button.grid(row = 6, column = 3)

delete_button = Button(window, text = "Delete Player", width = 12)
delete_button.grid(row = 7, column = 3)

close_button = Button(window, text = "Close App", width = 12)
close_button.grid(row = 8, column = 3)

window.mainloop()