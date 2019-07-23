import numpy as np
from PIL.ImageOps import expand
from keras.layers import Convolution2D, Activation

# Squeeze part of fire module with 1 * 1 convolutions, followed by
x = []

x = Convolution2D(np.squeeze, (1, 1), padding='valid', name='fire2/squeeze1x1')(x)
x = Activation('relu', name='fire2/relu_squeeze1x1')(x)

# Expand part has two portions, left uses 1 * 1 convolutions and is called expand1x1&nbsp;
left = Convolution2D(expand, (1, 1), padding='valid', name='fire2/expand1x1')(x)
left = Activation('relu', name='fire2/relu_expand1x1')(left)

# Right part uses 3 * 3 convolutions and is called expand3x3, both of these are follow#ed by Relu layer,
# Note that both receive x as input as designed.&nbsp;
right = Convolution2D(expand, (3, 3), padding='same', name='fire2/expand3x3')(x)
right = Activation('relu', name='fire2/relu_expand3x3')(right)

# Final output of Fire Module is concatenation of left and right.&nbsp;
x = np.concatenate([left, right], axis=3, name='fire2/concat')
