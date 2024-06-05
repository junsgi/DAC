from tensorflow import keras
from keras.models import load_model
import numpy as np


def pre(obj):
  obj = np.array(obj)
  obj = np.abs(obj - 255)
  obj[obj > 0] = 0.00392156862745098
  return obj.reshape(-1, 28, 28)


def getPredict(t1, t2, t3):
  numberModel = load_model("numberModel.h5")
  operatorModel = load_model("operatorModel.h5")
  n1 = np.argmax(numberModel.predict(pre(t1)))
  o = np.argmax(operatorModel.predict(pre(t2)))
  n2 = np.argmax(numberModel.predict(pre(t3)))
  print()
  print(numberModel.predict(pre(t1)))
  print(numberModel.predict(pre(t3)))
  print(n1, o, n2)
  print()
