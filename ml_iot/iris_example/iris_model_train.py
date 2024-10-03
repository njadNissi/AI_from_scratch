from sklearn.datasets import load_iris
from everywhereml.sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True) # replace this with your own data!
clf = RandomForestClassifier(n_estimators=5).fit(X, y)

features = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
labels = ["Iris Setosa", "Iris Versicolor", "Iris Virginica"]
# print(X)


'''
  Now we convert the classifier to C++ with a single line of code
  - instance_name will create an instance of the classifier in the produced code
    (you will use this name later)
'''
def generate_hfile():
  with open('IrisClassifier.h', 'w') as f:
    f.write(clf.to_arduino(instance_name='irisClassifier'))
    

if __name__=="__main__":
  input = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.4, 3.5, 4.5, 1.2],
    [5.9, 3.0, 5.0, 1.8]
  ]
  indexes = clf.predict(X=input)
  for index in indexes:
    print(f"{input[index]} : {labels[index]}")

  generate_hfile()