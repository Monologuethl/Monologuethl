from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Flatten, MaxPooling2D, Conv2D
import numpy as np
from keras.layers import Input

## First, define the vision modules

digit_input = Input(shape=(1, 28, 28))

x = Conv2D(64, (3, 3))(digit_input)
x = Conv2D(64, (3, 3))(x)
x = MaxPooling2D((2, 2))(x)
out = Flatten()(x)


vision_model = Model(digit_input, out)