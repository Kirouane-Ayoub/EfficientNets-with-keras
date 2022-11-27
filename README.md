# EfficientNets-with-keras : 


What is EfficientNet?

![1669154527421](https://user-images.githubusercontent.com/99510125/204158584-60acb9a4-df23-4d4e-9e99-629471ba7d50.png)


EfficientNet is a convolutional neural network architecture and scaling method that uniformly scales all depth/width/resolution dimensions using a compound coefficient.
The researchers first designed a baseline network by performing the Neural architecture search (NAS), a technique for automating the design of neural networks. It optimizes both the accuracy and efficiency as measured on the floating-point operations per second (FLOPS) basis. This developed architecture uses the mobile inverted bottleneck convolution (MBConv). The researchers then scaled up this baseline network to obtain a family of deep learning models, called EfficientNets. Its architecture is given in the below diagram.

