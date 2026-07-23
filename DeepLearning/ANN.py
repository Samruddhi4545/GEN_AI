import numpy as np
from sklearn.neural_network import MLPClassifier #type:ignore
X=np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])
y=np.array([0,0,0,1])#XOR output
model=MLPClassifier(hidden_layer_sizes=(4,),
                    activation='relu',
                    max_iter=5000,
                    random_state=1
)
model.fit(X,y)
pred_y=model.predict(X)
print("Actual",y)
print("predicted",pred_y)
accuracy=model.score(X,y)
print("Accuracy:",accuracy)