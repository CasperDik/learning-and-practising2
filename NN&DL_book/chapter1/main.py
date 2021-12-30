from chapter1 import mnist_loader
from chapter1 import network

# load data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

# set up network with 30 hidden neurons
net = network.Network([784, 10, 10])

# use stochastic gradient descent to learn from the MNIST training_data over 30 epochs
# with a mini-batch size of 10, and a learning rate of η=3.0
net.SGD(training_data, 30, 10, 3, test_data=test_data)

# todo: learn how the code works before going to chapter 2 (except backpropagation)