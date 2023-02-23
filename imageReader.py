import gzip
import pickle
import sys
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)

def intToOutput(entier):
    out=np.zeros((10,1))
    out[entier] = 1
    return out


def loadMnist():
    with gzip.open('data/mnist.pkl.gz','r') as fin:
        data=[] 
        trainingData, validationData, testData =pickle.load(fin, encoding='latin1')       
        return (trainingData, validationData, testData)


def getMnistImage():
    #retourne un tuple contenant (TrainingData, TestData, TestData2)
    #TrainingData contient dans un tuple (50 000 images écrites à la main, que devrait retourner le réseau de neuronne en regardant l'image)
    data = loadMnist()
    
    newTrainingData = [x for x in data[0][0]],[intToOutput(y) for y in data[0][1]]
    validationData = [x for x in data[1][0]],[intToOutput(y) for y in data[1][1]]
    testData = [x for x in data[2][0]],[intToOutput(y) for y in data[2][1]]
    print(newTrainingData[1])
    return newTrainingData,validationData,testData  
    


