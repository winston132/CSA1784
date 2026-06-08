import math

inputs = [1, 2]
weights = [0.5, 0.4]
bias = 0.1

net = inputs[0] * weights[0] + inputs[1] * weights[1] + bias
output = 1 / (1 + math.exp(-net))

print("Output =", round(output, 4))