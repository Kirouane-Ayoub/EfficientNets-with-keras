# -*- coding: utf-8 -*-
"""EfficientNets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c-T45Qq9qhJrbmKaVSdtordAEKDgptF2
"""

!pip install -U git+https://github.com/qubvel/efficientnet

import efficientnet.keras as enet
from keras.backend import sigmoid
from keras.models import Model
from keras.layers import Dense, Dropout, Activation, BatchNormalization

def swish_act(x, beta = 1):
    return (x * sigmoid(beta * x))

model = enet.EfficientNetB0(include_top=False, input_shape=(32,32,3), pooling='avg') # u can add weights='imagenet'

# Adding 2 fully-connected layers to B0.
x = model.output

x = BatchNormalization()(x)
x = Dropout(0.7)(x)

x = Dense(512)(x)
x = BatchNormalization()(x)
x = Activation(swish_act)(x)
x = Dropout(0.5)(x)

x = Dense(128)(x)
x = BatchNormalization()(x)
x = Activation(swish_act)(x)

# Output layer
predictions = Dense(10, activation="softmax")(x)

model_final = Model(inputs = model.input, outputs = predictions)

model_final.summary()

from tensorflow.keras.utils import plot_model

plot_model(model)

"""# EfficientNet-B7"""

model1 = enet.EfficientNetB7(include_top=False, input_shape=(32,32,3), pooling='avg')

model1.summary()