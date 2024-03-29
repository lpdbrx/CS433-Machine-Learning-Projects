from keras.models import Sequential
from keras.layers import Conv2DTranspose, Conv2D, Flatten, MaxPooling2D, LeakyReLU, Dropout, Activation, GlobalAveragePooling2D

def model_FCN(input_shape=(16, 16, 3)):
    alpha = 0.01
    model = Sequential()
    model.add(Conv2D(32, 2, input_shape=input_shape))
    model.add(LeakyReLU(alpha=alpha))
    model.add(Conv2D(32, 2))
    model.add(LeakyReLU(alpha=alpha))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, 2))
    model.add(LeakyReLU(alpha=alpha))
    model.add(Conv2D(64, 2))
    model.add(LeakyReLU(alpha=alpha))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2DTranspose(2, kernel_size=1, padding='valid'))
    model.add(GlobalAveragePooling2D())
    model.add(Activation('sigmoid'))
    return model