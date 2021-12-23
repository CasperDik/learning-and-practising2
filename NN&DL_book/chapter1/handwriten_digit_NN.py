import numpy as np

class Network(object):
    # if we want to create a Network object with 2 neurons in the first layer, 3 neurons in the second layer, and 1 neuron in the final layer
    # net = Network([2, 3, 1])

    def __init__(self, sizes):
        # sizes contains the number of neurons in the respective layers
        self.num_layers = len(sizes)
        self.sizes = sizes

        # The biases and weights in the Network object are all initialized randomly --> explore better way later
        # Network initialization code assumes that the first layer of neurons is an input layer
        # and omits to set any biases for those neurons
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

        def sigmoid(z):
            return 1.0 / (1.0 + np.exp(-z))

        def feedforward(self, a):
            """Return the output of the network if "a" is input."""
            for b, w in zip(self.biases, self.weights):
                a = sigmoid(np.dot(w, a) + b)
            return a



net = Network([2, 3, 1])