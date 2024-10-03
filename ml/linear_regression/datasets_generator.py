import random as rd

def OR_dataset():
    return Xy_separate([
        #w1 w2 y
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ])

def NOR_dataset():
    return Xy_separate([
        #w1 w2 y
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 0)
    ])

def AND_dataset():
    return Xy_separate([
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1)
    ])

def XOR_dataset():
    return Xy_separate([
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ])

    
def linear_dataset(w:list[float], b, size:int) -> tuple[list, list]:
    """
        datapoints for a line with:
            - w: slope (vector)
            - b: y intercept
    """
    dataset = []
    for _ in range(size): # generate sample
        xi = []
        yi = 0
        for  v in w: # generate feature value
            xij = rd.randint(-25, 25)
            xi.append(xij)
            yi += v * xij
        xi.append(yi + b)
        dataset.append(tuple(xi))
    return Xy_separate(dataset=dataset)


def Xy_separate(dataset:list[tuple]) -> tuple[list, list]:
    X = []
    y = []
    
    for x in dataset:
        X.append(x[:-1])
        y.append(x[-1])
    return X, y


if __name__=="__main__":
     
    print(linear_dataset([1, -2, 3], .5, size=10))