X = [2, 4, 6, 8]
y = [0, 0, 1, 1]

correct = 0

for i in range(len(X)):
    pred = 0 if X[i] < 5 else 1
    if pred == y[i]:
        correct += 1

print("Accuracy:", correct / len(X))