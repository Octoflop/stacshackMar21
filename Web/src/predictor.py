from sklearn import svm
import pickle
import cv2
import os
class Predictor:

    RECOGNISER_NAME = 'assets/recogniser'
    
    def __init__(self):
        self.classifier = pickle.load(open(self.RECOGNISER_NAME, 'rb'))

    def do_prediction(self, filename):
        im = cv2.imread(filename, 1)
        im_small = cv2.resize(im, (150,150))
        cv2.imwrite(filename, im_small)
        im_gray = cv2.cvtColor(im_small, cv2.COLOR_RGB2GRAY)
        output = im_gray.flatten().tolist()
        result = self.classifier.predict([output])
        if (result != 1):
            os.remove(filename)    
        return result[0]
