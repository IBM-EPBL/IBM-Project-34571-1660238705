{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "45ea1ff3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np#used for numerical analysis\n",
    "import tensorflow #open source used for both ML and DL for computation\n",
    "from tensorflow.keras.models import Sequential #it is a plain stack of layers\n",
    "from tensorflow.keras import layers #A layer consists of a tensor-in tensor-out computation function\n",
    "#Dense layer is the regular deeply connected neural network layer\n",
    "from tensorflow.keras.layers import Dense,Flatten\n",
    "#Faltten-used fot flattening the input or change the dimension\n",
    "from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dropout #Convolutional layer\n",
    "#MaxPooling2D-for downsampling the image\n",
    "from keras.preprocessing.image import ImageDataGenerator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "31c076b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initializing the CNN\n",
    "classifier = Sequential()\n",
    "\n",
    "# First convolution layer and pooling\n",
    "classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))\n",
    "classifier.add(MaxPooling2D(pool_size=(2, 2)))\n",
    "\n",
    "# Second convolution layer and pooling\n",
    "classifier.add(Conv2D(32, (3, 3), activation='relu'))\n",
    "\n",
    "# input_shape is going to be the pooled feature maps from the previous convolution layer\n",
    "classifier.add(MaxPooling2D(pool_size=(2, 2)))\n",
    "\n",
    "# Flattening the layers\n",
    "classifier.add(Flatten())\n",
    "\n",
    "# Adding a fully connected layer\n",
    "classifier.add(Dense(units=128, activation='relu'))\n",
    "classifier.add(Dense(units=5, activation='softmax')) # softmax for more than 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "80e45b94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " conv2d (Conv2D)             (None, 62, 62, 32)        896       \n",
      "                                                                 \n",
      " max_pooling2d (MaxPooling2D  (None, 31, 31, 32)       0         \n",
      " )                                                               \n",
      "                                                                 \n",
      " conv2d_1 (Conv2D)           (None, 29, 29, 32)        9248      \n",
      "                                                                 \n",
      " max_pooling2d_1 (MaxPooling  (None, 14, 14, 32)       0         \n",
      " 2D)                                                             \n",
      "                                                                 \n",
      " flatten (Flatten)           (None, 6272)              0         \n",
      "                                                                 \n",
      " dense (Dense)               (None, 128)               802944    \n",
      "                                                                 \n",
      " dense_1 (Dense)             (None, 5)                 645       \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 813,733\n",
      "Trainable params: 813,733\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "classifier.summary()#summary of our model"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}