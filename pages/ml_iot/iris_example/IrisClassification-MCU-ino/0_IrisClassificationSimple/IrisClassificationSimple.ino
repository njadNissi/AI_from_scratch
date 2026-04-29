#include "IrisClassifier.h"

// IrisClassifier.h creates a irisClassifier object
// that you can use to classify a feature vector
// no setup is required
String features[] = {"Sepal Length", "Sepal Width", "Petal Length", "Petal Width"};
String labels[] = {"Iris Setosa", "Iris Versicolor", "Iris Virginica"};
void setup() {
    Serial.begin(115200);
}

void loop() {
  delay(500);
  //ex1
  predict(5.1, 3.5, 1.4, 0.2);

  delay(500);
  //ex2
  predict(6.4, 3.5, 4.5, 1.2);

  delay(500);
  //ex3
  predict(5.9, 3.0, 5.0, 1.8);

}

void predict(float sl, float sw, float pl, float pw){
  float input[4] = {sl, sw, pl, pw};
  int cl = irisClassifier.predict(input);
  for(int i=0; i<3; i++){
    Serial.print(" | ");
    Serial.print(features[i]);
    Serial.print(" : ");
    Serial.print(input[i]);
  }
  Serial.print(" ====> ");
  Serial.println(labels[cl]);
  Serial.println();
}