def eval_val(x1, x2, c, y1, y2):
    return x1*y1 + x2*y2 + c

def eval(x1, x2, c, y1, y2):
    return eval_val(x1, x2, c, y1, y2) >= 0

def subtract(x, y, lr):
    return x + y * lr

def main():
    counter = 0
    retval = -1
    x1, x2, c, y1, y2, learning_rate = 3, 4, -10, 1, 1, 0.1
    while True:
        if eval(x1, x2, c, y1, y2):
            break
        else:
            print(eval_val(x1, x2, c, y1, y2))
            counter += 1
            x1 = subtract(x1, y1, learning_rate)
            x2 = subtract(x2, y2, learning_rate)
            c = subtract(c, 1, learning_rate)
    print(counter)

if __name__ == '__main__':
    main()
