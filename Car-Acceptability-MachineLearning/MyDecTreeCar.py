#-------------------------------------
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd

class MyDecisionTreeCar:

    def __init__(self):
        self.df = pd.read_csv('car_evaluation.csv')          # load the dataset from csv
        self.X = self.df.drop('class', axis='columns')       # features (all columns except class)
        self.y = self.df['class']                            # target values (class column)
        self.seedValue = 1                                   # default seed value
        self.X_train=None                                    # will hold X training data
        self.X_test=None                                     # will hold X testing data
        self.y_train=None                                    # will hold y training values
        self.y_test=None                                     # will hold y testing values
        self.tree = DecisionTreeClassifier()                 # decision tree model
        self.y_hat=None                                      # will store predictions for test data

    # updates the random seed so the split can change
    def updateSeed(self,newValue):
        self.seedValue = newValue

    # splits the data and trains the decision tree
    def trainData(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=100, random_state=self.seedValue, stratify=self.y)  # split data

        self.tree = DecisionTreeClassifier()                 # create a new tree model
        self.tree.fit(self.X_train, self.y_train)            # train the tree with training data

    # makes a prediction using one row of numeric input
    def makePrediction(self, buying, maint, doors, persons, lug_boot, safety):
        input_data = [[buying, maint, doors, persons, lug_boot, safety]]  # pack inputs into list
        df2 = pd.DataFrame(input_data,
            columns=['buying','maint','doors','persons','lug_boot','safety']) # convert to dataframe
        result = self.tree.predict(df2)                       # make prediction
        return result[0]                                      # return the prediction value

    # tests the model using test data and returns confusion matrix + accuracy
    def testData(self):
        self.y_hat = self.tree.predict(self.X_test)          # predict y values for the test set
        accuracy = accuracy_score(self.y_test, self.y_hat)   # calculate accuracy
        cm = confusion_matrix(self.y_test, self.y_hat)       # create confusion matrix
        return cm, accuracy                                  # return test results

    # returns the category names as a readable string
    def readCategories(self):
        result=''
        for val in sorted(set(self.y)):                      # loop through class values
            if val == 0: result += "Unacceptable / "
            if val == 1: result += "Acceptable / "
            if val == 2: result += "Good / "
            if val == 3: result += "Very Good / "
        return result[:-3]

