import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def inverse_sigmoid(x):
    return - np.log((1 - x)/x)

def main():
    x = sigmoid(5)
    y = inverse_sigmoid(x)
    print(x, y)

if __name__ == '__main__':
    print(sigmoid(20))
    print(sigmoid(2))
