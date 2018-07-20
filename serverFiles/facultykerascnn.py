'''
kerascnnmnist.py
This program uses keras to build a CNN.
'''
#Import(ant) statements
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.models import Sequential, load_model
import keras.preprocessing.image
#import matplotlib.pylab as plt



#some definitions
batch_size=5
num_classes=69
epochs=10

#image dimensions
img_x, img_y = 512, 768	#would be 512, 768 for cf

#load data I think
train_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
#test_datagen= keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory("facultyImages/train", target_size=(512,768), batch_size=batch_size)

#validation_generator = test_datagen.flow_from_directory("colorferet/validate", target_size=(512, 768), batch_size=batch_size)


#x_train = x_train.reshape(x_train.shape[0], img_x, img_y, 1)
#x_test = x_test.reshape(x_test.shape[0], img_x, img_y, 1)
input_shape = (None, None, 3)

#convert data to correct type
#x_train = x_train.astype('float32')
#x_test =x_test.astype('float32')
#x_train /= 255
#x_test /= 255
#print('x_train shape:', x_train.shape)
#print(x_train.shape[0], 'train samples')
#print(x_test.shape[0], 'test samples')

#convert class vectors to binary class matrices for use in categorical_crossentropy
#y_train =keras.utils.to_categorical(y_train, num_classes)
#y_test = keras.utils.to_categorical(y_test, num_classes)

#Build the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(5,5), strides=(1,1), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
model.add(Conv2D(64, (5,5), activation='relu'))
model.add(GlobalAveragePooling2D())
model.add(Dense(1000, activation='relu'))	#In this tutorial, was 1000
model.add(Dense(num_classes, activation='softmax'))

#Train and evaluate the model
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.SGD(lr=0.01), metrics=['accuracy'])

#class AccuracyHistory(keras.callbacks.Callback):
#	def on_train_begin(self, logs={}):
#		self.acc=[]
#	def on_epoch_end(self, batch, logs={}):
#		self.acc.append(logs.get('acc'))

#history = AccuracyHistory()

model.fit_generator(train_generator, steps_per_epoch=100, epochs=epochs)

model.save('facultycnnmodel.h5')
#score = model.evaluate_generator(validation_generator,steps=800)
#print('Test loss:', score[0])
#print('Test accuracy:', score[1])
del model
#plt.plot(range(1,11), hitory.acc)
#plt.xlabel('Epochs')
#plt.ylabel('Accuracy')
#plt.show()
