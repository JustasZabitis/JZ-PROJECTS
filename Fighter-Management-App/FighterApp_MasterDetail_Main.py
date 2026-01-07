import sqlite3
from tkinter import *
from FighterApp_Display import *

#============================================================
# Color Palette
BG_MAIN   = "#fef9e7"
BG_FRAME  = "#f2f5e0"
COLOR_LABEL  = "#2f3640"
ENTRY_BG  = "#fefefe"

NAV_COLOR = "#f5cd79"
DATA_COLOR = "#63cdda"
ACTION_COLOR = "#e77f67"
DISPLAY_ALL_COLOR = "#78e08f"
NATION_COLOR = "#9b59b6"
WINS_COLOR = "#f6b93b"
SEARCH_COLOR = "#60a3bc"

#============================================================
window = Tk()
window.geometry("900x580")
window.title("Fighter Application")
window.configure(bg=BG_MAIN)

#============================================================
# General Methods to Display Data


def refreshListbox():
    listbox.delete(0, END)
    cur.execute("select Fighter_Name from Fighter order by Fighter_Name")
    for (name,) in cur.fetchall():
        listbox.insert(END, name)

def display(index):
    global current
    cur.execute("select * from Fighter order by Fighter_Name")
    fighters = cur.fetchall()

    # If there are no fighters in the database, stop and reset selection
    if not fighters:
        current = -1
        return

    # To Keep index value within valid range (avoid IndexError)
    if index < 0: index = 0
    if index >= len(fighters): index = len(fighters)-1

    current = index
    row = fighters[index]

    # Clear the fighter entry and insert the selected fighter's info
    entry_name.delete(0, END); entry_name.insert(END, row[0])
    entry_nat.delete(0, END); entry_nat.insert(END, row[1])
    entry_mgr.delete(0, END); entry_mgr.insert(END, row[2])
    entry_gym.delete(0, END); entry_gym.insert(END, row[3])
    entry_wins.delete(0, END); entry_wins.insert(END, row[4])
    entry_losses.delete(0, END); entry_losses.insert(END, row[5])
    entry_fights.delete(0, END); entry_fights.insert(END, row[6])
    var_retired.set(1 if row[7] else 0)


def onListSelect(event):
    try:

        # Get the index of the selected item in the listbox
        idx = listbox.curselection()[0]

        # Display the fighter's details on the right side of the form (table)
        display(idx)
    except:
        pass


#============================================================
# Database setup
con = sqlite3.connect("fighters.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE Fighter(Fighter_Name TEXT, Nationality TEXT, Manager TEXT, Training_Gym TEXT, Wins INTEGER, Losses INTEGER, Fights_Fought INTEGER, Retired BOOLEAN)")
    data = [
        ("Jon Jones", "USA", "Richard Schaefer", "Jackson Wink MMA", 27, 1, 28, False),
        ("Khabib Nurmagomedov", "Russia", "Ali Abdelaziz", "American Kickboxing Academy", 29, 0, 29, True),
        ("Conor McGregor", "Ireland", "Audie Attar", "SBG Ireland", 22, 6, 28, False),
        ("Amanda Nunes", "Brazil", "Dan Lambert", "American Top Team", 23, 5, 28, True),
        ("Israel Adesanya", "New Zealand", "Tim Simpson", "City Kickboxing", 24, 3, 27, False),
        ("Stipe Miocic", "USA", "Jim Walter", "Strong Style MMA", 20, 4, 24, False),
        ("Valentina Shevchenko", "Kyrgyzstan", "Roger Allen", "Tiger Muay Thai", 24, 4, 28, False),
        ("Georges St-Pierre", "Canada", "Rodolphe Beaulieu", "Tristar Gym", 26, 2, 28, True)
    ]
    cur.executemany("INSERT INTO Fighter VALUES(?,?,?,?,?,?,?,?)", data)
    con.commit()
except:
    print("Fighter table already exists")


#========= Definitions ============================


# Insert Fighter
def insertCmd():
    insert_win = Toplevel(window)
    insert_win.title("Add New Fighter")
    insert_win.geometry("420x380")
    insert_win.configure(bg=BG_FRAME)

    # Title bar
    Label(insert_win, text="Add New Fighter", bg="#e1b12c", fg="white",
          font=("Segoe UI", 12, "bold"), width=35, pady=4).grid(row=0, column=0, columnspan=4, pady=(0,10))

    # Manual labels and entry boxes
    Label(insert_win, text="Name:", bg=BG_FRAME, fg=COLOR_LABEL,
          font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky=E, padx=8, pady=3)
    name_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=25, font=("Segoe UI", 10))
    name_e.grid(row=1, column=1, columnspan=3, sticky=W, pady=3)

    Label(insert_win, text="Nationality:", bg=BG_FRAME, fg=COLOR_LABEL,
          font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky=E, padx=8, pady=3)
    nat_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=25, font=("Segoe UI", 10))
    nat_e.grid(row=2, column=1, columnspan=3, sticky=W, pady=3)

    Label(insert_win, text="Manager:", bg=BG_FRAME, fg=COLOR_LABEL,
          font=("Segoe UI", 10, "bold")).grid(row=3, column=0, sticky=E, padx=8, pady=3)
    mgr_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=25, font=("Segoe UI", 10))
    mgr_e.grid(row=3, column=1, columnspan=3, sticky=W, pady=3)

    Label(insert_win, text="Training Gym:", bg=BG_FRAME, fg=COLOR_LABEL,
          font=("Segoe UI", 10, "bold")).grid(row=4, column=0, sticky=E, padx=8, pady=3)
    gym_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=25, font=("Segoe UI", 10))
    gym_e.grid(row=4, column=1, columnspan=3, sticky=W, pady=3)

    # stats row
    Label(insert_win, text="Wins:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=5, column=0, sticky=E, pady=3)
    wins_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=6)
    wins_e.grid(row=5, column=1, sticky=W, pady=3)

    Label(insert_win, text="Losses:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=5, column=2, sticky=E, pady=3)
    losses_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=6)
    losses_e.grid(row=5, column=3, sticky=W, pady=3)

    Label(insert_win, text="Fights:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=6, column=0, sticky=E, pady=3)
    fights_e = Entry(insert_win, bg=ENTRY_BG, relief=FLAT, width=6)
    fights_e.grid(row=6, column=1, sticky=W, pady=3)

    # Retired checkbox
    var_ret = IntVar()
    Checkbutton(insert_win, text="Retired", variable=var_ret, bg=BG_FRAME,
                fg=COLOR_LABEL).grid(row=7, column=0, columnspan=2, sticky=W, padx=10, pady=5)


    # Save Fighter
    def save_fighter():
        try:

            # Collect data from the Entry fields
            # .get() retrieves text, .strip() removes extra spaces
            name = name_e.get().strip()
            nat = nat_e.get().strip()
            mgr = mgr_e.get().strip()
            gym = gym_e.get().strip()
            wins = int(wins_e.get() or 0)
            losses = int(losses_e.get() or 0)
            fights = int(fights_e.get() or 0)
            retired = bool(var_ret.get())

            # If no name is entered, stop (don't insert empty fighter)
            if not name:
                return

            # Insert the fighter data into the SQLite database
            cur.execute("INSERT INTO Fighter VALUES(?,?,?,?,?,?,?,?)",
                        (name, nat, mgr, gym, wins, losses, fights, retired))

            # Commit saves the new record permanently in the database
            con.commit()

            # Refresh the fighter list on the left to include the new entry
            refreshListbox()

            # Close the Insert window after saving
            insert_win.destroy()


        except Exception as e:
            print("Insert error:", e)

    # Buttons
    Button(insert_win, text="Save Fighter", bg=DATA_COLOR, relief=RAISED,
           font=("Segoe UI", 10, "bold"), command=save_fighter).grid(row=8, column=1, pady=10, sticky="e")
    Button(insert_win, text="Cancel", bg="#f6b93b", relief=RAISED,
           font=("Segoe UI", 10, "bold"), command=insert_win.destroy).grid(row=8, column=2, pady=10, sticky="w")

# Insert Fighter
#============================================================


# Search Fighters
def openSearchWindow():
    search_win = Toplevel(window)
    search_win.title("Search Fighters")
    search_win.geometry("360x200")
    search_win.configure(bg=BG_FRAME)

    Label(search_win, text="Search Fighters", bg="#e1b12c", fg="white",
          font=("Segoe UI", 12, "bold"), width=30, pady=4).pack(pady=(0,10))
    Label(search_win, text="Enter keyword:", bg=BG_FRAME, fg=COLOR_LABEL,
          font=("Segoe UI", 10, "bold")).pack(pady=4)
    keyword_entry = Entry(search_win, bg=ENTRY_BG, relief=FLAT, width=28, font=("Segoe UI", 10))
    keyword_entry.pack(pady=3)




    def do_search():

        # Get search keyword from input box and remove extra spaces
        kw = keyword_entry.get().strip()

        # If search box is empty, do nothing
        if not kw:
            return

        # Add symbols (%) around the keyword for partial matching
        # Example: typing "Conor" will match "%Conor%" → finds "Conor McGregor"
        kw_like = f"%{kw}%"

        # SQL query: search across multiple columns for any partial match
        cur.execute("""SELECT * FROM Fighter WHERE
                       Fighter_Name LIKE ? OR Nationality LIKE ? OR Manager LIKE ? OR Training_Gym LIKE ?
                       OR CAST(Wins AS TEXT) LIKE ? OR CAST(Losses AS TEXT) LIKE ? OR CAST(Fights_Fought AS TEXT) LIKE ?""",
                    (kw_like, kw_like, kw_like, kw_like, kw_like, kw_like, kw_like))

        # Fetch all rows that match
        results = cur.fetchall()

        # Open the results in the display window
        displayDialog(window, results)

    Button(search_win, text="Search", bg=SEARCH_COLOR, relief=RAISED,
           font=("Segoe UI", 10, "bold"), command=do_search).pack(side=LEFT, padx=60, pady=20)
    Button(search_win, text="Cancel", bg="#f6b93b", relief=RAISED,
           font=("Segoe UI", 10, "bold"), command=search_win.destroy).pack(side=LEFT, padx=10, pady=20)

#============================================================

#-------Event Handling Methods ---------------

def clearCmd():
    for e in (entry_name, entry_nat, entry_mgr, entry_gym, entry_wins, entry_losses, entry_fights):
        e.delete(0, END)
    var_retired.set(0)

def updateFightCmd():
    result = resultTypeVar.get()
    name = entry_name.get().strip()
    if not name:
        return
    if result == "Win":
        cur.execute("update Fighter set Wins = Wins + 1, Fights_Fought = Fights_Fought + 1 where Fighter_Name = ?", (name,))
    else:
        cur.execute("update Fighter set Losses = Losses + 1, Fights_Fought = Fights_Fought + 1 where Fighter_Name = ?", (name,))
    con.commit()
    refreshListbox()
    display(current)

def cmdNationalityDisplay():
    nat = natTypeVar.get()
    cur.execute("select * from Fighter where Nationality = ?", (nat,))
    rows = cur.fetchall()
    displayDialog(window, rows)

def cmdWinsDisplay():
    minWins = int(winTypeVar.get())
    cur.execute("select * from Fighter where Wins >= ?", (minWins,))
    rows = cur.fetchall()
    displayDialog(window, rows)

def displayDialogAll():
    cur.execute("select * from Fighter")
    fighters = cur.fetchall()
    displayDialog(window, fighters)

def nextCmd():
    global current
    cur.execute("select * from Fighter order by Fighter_Name")
    rows = cur.fetchall()
    if not rows: return

    # If we're not already at the last fighter, move to the next one
    if current < len(rows)-1:
        display(current+1)

def prevCmd():
    global current
    cur.execute("select * from Fighter order by Fighter_Name")
    rows = cur.fetchall()
    if not rows: return
    if current > 0:
        display(current-1)

#============================================================
# Layout
label1 = Label(window, text="Fighter Application", fg="#e1b12c", bg=BG_MAIN, font=("Segoe UI", 16, "bold"))
label1.place(x=150, y=20)

# listbox documentation https://www.geeksforgeeks.org/python/python-tkinter-listbox-widget/
#Create the left frame for the list of fighters
leftFrame = Frame(window, bg=BG_FRAME, width=250, height=430, bd=1, relief="sunken")
leftFrame.place(x=10, y=80)

# Create the Listbox widget
# This displays all fighter names filled in by refreshListbox
listbox = Listbox(leftFrame, width=34, height=23, bg=ENTRY_BG, fg=COLOR_LABEL)
listbox.pack(side=LEFT, fill=BOTH, expand=True)


# Add a vertical scrollbar for the list
scroll = Scrollbar(leftFrame, command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)

# Bind a click event to the Listbox
# When a user selects a name, run onListSelect() to show its details
listbox.config(yscrollcommand=scroll.set)
listbox.bind('<<ListboxSelect>>', onListSelect)

frame = Frame(window, bg=BG_FRAME, padx=10, pady=10, bd=1, relief="solid")
frame.place(x=280, y=80)

Label(frame, text="Fighter Info", bg="#e1b12c", fg="white", font=("Segoe UI", 12, "bold"), width=48, pady=4).grid(row=0, column=0, columnspan=6, pady=(0,10))
Button(frame, text="◀ Prev", bg=NAV_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=prevCmd).grid(row=1, column=0, padx=5, pady=4, sticky="ew")
Button(frame, text="▶ Next", bg=NAV_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=nextCmd).grid(row=1, column=1, padx=5, pady=4, sticky="ew")

Label(frame, text="Fighter:", bg=BG_FRAME, fg=COLOR_LABEL, font=("Segoe UI", 10, "bold")).grid(row=1, column=2, padx=5)
entry_name = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=22)
entry_name.grid(row=1, column=3, columnspan=2, padx=5, sticky="w")

Label(frame, text="Nationality:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=2, column=0, sticky=E, pady=3)
entry_nat = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=10); entry_nat.grid(row=2, column=1, pady=3, sticky="w")
Label(frame, text="Manager:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=2, column=2, sticky=E, pady=3)
entry_mgr = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=14); entry_mgr.grid(row=2, column=3, pady=3, sticky="w")
Label(frame, text="Gym:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=2, column=4, sticky=E, pady=3)
entry_gym = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=14); entry_gym.grid(row=2, column=5, pady=3, sticky="w")

Label(frame, text="Wins:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=3, column=0, sticky=E, pady=3)
entry_wins = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=6); entry_wins.grid(row=3, column=1, pady=3, sticky="w")
Label(frame, text="Losses:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=3, column=2, sticky=E, pady=3)
entry_losses = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=6); entry_losses.grid(row=3, column=3, pady=3, sticky="w")
Label(frame, text="Fights:", bg=BG_FRAME, fg=COLOR_LABEL).grid(row=3, column=4, sticky=E, pady=3)
entry_fights = Entry(frame, bg=ENTRY_BG, relief=FLAT, width=6); entry_fights.grid(row=3, column=5, pady=3, sticky="w")

var_retired = IntVar()
Checkbutton(frame, text="Retired", bg=BG_FRAME, fg=COLOR_LABEL, variable=var_retired).grid(row=4, column=0, columnspan=2, pady=4, sticky=W)

Button(frame, text="Insert", bg=DATA_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=insertCmd).grid(row=5, column=0, padx=5, pady=4, sticky="ew")
Button(frame, text="Clear", bg=DATA_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=clearCmd).grid(row=5, column=1, padx=5, pady=4, sticky="ew")

Label(frame, text="Record Result:", bg=BG_FRAME, fg=COLOR_LABEL, font=("Segoe UI", 9, "bold")).grid(row=5, column=2, sticky=E)
resultTypeVar = StringVar(value="Win")
combo11 = OptionMenu(frame, resultTypeVar, "Win", "Loss")
combo11.config(bg=ACTION_COLOR, fg="white", relief=RAISED, highlightthickness=0, font=("Segoe UI", 9))
combo11.grid(row=5, column=3, padx=5, sticky=W)
Button(frame, text="Record", bg=ACTION_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=updateFightCmd).grid(row=5, column=4, padx=5, pady=4, sticky="ew")

Label(frame, text="Filters:", bg=BG_FRAME, fg=COLOR_LABEL, font=("Segoe UI", 10, "bold")).grid(row=6, column=0, sticky=W, pady=(8,4))
Button(frame, text="Display All", bg=DISPLAY_ALL_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=displayDialogAll).grid(row=7, column=0, padx=5, pady=4, sticky="ew")
Button(frame, text="By Nationality", bg=NATION_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=cmdNationalityDisplay).grid(row=7, column=1, padx=5, pady=4, sticky="ew")
natTypeVar = StringVar(value="USA")
combo_nat = OptionMenu(frame, natTypeVar, "USA", "Ireland", "Brazil", "Russia", "Canada", "New Zealand")
combo_nat.config(bg=NATION_COLOR, fg="white", relief=RAISED, font=("Segoe UI", 9))
combo_nat.grid(row=7, column=2, padx=3, sticky=W)

Button(frame, text="By Wins >=", bg=WINS_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=cmdWinsDisplay).grid(row=7, column=3, padx=5, pady=4, sticky="ew")
winTypeVar = StringVar(value="10")
combo_wins = OptionMenu(frame, winTypeVar, "0","5","10","15","20")
combo_wins.config(bg=WINS_COLOR, fg="white", relief=RAISED, font=("Segoe UI", 9))
combo_wins.grid(row=7, column=4, padx=3, sticky=W)

Button(frame, text="Search", bg=SEARCH_COLOR, relief=RAISED, font=("Segoe UI", 10, "bold"), command=openSearchWindow).grid(row=8, column=0, padx=5, pady=4, sticky="ew")

#============================================================
current = -1
refreshListbox()

mainloop()
