from sklearn import tree

# Training Data
X = [[0, 0], [1, 1], [1, 0], [0, 1]]
Y = [0, 1, 1, 0]

# Create and Train Model
clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)

# Predict
print(clf.predict([[1, 1]]))