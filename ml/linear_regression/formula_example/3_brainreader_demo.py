import pandas as pd # just to avoid warning, pass feature name as input
import pickle


model = None
with open("artifacts/magicMathsModel.pkl", "rb") as file:  # Open in binary read mode
    model = pickle.load(file)
    # Print weights and bias
    print("Weights:", model.coef_)
    print("Bias:", model.intercept_)



if __name__=='__main__':
    
    while True:
        numbers = []
        print("   WELCOME TO AI RESULT PREDICTOR    ")
        print("=" * 40)
        # Round 1
        user = int(input("[1] Enter a 5-digits integer number: "))
        result = int(model.predict(pd.DataFrame({'x': [user]}))[0])
        print(f"AI preidcts the result will be: {result}")
        numbers.append(user)
        
        # Round 2
        user = int(input("[2] Enter again 5-digits integer number: "))
        ai = 99999 - user
        numbers.extend([user, ai])
        print(f"AI types: {ai}")
        
        user = int(input("[3] Enter for the last time a 5-digits integer number: "))
        ai = 99999 - user
        numbers.extend([user, ai])
        print(f"AI types: {ai}")

        print("=" * 20)
        print("Verify that I am right:")
        print(f"\t {numbers[0]}")
        for n in numbers[1:]:
            print(f"\t+{n}")
        print("  " + "-"*20)
        print(f"\t{result}")
        print("  " + "-"*20)