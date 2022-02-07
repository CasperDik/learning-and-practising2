import mnist_loader

# load data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

network_type = 2

if network_type == 1:
    import network1

    # set up network with 30 hidden neurons
    net = network1.Network([784, 10, 10])

    # use stochastic gradient descent to learn from the MNIST training_data over 30 epochs
    # with a mini-batch size of 10, and a learning rate of η=3.0
    net.SGD(training_data, 30, 10, 3, test_data=test_data)

if network_type == 2:
    import network2
    net = network2.Network([784, 30, 10], cost=network2.CrossEntropyCost)
    net.large_weight_initializer()
    net.SGD(training_data, 30, 10, 0.5, evaluation_data=test_data, monitor_evaluation_accuracy = True)