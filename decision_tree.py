#-------------------------------------------------------------------------
# AUTHOR: David Lam
# FILENAME: decision_tree.py
# SPECIFICATION: Build a decision tree classifier for the contact lens dataset
# FOR: CS 4210- Assignment #1
# TIME SPENT: 4 days
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
for i in range(len(db)):
    encoded_row = []
    
    if db[i][0] == 'Young':
        encoded_row.append(1)
    elif db[i][0] == 'Prepresbyopic':
        encoded_row.append(2)
    elif db[i][0] == 'Presbyopic':
        encoded_row.append(3)

    if db[i][1] == 'Myope':
        encoded_row.append(1)
    elif db[i][1] == 'Hypermetrope':
        encoded_row.append(2)

    if db[i][2] == 'Yes':
        encoded_row.append(1)
    elif db[i][2] == 'No':
        encoded_row.append(2)
        
    if db[i][3] == 'Reduced':
        encoded_row.append(1)
    elif db[i][3] == 'Normal':
        encoded_row.append(2)

    X.append(encoded_row)

print(X)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here
for i in range(len(db)):
    if db[i][4] == 'Yes':
        Y.append(1)
    elif db[i][4] == 'No':
        Y.append(2)

print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()