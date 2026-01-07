from tkinter import *
from MyDecTreeCar import MyDecisionTreeCar
import random
import matplotlib.pyplot as plt


decisionTree = MyDecisionTreeCar()

def trainData():
    decisionTree.updateSeed(int(seedVar.get()))
    decisionTree.trainData()

def testData():
    output.delete("1.0","end")
    output.insert(END, decisionTree.readCategories()+"\n")
    result, accuracy = decisionTree.testData()
    output.insert(END, f"\nConfusion M# sets the seed and trains the decision tree model")
def trainData():
    decisionTree.updateSeed(int(seedVar.get()))   # convert selected seed to int and store it
    decisionTree.trainData()                      # train the model with the new seed


# tests the model accuracy and shows the results
def testData():
    output.delete("1.0","end")                    # clear right panel text
    output.insert(END, decisionTree.readCategories()+"\n")  # show class labels
    result, accuracy = decisionTree.testData()    # run the model test
    output.insert(END, f"\nConfusion Matrix:\n{result}\n")  # display matrix
    output.insert(END, f"\nAccuracy: {int(accuracy*100)}%") # display accuracy


# fills all entry boxes with random values to test quickly
def fillRandom():
    entries[0].delete(0,END); entries[0].insert(END, random.randint(0,3))      # random buying
    entries[1].delete(0,END); entries[1].insert(END, random.randint(0,3))      # random maint
    entries[2].delete(0,END); entries[2].insert(END, random.choice([2,3,4,5])) # random doors
    entries[3].delete(0,END); entries[3].insert(END, random.choice([2,4,6]))   # random persons
    entries[4].delete(0,END); entries[4].insert(END, random.randint(0,2))      # random luggage
    entries[5].delete(0,END); entries[5].insert(END, random.randint(0,2))      # random safety


# clears every input and output field in the GUI
def resetForm():
    entries[0].delete(0, END)      # clear buying
    entries[1].delete(0, END)      # clear maint
    entries[2].delete(0, END)      # clear doors
    entries[3].delete(0, END)      # clear persons
    entries[4].delete(0, END)      # clear luggage
    entries[5].delete(0, END)      # clear safety
    predictionBox.delete(0, END)   # clear prediction output
    output.delete("1.0", "end")    # clear right-side text area
    suggestion.delete("1.0", "end")# clear suggestion text area


# creates a suggestion message based on the predicted result and values entered
def generateSuggestion(pred, buying, maint, doors, persons, lug_boot, safety):

    if pred == 0:                              # if prediction is Unacceptable
        if safety == 0:                        # very low safety
            return "Safety is very low. Improving safety may increase acceptability."
        if buying >= 2:                        # overpriced car
            return "Buying price is high. Consider a cheaper model."
        return "Several features fall below acceptable standard."

    if pred == 1:                              # if Acceptable
        if lug_boot == 0:                      # very small boot
            return "Small boot size. Medium or large boot improves rating."
        return "Car is acceptable but could be improved in a few areas."

    if pred == 2:                              # if Good
        if buying == 3:                        # good car but expensive
            return "Great car overall, but expensive."
        return "Solid car with good characteristics."

    if pred == 3:                              # if Very Good
        return "Excellent rating. No improvements required."

    return ""


# uses the decision tree to make a prediction and display the result
def makePrediction():
    buying = int(entries[0].get())        # read buying value
    maint = int(entries[1].get())         # read maint value
    doors = int(entries[2].get())         # read doors value
    persons = int(entries[3].get())       # read persons value
    lug_boot = int(entries[4].get())      # read luggage value
    safety = int(entries[5].get())        # read safety value

    pred = decisionTree.makePrediction(buying, maint, doors, persons, lug_boot, safety) # get model prediction

    label = "Unacceptable"                # default label
    if pred == 1: label = "Acceptable"    # change label
    if pred == 2: label = "Good"
    if pred == 3: label = "Very Good"

    predictionBox.delete(0, END)          # clear the prediction box
    predictionBox.insert(END, label)      # show new prediction

    suggestion.delete("1.0","end")        # clear old suggestions
    suggestion.insert(END,                # show new suggestion
        generateSuggestion(pred, buying, maint, doors, persons, lug_boot, safety)
    )


# shows pie charts of the dataset (class, safety, buying)
def showDistributions():
    df = decisionTree.df                 # get dataframe used in training

    class_counts = df['class'].value_counts().sort_index()  # count each class
    class_labels = ["Unacc", "Acc", "Good", "VGood"]        # labels for the pie chart

    plt.figure(figsize=(5,5))            # create figure size
    plt.pie(class_counts, labels=class_labels, autopct="%1.1f%%", startangle=140) # class pie
    plt.title("Class Distribution")      # title
    plt.axis('equal')                    # keep circle shape
    plt.show()                           # show chart

    safety_counts = df['safety'].value_counts().sort_index() # count safety values
    safety_labels = ["Low", "Med", "High"]                   # safety labels

    plt.figure(figsize=(5,5))            # new chart
    plt.pie(safety_counts, labels=safety_labels, autopct="%1.1f%%", startangle=140)
    plt.title("Safety Rating Distribution")
    plt.axis('equal')
    plt.show()

    buying_counts = df['buying'].value_counts().sort_index() # count buying values
    buying_labels = ["Low","Med","High","VHigh"]             # buying labels

    plt.figure(figsize=(5,5))            # new chart
    plt.pie(buying_counts, labels=buying_labels, autopct="%1.1f%%", startangle=140)
    plt.title("Buying Price Distribution")
    plt.axis('equal')
    plt.show()


# GUI


window = Tk()
window.geometry("900x900")
window.title("Car Acceptability Predictor")

# LEFT PANEL
left = Frame(window, width=450, height=700)
left.grid(row=0, column=0, padx=10, pady=10)

title = Label(left, text="Car Acceptability Predictor", fg="blue", bg="yellow", font=("arial", 16, "bold"))
title.pack(pady=10)

desc = Label(left, text="This program uses a Decision Tree model to predict car acceptability.\n\nHow to Use:\n1. Select a seed value\n2. Click Train Data\n3. Click Test Data\n4. Enter numeric car values\n5. Click Make Prediction", justify=LEFT)
desc.pack()


codes = Label(left, text="Numeric Codes:\nBuying: 0-3 (low - vhigh)\nMaint: 0-3 (low - vhigh)\nDoors: 2,3,4,5+\nPersons: 2,4,6\nLuggage: 0-2 (small - big)\nSafety: 0-2 (low - high)", justify=LEFT, fg="darkgreen")
codes.pack(pady=10)


seedFrame = Frame(left)
seedFrame.pack(pady=10)
Label(seedFrame, text="Seed Value").grid(row=0, column=0)
seedVar = StringVar()
seedVar.set("1")
OptionMenu(seedFrame, seedVar, '1','2','3','4','5').grid(row=0, column=1)

trainBtn = Button(left, text="Train Data", command=trainData, width=20)
testBtn = Button(left, text="Test Data", command=testData, width=20)
trainBtn.pack(pady=5)
testBtn.pack(pady=5)

inputFrame = Frame(left)
inputFrame.pack(pady=10)

labels = ["Buying (0-3)", "Maint (0-3)", "Doors", "Persons", "Luggage (0-2)", "Safety (0-2)"]
entries = []

# Buying (0-3)
Label(inputFrame, text="Buying (0-3)").grid(row=0, column=0, sticky=W)
e0 = Entry(inputFrame)
e0.grid(row=0, column=1)
entries.append(e0)

# Maint (0-3)
Label(inputFrame, text="Maint (0-3)").grid(row=1, column=0, sticky=W)
e1 = Entry(inputFrame)
e1.grid(row=1, column=1)
entries.append(e1)

# Doors
Label(inputFrame, text="Doors").grid(row=2, column=0, sticky=W)
e2 = Entry(inputFrame)
e2.grid(row=2, column=1)
entries.append(e2)

# Persons
Label(inputFrame, text="Persons").grid(row=3, column=0, sticky=W)
e3 = Entry(inputFrame)
e3.grid(row=3, column=1)
entries.append(e3)

# Luggage (0-2)
Label(inputFrame, text="Luggage (0-2)").grid(row=4, column=0, sticky=W)
e4 = Entry(inputFrame)
e4.grid(row=4, column=1)
entries.append(e4)

# Safety (0-2)
Label(inputFrame, text="Safety (0-2)").grid(row=5, column=0, sticky=W)
e5 = Entry(inputFrame)
e5.grid(row=5, column=1)
entries.append(e5)


Button(left, text="Random Example", command=fillRandom, width=20).pack(pady=5)
Button(left, text="Reset Inputs", command=resetForm, width=20).pack(pady=5)
Button(left, text="Make Prediction", command=makePrediction, width=20).pack(pady=10)
Button(left, text="Show Feature Distribution", command=showDistributions, width=20).pack(pady=5)


predictionBox = Entry(left, width=25)
predictionBox.pack(pady=5)

Label(left, text="Suggestion:", fg="blue").pack()
suggestion = Text(left, height=4, width=40)
suggestion.pack()

# RIGHT PANEL
right = Frame(window, width=450, height=700, relief="sunken", borderwidth=2)
right.grid(row=0, column=1, padx=10, pady=10)

Label(right, text="OUTPUT PANEL", fg="blue", font=("arial", 14, "bold")).pack(pady=10)

output = Text(right, height=30, width=50)
output.pack()

window.mainloop()
