# import tensorflow as tf
# import torch
import math
import numpy as np
# import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# import scipy as sp

# Step1
###############################################
# Test case: all 0-9 jianan dataset
###############################################
# imgX=[mpl.image.imread("0.png"),
#       mpl.image.imread("1.png"),
#       mpl.image.imread("2.png"),
#       mpl.image.imread("3.png"),
#       mpl.image.imread("4.png"),
#       mpl.image.imread("5.png"),
#       mpl.image.imread("6.png"),
#       mpl.image.imread("7.png"),
#       mpl.image.imread("8.png"),
#       mpl.image.imread("9.png")]

# imgY=[mpl.image.imread("9.png")]
# output: [0.0]
# imgY=[mpl.image.imread("8.png")]
# output: [0.0]
# imgY=[mpl.image.imread("7.png")]
# output: [0.0]
# imgY=[mpl.image.imread("6.png")]
# output: [0.0]
# imgY=[mpl.image.imread("5.png")]
# output: [0.0]
# imgY=[mpl.image.imread("4.png")]
# output: [0.0]
# imgY=[mpl.image.imread("3.png")]
# # output: [0.0]
# imgY=[mpl.image.imread("2.png")]
# output: [0.0]
# imgY=[mpl.image.imread("1.png")]
# output: [0.0]

###############################################
# Test case: 0-9 separate hand writting
###############################################

# imgX=[mpl.image.imread("0.png"),
#       mpl.image.imread("0_1.png"),
#       mpl.image.imread("0_2.png"),
#       mpl.image.imread("0_3.png")]
#
# imgY=[mpl.image.imread("0_4.png")]
# output: [0.09375]

# imgX=[mpl.image.imread("0.png"),
#       mpl.image.imread("0_1.png"),
#       mpl.image.imread("0_2.png"),
#       mpl.image.imread("0_3.png")]
#
# imgY=[mpl.image.imread("1_1.png")]
# output: [0.10546875]

# imgX=[mpl.image.imread("1.png"),
#       mpl.image.imread("1_4.png"),
#       mpl.image.imread("1_2.png"),
#       mpl.image.imread("1_3.png")]
#
# imgY=[mpl.image.imread("1_1.png")]
# output: [0.03125]

# imgX=[mpl.image.imread("1.png"),
#       mpl.image.imread("1_4.png"),
#       mpl.image.imread("1_2.png"),
#       mpl.image.imread("1_3.png")]
#
# imgY=[mpl.image.imread("0.png")]
# output: [0.10546875]

# imgX=[mpl.image.imread("2.png"),
#       mpl.image.imread("2_4.png"),
#       mpl.image.imread("2_2.png"),
#       mpl.image.imread("2_3.png")]
#
# imgY=[mpl.image.imread("2_1.png")]
# output: [0.046875]

# imgX=[mpl.image.imread("3.png"),
#       mpl.image.imread("3_4.png"),
#       mpl.image.imread("3_2.png"),
#       mpl.image.imread("3_3.png")]
#
# imgY=[mpl.image.imread("3_1.png")]
# output: [0.109375]

# imgX=[mpl.image.imread("3.png"),
#       mpl.image.imread("3_4.png"),
#       mpl.image.imread("3_2.png"),
#       mpl.image.imread("3_3.png")]
#
# imgY=[mpl.image.imread("0_1.png")]
# output: [0.15625]


# imgX=[mpl.image.imread("4.png"),
#       mpl.image.imread("4_4.png"),
#       mpl.image.imread("4_2.png"),
#       mpl.image.imread("4_3.png")]
#
# imgY=[mpl.image.imread("4_1.png")]
# output: [0.12109375]

# imgX=[mpl.image.imread("4.png"),
#       mpl.image.imread("4_4.png"),
#       mpl.image.imread("4_2.png"),
#       mpl.image.imread("4_3.png")]
#
# imgY=[mpl.image.imread("3_1.png")]
# output: [0.12890625]


# imgX=[mpl.image.imread("5.png"),
#       mpl.image.imread("5_4.png"),
#       mpl.image.imread("5_2.png"),
#       mpl.image.imread("5_3.png")]
#
# imgY=[mpl.image.imread("5_1.png")]
# output: [0.06640625]

# imgX=[mpl.image.imread("5.png"),
#       mpl.image.imread("5_4.png"),
#       mpl.image.imread("5_2.png"),
#       mpl.image.imread("5_3.png")]
#
# imgY=[mpl.image.imread("4_1.png")]
# output: [0.140625]

# imgX=[mpl.image.imread("6.png"),
#       mpl.image.imread("6_4.png"),
#       mpl.image.imread("6_2.png"),
#       mpl.image.imread("6_3.png")]
#
# imgY=[mpl.image.imread("6_1.png")]
# output: [0.140625]

# imgX=[mpl.image.imread("7.png"),
#       mpl.image.imread("7_4.png"),
#       mpl.image.imread("7_2.png"),
#       mpl.image.imread("7_3.png")]
#
# imgY=[mpl.image.imread("7_1.png")]
# output: [0.03515625]

# imgX=[mpl.image.imread("7.png"),
#       mpl.image.imread("7_4.png"),
#       mpl.image.imread("7_2.png"),
#       mpl.image.imread("7_3.png")]
#
# imgY=[mpl.image.imread("1_1.png")]
# output: [0.07421875]

# imgX=[mpl.image.imread("7.png"),
#       mpl.image.imread("7_4.png"),
#       mpl.image.imread("7_2.png"),
#       mpl.image.imread("7_3.png")]
#
# imgY=[mpl.image.imread("3_1.png")]
# output: [0.125]

# imgX=[mpl.image.imread("8.png"),
#       mpl.image.imread("8_4.png"),
#       mpl.image.imread("8_2.png"),
#       mpl.image.imread("8_3.png")]
#
# imgY=[mpl.image.imread("8_1.png")]
# output: [0.14453125]

# imgX=[mpl.image.imread("8.png"),
#       mpl.image.imread("8_4.png"),
#       mpl.image.imread("8_2.png"),
#       mpl.image.imread("8_3.png")]
#
# imgY=[mpl.image.imread("0_1.png")]
# output: [0.18359375]

# imgX=[mpl.image.imread("9.png"),
#       mpl.image.imread("9_4.png"),
#       mpl.image.imread("9_2.png"),
#       mpl.image.imread("9_3.png")]
#
# imgY=[mpl.image.imread("9_1.png")]
# output: [0.07421875]


####################################
# Test case: all 0-9 hand writting
####################################
# imgX=[mpl.image.imread("9.png"),
#       mpl.image.imread("9_4.png"),
#       mpl.image.imread("9_2.png"),
#       mpl.image.imread("9_3.png"),
#       mpl.image.imread("8.png"),
#       mpl.image.imread("8_4.png"),
#       mpl.image.imread("8_2.png"),
#       mpl.image.imread("8_3.png"),
#       mpl.image.imread("7.png"),
#       mpl.image.imread("7_4.png"),
#       mpl.image.imread("7_2.png"),
#       mpl.image.imread("7_3.png"),
#       mpl.image.imread("6.png"),
#       mpl.image.imread("6_4.png"),
#       mpl.image.imread("6_2.png"),
#       mpl.image.imread("6_3.png"),
#       mpl.image.imread("5.png"),
#       mpl.image.imread("5_4.png"),
#       mpl.image.imread("5_2.png"),
#       mpl.image.imread("5_3.png"),
#       mpl.image.imread("4.png"),
#       mpl.image.imread("4_4.png"),
#       mpl.image.imread("4_2.png"),
#       mpl.image.imread("4_3.png"),
#       mpl.image.imread("3.png"),
#       mpl.image.imread("3_4.png"),
#       mpl.image.imread("3_2.png"),
#       mpl.image.imread("3_3.png"),
#       mpl.image.imread("2.png"),
#       mpl.image.imread("2_4.png"),
#       mpl.image.imread("2_2.png"),
#       mpl.image.imread("2_3.png"),
#       mpl.image.imread("1.png"),
#       mpl.image.imread("1_4.png"),
#       mpl.image.imread("1_2.png"),
#       mpl.image.imread("1_3.png")]

# imgY=[mpl.image.imread("9_1.png")]
# output: [0.890625]
# imgY=[mpl.image.imread("8_1.png")]
# output: [0.859375]
# imgY=[mpl.image.imread("7_1.png")]
# output: [0.93359375]
# imgY=[mpl.image.imread("6_1.png")]
# output: [0.875]
# imgY=[mpl.image.imread("5_1.png")]
# output: [0.890625]
# imgY=[mpl.image.imread("4_1.png")]
# output: [0.890625]
# imgY=[mpl.image.imread("3_1.png")]
# # output: [0.890625]
# imgY=[mpl.image.imread("2_1.png")]
# output: [0.88671875]
# imgY=[mpl.image.imread("1_1.png")]
# output: [0.9609375]

####################################
# Test case: all 0-9 well known font
####################################
# imgX=[mpl.image.imread("well_known_fonts/9_5.png"),
#       mpl.image.imread("well_known_fonts/9_4.png"),
#       mpl.image.imread("well_known_fonts/9_2.png"),
#       mpl.image.imread("well_known_fonts/9_3.png"),
#       mpl.image.imread("well_known_fonts/8_5.png"),
#       mpl.image.imread("well_known_fonts/8_4.png"),
#       mpl.image.imread("well_known_fonts/8_2.png"),
#       mpl.image.imread("well_known_fonts/8_3.png"),
#       mpl.image.imread("well_known_fonts/7_5.png"),
#       mpl.image.imread("well_known_fonts/7_4.png"),
#       mpl.image.imread("well_known_fonts/7_2.png"),
#       mpl.image.imread("well_known_fonts/7_3.png"),
#       mpl.image.imread("well_known_fonts/6_5.png"),
#       mpl.image.imread("well_known_fonts/6_4.png"),
#       mpl.image.imread("well_known_fonts/6_2.png"),
#       mpl.image.imread("well_known_fonts/6_3.png"),
#       mpl.image.imread("well_known_fonts/5_5.png"),
#       mpl.image.imread("well_known_fonts/5_4.png"),
#       mpl.image.imread("well_known_fonts/5_2.png"),
#       mpl.image.imread("well_known_fonts/5_3.png"),
#       mpl.image.imread("well_known_fonts/4_5.png"),
#       mpl.image.imread("well_known_fonts/4_4.png"),
#       mpl.image.imread("well_known_fonts/4_2.png"),
#       mpl.image.imread("well_known_fonts/4_3.png"),
#       mpl.image.imread("well_known_fonts/3_5.png"),
#       mpl.image.imread("well_known_fonts/3_4.png"),
#       mpl.image.imread("well_known_fonts/3_2.png"),
#       mpl.image.imread("well_known_fonts/3_3.png"),
#       mpl.image.imread("well_known_fonts/2_5.png"),
#       mpl.image.imread("well_known_fonts/2_4.png"),
#       mpl.image.imread("well_known_fonts/2_2.png"),
#       mpl.image.imread("well_known_fonts/2_3.png"),
#       mpl.image.imread("well_known_fonts/1_5.png"),
#       mpl.image.imread("well_known_fonts/1_4.png"),
#       mpl.image.imread("well_known_fonts/1_2.png"),
#       mpl.image.imread("well_known_fonts/1_3.png")]
#
# imgY=[mpl.image.imread("well_known_fonts/9_1.png")]
# hand written output: [0.890625]
# well known fonts output: [0.9765625]
# imgY=[mpl.image.imread("well_known_fonts/8_1.png")]
# hand written output: [0.859375]
# well known fonts output: [0.9609375]
# imgY=[mpl.image.imread("well_known_fonts/7_1.png")]
# hand written output: [0.93359375]
# well known fonts output: [0.984375]
# imgY=[mpl.image.imread("well_known_fonts/6_1.png")]
# hand written output: [0.875]
# well known fonts output: [0.97265625]
# imgY=[mpl.image.imread("well_known_fonts/5_1.png")]
# hand written output: [0.890625]
# well known fonts output: [0.984375]
# imgY=[mpl.image.imread("well_known_fonts/4_1.png")]
# hand written output: [0.890625]
# well known fonts output: [0.98046875]
# imgY=[mpl.image.imread("well_known_fonts/3_1.png")]
# hand written output: [0.890625]
# well known fonts output: [0.96875]
# imgY=[mpl.image.imread("well_known_fonts/2_1.png")]
# hand written output: [0.88671875]
# well known fonts output: [0.95703125]
# imgY=[mpl.image.imread("well_known_fonts/1_1.png")]
# hand written output: [0.9609375]
# well known fonts output: [0.97265625]

# Arial _1
###############################################
# Test case: all 0-9 well known font Arial _1
###############################################
imgX=[mpl.image.imread("well_known_fonts/9_1.png"),
      mpl.image.imread("well_known_fonts/8_1.png"),
      mpl.image.imread("well_known_fonts/7_1.png"),
      mpl.image.imread("well_known_fonts/6_1.png"),
      mpl.image.imread("well_known_fonts/5_1.png"),
      mpl.image.imread("well_known_fonts/4_1.png"),
      mpl.image.imread("well_known_fonts/3_1.png"),
      mpl.image.imread("well_known_fonts/2_1.png"),
      mpl.image.imread("well_known_fonts/1_1.png")]

imgY=[mpl.image.imread("well_known_fonts/9_1.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.9765625]
# Arial output: [0.015625]
# imgY=[mpl.image.imread("well_known_fonts/8_1.png")]
# hand written output: [0.859375]
# all well known fonts output: [0.9609375]
# Arial output: [0.015625]
# imgY=[mpl.image.imread("well_known_fonts/7_1.png")]
# hand written output: [0.93359375]
# all well known fonts output: [0.984375]
# Arial output: [0.01953125]
# imgY=[mpl.image.imread("well_known_fonts/6_1.png")]
# hand written output: [0.875]
# all well known fonts output: [0.97265625]
# Arial output: [0.01171875]
# imgY=[mpl.image.imread("well_known_fonts/5_1.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.984375]
# Arial output: [0.01953125]
# imgY=[mpl.image.imread("well_known_fonts/4_1.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.98046875]
# Arial output: [0.00390625]
# imgY=[mpl.image.imread("well_known_fonts/3_1.png")]
# hand written output: [0.890625]
# Arial output: [0.03515625]
# imgY=[mpl.image.imread("well_known_fonts/2_1.png")]
# hand written output: [0.88671875]
# Arial output: [0.04296875]
# imgY=[mpl.image.imread("well_known_fonts/1_1.png")]
# hand written output: [0.9609375]
# Arial output: [0.03125]


# Bodoni MT Heavy Italic _2
###############################################################
# Test case: all 0-9 well known font Bodoni MT Heavy Italic _2
###############################################################
# imgX=[mpl.image.imread("well_known_fonts/9_2.png"),
#       mpl.image.imread("well_known_fonts/8_2.png"),
#       mpl.image.imread("well_known_fonts/7_2.png"),
#       mpl.image.imread("well_known_fonts/6_2.png"),
#       mpl.image.imread("well_known_fonts/5_2.png"),
#       mpl.image.imread("well_known_fonts/4_2.png"),
#       mpl.image.imread("well_known_fonts/3_2.png"),
#       mpl.image.imread("well_known_fonts/2_2.png"),
#       mpl.image.imread("well_known_fonts/1_2.png")]

# imgY=[mpl.image.imread("well_known_fonts/9_2.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.9765625]
# Arial output:
# Bodoni output: [0.0234375]
# imgY=[mpl.image.imread("well_known_fonts/8_2.png")]
# hand written output: [0.859375]
# all well known fonts output: [0.9609375]
# Arial output:
# Bodoni output: [0.01171875]
# imgY=[mpl.image.imread("well_known_fonts/7_2.png")]
# hand written output: [0.93359375]
# all well known fonts output: [0.984375]
# Arial output:
# Bodoni output: [0.0390625]
# imgY=[mpl.image.imread("well_known_fonts/6_2.png")]
# hand written output: [0.875]
# all well known fonts output: [0.97265625]
# Arial output:
# Bodoni output: [0.0234375]
# imgY=[mpl.image.imread("well_known_fonts/5_2.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.984375]
# Arial output:
# Bodoni output:
# imgY=[mpl.image.imread("well_known_fonts/4_2.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.98046875]
# Arial output:
# Bodoni output:
# imgY=[mpl.image.imread("well_known_fonts/3_2.png")]
# hand written output: [0.890625]
# Arial output:
# Bodoni output:
# imgY=[mpl.image.imread("well_known_fonts/2_2.png")]
# hand written output: [0.88671875]
# Arial output:
# Bodoni output:
# imgY=[mpl.image.imread("well_known_fonts/1_2.png")]
# hand written output: [0.9609375]
# Arial output:
# Bodoni output:

# Constantia Bold _3
###############################################################
# Test case: all 0-9 well known font Bodoni MT Heavy Italic _2
###############################################################
# imgX=[mpl.image.imread("well_known_fonts/9_3.png"),
#       mpl.image.imread("well_known_fonts/8_3.png"),
#       mpl.image.imread("well_known_fonts/7_3.png"),
#       mpl.image.imread("well_known_fonts/6_3.png"),
#       mpl.image.imread("well_known_fonts/5_3.png"),
#       mpl.image.imread("well_known_fonts/4_3.png"),
#       mpl.image.imread("well_known_fonts/3_3.png"),
#       mpl.image.imread("well_known_fonts/2_3.png"),
#       mpl.image.imread("well_known_fonts/1_3.png")]

# imgY=[mpl.image.imread("well_known_fonts/9_3.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.9765625]
# Arial output: [0.00390625]
# Bodoni output: [0.0]
# Constantia output: [0.015625]
# imgY=[mpl.image.imread("well_known_fonts/8_3.png")]
# hand written output: [0.859375]
# all well known fonts output: [0.9609375]
# Arial output: [0.0]
# Bodoni output: [0.0]
# Constantia output: [0.01171875]
# imgY=[mpl.image.imread("well_known_fonts/7_3.png")]
# hand written output: [0.93359375]
# all well known fonts output: [0.984375]
# Arial output: [0.0]
# Bodoni output: [0.0]
# Constantia output: [0.01953125]
# imgY=[mpl.image.imread("well_known_fonts/6_3.png")]
# hand written output: [0.875]
# all well known fonts output: [0.97265625]
# Arial output: [0.0]
# Bodoni output: [0.0]
# Constantia output: [0.02734375]
# imgY=[mpl.image.imread("well_known_fonts/5_3.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.984375]
# Arial output: [0.00390625]
# Bodoni output: [0.0]
# Constantia output: [0.01953125]
# imgY=[mpl.image.imread("well_known_fonts/4_3.png")]
# hand written output: [0.890625]
# all well known fonts output: [0.98046875]
# Arial output: [0.01171875]
# Bodoni output: [0.0]
# Constantia output: [0.0234375]
# imgY=[mpl.image.imread("well_known_fonts/3_3.png")]
# hand written output: [0.890625]
# Arial output: [0.0]
# Bodoni output: [0.0]
# Constantia output: [0.01171875]
# imgY=[mpl.image.imread("well_known_fonts/2_3.png")]
# hand written output: [0.88671875]
# Arial output: [0.0]
# Bodoni output: [0.0]
# Constantia output: [0.03515625]
# imgY=[mpl.image.imread("well_known_fonts/1_3.png")]
# hand written output: [0.9609375]
# Arial output: [0.0]
# Bodoni output: [0.0]
# Constantia output: [0.0390625]

# Ebrima _4
# Dubai _5

# for i in range(1,11):
#     plt.subplot(2,5,i)
#     plt.imshow(imgX[i-1])
    # plt.show()

# Step2
class Perceptron(object):
    def __init__(self, input_dimensions = 256, number_of_classes = 256, seed = None):
        if seed != None:
            np.random.seed(seed)
        self.input_dimensions = input_dimensions
        self.number_of_classes = number_of_classes
        self._initialize_weights()
    def _initialize_weights(self):
        self.weights = np.random.randn(self.number_of_classes, self.input_dimensions)
        print('self.weights before: %s' % self.weights)
        # self.weights = np.random.randn(self.number_of_classes, self.input_dimensions + 1)
        # print('self.weights after: %s' % self.weights)
    def initialize_all_weights_to_zeros(self):
        self.weights = np.zeros((self.number_of_classes, self.input_dimensions + 1))

    def predict(self, X):
        # print(X.shape[0],X.shape[1])
        # print(self.weights.shape[0],self.weights.shape[1])
        pred=[]
        for i in range(0,X.shape[0]):
            activation=[]
            for j in range(0,self.weights.shape[0]):
                summation = np.dot(X[i,:],((self.weights[j,:self.weights.shape[1]-1].T))) + self.weights[j][self.weights.shape[1]-1]
                if summation > 0.85:
                    activation.append(1)
                else:
                    activation.append(0)
            pred.append(activation)
        return(pred)

    def print_weights(self):
        return(self.weights)

    def train(self, X, Y, img_amount, num_epochs = 10, alpha = 0.001):
        # outfile = open('debug.txt', 'a')
        # outfile.write('self.weights[1,:] starts:\n')
        # outfile.write(str(self.weights[1,:]))
        # outfile.write('\n')
        # outfile.write('self.weights[1,:] starts:\n')
        # outfile.close()
        for j in range(self.weights.shape[0]):  #train 256 weights for each output pixels
            treat = float(0.0)
            for k in range(self.weights.shape[1] - 1):
                tempsum = float(0.0)
                for i in range(img_amount):                 #train its pixels in each picture
                    temp = np.dot(X[i,:],self.weights[j,:self.weights.shape[1]-1].T) + self.weights[j][self.weights.shape[1]-1]
                    temp = temp - Y[i][j]
                    # print('temp: %s' % temp)
                    # print('Y[i][j]: %s' % Y[i][j])
                    # print('X[i,:]: %s' % X[i,:])
                    # print('Y[i][j]: %s' % Y[i][j])
                    # print('self.weights.shape[1] - 1].T: %s' % self.weights[j,:self.weights.shape[1]-1].T)
                    # print('self.weights.shape: %s' % str(self.weights.shape))
                    tempsum += X[i][k] * temp
                    treat += temp
                self.weights[j][k] -= tempsum * alpha
                self.weights[j][self.weights.shape[1] - 1] -= treat * alpha / 256
                # print('self.weights[j][k]: %s' % self.weights[j][k])
                # print('self.weights[j][self.weights.shape[1] - 1]: %s' % self.weights[j][self.weights.shape[1] - 1])

    def calculate_percent_error(self, img_amount, X, Y):
        y_ = self.predict(X)
        sumary = 0
        error = 0
        for j in range(0,img_amount):
            for i in range(0,256):
                if y_[j][i] != Y[j][i]:
                    error += 1
                sumary += 1
        error_percent = float(error) / float(sumary)
        print(float(error),float(sumary))
        print('y_: %s' % y_)
        print('Y: %s' % Y)
        print('imgX1: %s' % str(imgX[1]))
        # outfile = open('debug.txt', 'a')
        # for i in imgX[1]:
        #     outfile.write(str(i))
        # outfile.close()
        print('processImageReverse(y_): %s' % str(np.array(y_[0]).reshape((16, 16))))
        print('y_ type: %s' % type(y_))
        print('Y type: %s' % type(Y))
        print('imgX1 type: %s' % type(imgX[1]))
        print('imgX1 shape: %s' % str(imgX[1].shape))
        print('processImageReverse(y_) shape: %s' % str(processImageReverse(y_).shape))
        plt.imshow(np.array(Y[0]).reshape((16, 16)), cmap='gray', vmin=0, vmax=1)
        plt.show()
        plt.imshow(np.array(y_[0]).reshape((16, 16)), cmap='gray', vmin=0, vmax=1)
        plt.show()
        return error_percent


###############################################
#define the function to output weights in files
###############################################
def printWetInFile(my_weight, num):
    f = open("weights" + num + ".txt", "w")
    for i in range(0,256):
        s = str(my_weight[i])
        f.write(s)
    f.close()

def processImage(Image, img_amount):
    img=[]
    ytrain=[]
    sumbl=0
    for i in range(img_amount):
        it=[]
        biy=[]
        # print('Image[i]: %s' % Image[i])
        for j in Image[i]:
            # print('j: %s' % j)
            for k in j:
                it.append(255) if k[0] > 0.85 else it.append(0)
                biy.append(1) if k[0] > 0.85 else biy.append(0)
                if k[0] == 0: sumbl += 1
        img.append(it)
        ytrain.append(biy)
    # print('ytrain: %s' % ytrain)
    # print('ytrain len: %s' % len(ytrain))
    # print('sumbl: %s' % sumbl)
    return np.array(img),ytrain,sumbl


def processImageReverse(Image):
    img=[]
    for i in range(1):
        it=[]
        row=[]
        columns=[]
        pos=0
        print(Image)
        for j in Image[i]:
            columns.append(255) if j > 0 else columns.append(0)
            columns.append(columns[0])
            columns.append(columns[0])
            row.append(columns)
            columns.clear()

            if pos % 16 == 15:
                it.append(row)
                row.clear()
            pos+=1
        img.append(it)
    return np.array(img)
print('-----------------------debug1')
#step2_3()
input_dimensions = 256
number_of_classes = 256

model = Perceptron(input_dimensions=input_dimensions, number_of_classes=number_of_classes, seed=1)
printWetInFile(model.print_weights(), "1")
imageX, y_train_X, sumblack_X = processImage(imgX, len(imgX))
imageY, y_train_Y, sumblack_Y = processImage(imgY, len(imgY))

model.initialize_all_weights_to_zeros()
percent_error=[]
print('-----------------------debug2')
for k in range (1):
    print('-----------------------debug3 k: %s' % k)
    model.train(imageX, y_train_X, len(imageX), num_epochs=1, alpha=0.000002)
    # percent_error.append(model.calculate_percent_error(imageX,y_train_X))
    percent_error.append(model.calculate_percent_error(len(imageY), imageY, y_train_Y))
    # print(model.print_weights())
print("******  Percent Error ******\\n" , percent_error)
printWetInFile(model.print_weights(), "2")


# step 4
def Compute_Metrics(X, Y, sumbl):
    y_pred = model.predict(X)
    h=0
    fa = 0
    for i in range(10):
        for j in range(256):
            if y_pred[i][j] == 0:
                if Y[i][j] == 0: h += 1
                if Y[i][j] == 1: fa += 1
    print(h,fa)
    h = float(h) / float(sumbl)
    fa = float(fa) / float(sumbl)
    return h, fa


#step 5
def Normalize(X):
    summary = 0.0
    for i in X:
        summary += float(i) * float(i)
    summary = math.sqrt(summary)
    return summary

def Gaussian_noise():
    #Generate noise
    Noise=[]
    st_devia=(0.001,0.002,0.003,0.005,0.01,0.02,0.03,0.05,0.1)
    for i in range(9):
        x = np.random.normal(loc=0, scale=st_devia[i], size=25)
        Noise.append(x)

    #Add noise to picture 1 - 9
    imageNoise = y_train_X.copy()
    for i in range(1,10):
        newpos = np.random.randint(256, size = (25))
        #print(newpos)
        for j in range(25):
            imageNoise[i][newpos[j]] += Noise[i-1][j]
        #print(imageNoise[i])

        #renormalize
        magni = Normalize(imageNoise[i])
        for j in range(256):
            imageNoise[i][j] = float(imageNoise[i][j]) / magni

    return imageNoise


Fh, Ffa = Compute_Metrics(imageX, y_train_X, sumblack_X)
# TODO image output
# print(Fh, Ffa)
# print('imageX: %s' % imageX)
# print('y_train_X: %s' % y_train_X)
# print('sumblack: %s' % sumblack_X)

Fh, Ffa = Compute_Metrics(imageY, y_train_X, sumblack_Y)
# print(Fh, Ffa)
# print('imageY: %s' % imageY)
# print('y_train_Y: %s' % y_train_Y)
# print('sumblack_Y: %s' % sumblack_Y)
