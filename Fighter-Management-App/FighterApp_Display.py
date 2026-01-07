from tkinter import *

def displayDialog(window, fighter_list):
    window2 = Toplevel(window)
    window2.geometry("1300x650")
    window2.title("Fighter List")
    fighterList = fighter_list

#============================================================
# Event Handling Methods

    def displayAll():
        for i in range(0, len(fighterList)):
            line = '' + fighterList[i][0]
            line += '\t\t' + fighterList[i][1]
            line += '\t\t' + fighterList[i][2]
            line += '\t\t' + fighterList[i][3]
            line += '\t\tWins=' + str(fighterList[i][4])
            line += '\tLosses=' + str(fighterList[i][5])
            line += '\tFights=' + str(fighterList[i][6])
            retired = fighterList[i][7]
            if retired:
                line += '\t\tRetired'
            line += '\n\n'
            text.insert(END, line)

    def closeEvent():
        window2.destroy()

    button6 = Button(window2, text="Close", fg="black", font=("arial", 12, "bold"), command=closeEvent)
    button6.place(x=10, y=10)

    text = Text(window2, undo=True, height=34, width=150)
    text.place(x=20, y=60)

    displayAll()
