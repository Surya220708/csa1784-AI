from sklearn.neural_network import MLPClassifier

# Training Data
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [0,1,1,0]

# Feed Forward Neural Network
model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=1000,
                      random_state=1)

model.fit(X, Y)

print(model.predict([[1,0]]))