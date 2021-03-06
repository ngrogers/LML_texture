import os

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import preprocessing


from google.colab import drive
drive.mount('/content/drive', force_remount=False)

x = np.load('/content/drive/MyDrive/colab_share/x2_retrain.npy')
y3 = np.load('/content/drive/MyDrive/colab_share/y_glyph_retrain.npy')
y = np.load('/content/drive/MyDrive/colab_share/y_retrain.npy')

model = keras.models.load_model("/content/drive/MyDrive/colab_share/trained_model05.h5")

z_score_preproc = preprocessing.StandardScaler()

x_use = x
x_use = z_score_preproc.fit_transform(x_use)
y_use = y3
y_pred1 = model(x_use, training=False)


fig=plt.figure(figsize=(6,6), dpi= 150, facecolor='w', edgecolor='k')
plt.plot(y_use+0.1*np.random.rand(np.size(y_use)),y_pred1, 'o', markersize=0.5, alpha=0.1)
