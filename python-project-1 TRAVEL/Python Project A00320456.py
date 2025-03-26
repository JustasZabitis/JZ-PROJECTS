class NoVisits (Exception) : pass

from tkinter import *
window = Tk()
window.geometry("600x700")
window.title("Welcome")

class Destination:
  def __init__(self, country, city, Tactivities):
    self.__country = country
    self.__city = city
    self.__Tactivities = int(Tactivities)
    self.__visits = 0
    self.__Cactivities = 0
    self.__money = 0
    self.__rating = 0
    self.__percentCompleted = ""

  def getCountry(self):
    return self.__country

  def getCity(self):
    return self.__city

  def getVisits(self):
    return self.__visits

  def getMoney(self):
    return self.__money

  def getTactivities(self):
    return self.__Tactivities

  def getCactivities(self):
    return self.__Cactivities

  def getRating(self):
    return self.__rating

  def getCompleted(self):
    if (self.__visits)==0:
      raise NoVisits
    else:
      self.__percentCompleted = int(100 * (self.__Cactivities / (self.__Tactivities)))
      return self.__percentCompleted

  def getPercentCompleted(self):
    return self.__percentCompleted



  def addVisits(self):
    self.__visits += 1

  def addCactivities(self):
    self.__Cactivities += 1

  def addMoney(self):
    self.__money += 500

  def addRating(self, rating):
    if (self.__visits == 0):
      raise NoVisits
    else:
      self.__rating = rating






  def resetAll(self):
    self.__visits = 0
    self.__Cactivities = 0
    self.__money = 0
    self.__rating = 0
    self.__percentCompleted = ""

#------------end of class definition------------------

def display(index):
  global current
  global place
  place = placelist[index]
  current = index
  entry2.delete(0, END) # delete old value
  entry2.insert(END, place.getCity())
  entry3.delete(0, END) # delete old value
  entry3.insert(END, place.getCountry())
  entry4.delete(0, END) # delete old value
  entry4.insert(END, str(place.getVisits()))
  entry5.delete(0, END) # delete old value
  entry5.insert(END, place.getTactivities())
  entry6.delete(0, END) # delete old value
  entry6.insert(END, str(place.getCactivities()))
  entry7.delete(0, END) # delete old value
  entry7.insert(END, f"€{place.getMoney()}")
  entry8.delete(0, END)
  entry8.insert(END, str(place.getRating()))
  entry9.delete(0, END)

  if place.getPercentCompleted() == "":
    entry9.insert(END, "")
  else:
    entry9.insert(END, f"{place.getPercentCompleted()}%")


  entryMsg.delete(0, END)


def addVisits():
  global place
  place.addVisits()
  display(current)

def addMoney():
  global place
  place.addMoney()
  display(current)

def addCactivities():
  global place
  place.addCactivities()
  display(current)


def addRating():
  try:
    rating = int(ratingVar.get())
    place.addRating(rating)
    display(current)
  except:
    entryMsg.insert(END, "No Visits Yet")




def percentCompleted():
  try:
    result = place.getCompleted()
    place.getPercentCompleted()
    entry9.delete(END, 0)
    entry9.insert(END, (str(result) + " %"))
  except:
    entryMsg.delete(END, 0)
    entryMsg.insert(END, "No Visits Yet")






#NEXT            FIRST             LAST              PREV


def nextCmd():
  global current
  if (current<(len(placelist) - 1)):
    current += 1
    display(current)


def prevCmd():
  global current
  if (current>0):
    current -= 1
    display(current)


def firstCmd():
  display(0)



def lastCmd():
  display(len(placelist) - 1)




#NEXT            FIRST             LAST              PREV




def insertNewPlace():
  destination=entry3.get()
  country=entry2.get()
  tactivities=entry5.get()
  tactivities = int(tactivities)
  newplace=Destination(destination, country, tactivities)
  placelist.append(newplace)











def resetAll():
  global place
  place.resetAll()
  display(current)









def exitEvent():
  quit()



global current
global place
place1 = Destination("Spain", "Barcelona", "23")
place2 = Destination("France", "Paris", "32")
place3 = Destination("Germany", "Berlin", "16")
place4 = Destination("Italy", "Rome", "54")
place5 = Destination("Poland", "Warsaw", "10")

placelist = [place1, place2, place3, place4, place5]
current = 0
place = placelist[current] # Initialize first item in the list

frame = Frame(window, width=10000, height=10000)
frame.place(x=10,y=80)


label1 = Label(window, text="Travel Destination Tracker", fg="blue",bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=15, y=30)              # place on screen

label2 = Label(window, text="Destination Name", fg="blue", width=13, font=("arial", 10, "bold"))  #
label2.place(x=10, y=90)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=130, y=90)

label3 = Label(window, text="Country", fg="blue", width=8, font=("arial", 10, "bold"))  #
label3.place(x=31, y=115)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=130, y=115)

label4 = Label(window, text="Num of Visits", fg="blue", width=10, font=("arial", 10, "bold"))  #
label4.place(x=25, y=175)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=130, y=175)

label5 = Label(window, text="Total Activities", fg="blue", width=12, font=("arial", 10, "bold"))  #
label5.place(x=17, y=235)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=130, y=235)

label6 = Label(window, text="Completed Act's", fg="blue", width=12, font=("arial", 10, "bold"))  #
label6.place(x=17, y=300)

entry6 = Entry(window)
entry6.insert(END, '0')
entry6.place(x=130, y=300)

label7 = Label(window, text="Money Spent", fg="blue", width=12, font=("arial", 10, "bold"))  #
label7.place(x=17, y=455)

entry7= Entry(window)
entry7.insert(END, '0')
entry7.place(x=130, y=455)

label8 = Label(window, text="Rating", fg="blue", width=12, font=("arial", 10, "bold"))  #
label8.place(x=17, y=390)

entry8= Entry(window)
entry8.insert(END, '0')
entry8.place(x=130, y=390)

label9 = Label(window, text="% Completed", fg="blue", width=12, font=("arial", 10, "bold"))  #
label9.place(x=17, y=325)

entry9= Entry(window)
entry9.insert(END, '')
entry9.place(x=130, y=325)

label10 = Label(window, text="Error Message", fg="red", width=12, font=("arial", 10, "bold"))  #
label10.place(x=17, y=520)

entryMsg = Entry(window)
entryMsg.insert(END, '')
entryMsg.place(x=130, y=520)




#-------------------------------

button1 = Button(frame, text="Record Visit", fg="white", bg="green", font=("arial", 10, "bold"), width=15, height=1, command=addVisits)
button1.place(x=260, y=90)

button2 = Button(frame, text="Add Activity", fg="white", bg="blue", font=("arial", 10, "bold"), width=15, height=1, command=addCactivities)
button2.place(x=400, y=228)

button3 = Button(frame, text="Add Money", fg="white", bg="purple", font=("arial", 10, "bold"), width=15, height=1, command=addMoney)
button3.place(x=260, y=370)

button4 = Button(frame, text="Add Rating", fg="white", bg="orange", font=("arial", 10, "bold"), width=15, height=1, command=addRating)
button4.place(x=260, y=305)

button5 = Button(frame, text="Reset All", fg="white", bg="red", font=("arial", 10, "bold"), width=15, height=1, command=resetAll)
button5.place(x=300, y=500)

button6 = Button(frame, text="Exit", fg="white", bg="pink", font=("arial", 10, "bold"), width=15, height=1 ,command=exitEvent)
button6.place(x=160, y=500)

button7 = Button(frame, text="% Completed", fg="white", bg="violet", font=("arial", 10, "bold"), width=15, height=1 ,command=percentCompleted)
button7.place(x=260, y=228)

button8 = Button(frame, text="Next", fg="white", bg="indigo", font=("arial", 10, "bold"), width=15, height=1 ,command=nextCmd)
button8.place(x=260, y=0)

button9 = Button(frame, text="Previous", fg="white", bg="indigo", font=("arial", 10, "bold"), width=15, height=1 ,command=prevCmd)
button9.place(x=400, y=0)

button10 = Button(frame, text="First", fg="white", bg="indigo", font=("arial", 10, "bold"), width=15, height=1 ,command=firstCmd)
button10.place(x=260, y=30)

button11 = Button(frame, text="Last", fg="white", bg="indigo", font=("arial", 10, "bold"), width=15, height=1 ,command=lastCmd)
button11.place(x=400, y=30)


list1 = ['1', '2', '3', '4', '5']
ratingVar = StringVar()
combo1 = OptionMenu(frame, ratingVar, *list1)
ratingVar.set("1")
combo1.config(font=("arial", 10, "bold"), bg="yellow", fg="black", width=13)
combo1.place(x=400, y=303)

menu1 = Menu(window)
window.config(menu=menu1)
subm1=Menu(menu1)
menu1.add_cascade(label="Add_Place", menu=subm1)
subm1.add_command(label="clearData",font=("arial", 12, "bold"),command = resetAll)
subm1.add_command(label="Insert Place", font=("arial", 12, "bold"), command = insertNewPlace)










display(0)

mainloop()