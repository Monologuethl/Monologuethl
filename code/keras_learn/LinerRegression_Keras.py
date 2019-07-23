import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
# a) 创建训练数据
# rainX 的数据范围是 -1 到 1，TrainY 与 TrainX 的关系是3倍，并且我们加入了一些噪声点。
trX = np.linspace(-1, 1, 101)
trY = 3 * trX + np.random.randn(*trX.shape) * 0.33
# b) 构建模型
model = Sequential()
model.add(Dense(input_dim=1, output_dim=1, init='uniform', activation='linear'))
# 输入数据 x，权重 w 和偏置项
# Linear regression model is initialized with weight w: -0.03, b: 0.00
weights = model.layers[0].get_weights()
w_init = weights[0][0][0]
b_init = weights[1][0]
print('Linear regression model is initialized with weights w: %.2f, b: %.2f' % (w_init, b_init))
model.compile(optimizer='sgd', loss='mse')
model.fit(trX, trY, nb_epoch=200, verbose=1)

weights = model.layers[0].get_weights()
w_final = weights[0][0][0]
b_final = weights[1][0]
print('Linear regression model is trained to have weight w: %.2f, b: %.2f' % (w_final, b_final))

model.save_weights("my_model.h5")

# model.load_weights('my_model_weights.h5')