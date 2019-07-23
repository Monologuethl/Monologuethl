from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout

model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(100, 100, 32)))
# This ads a Convolutional layer with 64 filters of size 3 * 3 to the graph
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten())
# -------------------------------------------------------------------------------------
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.compile(loss='binary_crossentropy', optimizer='rmsprop')

# 指定优化器和损失函数

# 随机梯度下降
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

x_train = ''
y_train = ''

x_test = ''
y_test = ''
# 向模型中输入数据,指定 batch_size 和 epochs 来训练
model.fit(x_train, y_train, batch_size=32, epochs=10)
# 测试模型的性能
score = model.evaluate(x_test, y_test, batch_size=32)

