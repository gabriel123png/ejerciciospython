import pandas as pd
from sklearn.tree  import DecisionTreeClassifier

x=[[10000],[20000],[30000],[50000],[70000],[90000]]
y=[0,0,0,1,1,1]

modelo=DecisionTreeClassifier(random_state=42)
modelo.fit(x , y)

prediccion=modelo.predict([[45000]])

if prediccion [0] == 1:
    print("el cliente puede comprar")
else:
    print("el cliente no puede comprar")