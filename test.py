from os import replace
import imageReader
import numpy as np



def sigmoid(X):
    return 1/(1+np.exp(-X))
       

def sampleData(testData, tailleSample):
    aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
    return np.random.choice(testData, tailleSample, replace = False)
    



class network(object):
    def __init__(self,sizeLayers) : # sizeLayers tableau contenant le nombre de neuronnes dans chaque couche (ex: [1,3,5])
        self.nombreCouche=len(sizeLayers)
        self.nombreNeuronnes=sizeLayers
        
        self.weight=[]
        self.biais=[]
        
        for i in range(1,len(sizeLayers)): # pour toutes les couches sauf la première
            self.biais.append(np.random.randn(sizeLayers[i],1)) #crée un biais pour chaque neuronne de la couche i
            
            C=[]
            for j in range(sizeLayers[i]):  #pour chaque neuronne de la couche i crée un lien (en définissant le poids) avec tous les neuronnes de la couche i-1 
                C.append(np.random.rand(sizeLayers[i-1]))
            self.weight.append(np.array(C))

        self.biais= np.array(self.biais, dtype="object")
        self.weight=np.array(self.weight, dtype="object")   #lilste de neuronnes
    def  backPropagation(self, input, desiredOutput):
        
        realOutput=self.resultat(input)
        
        


    def gradientDescent(self, NumberRound, tailleSample, learningRate):
        testData = imageReader.getMnistImage()[0]
        
        for i in range(NumberRound):
            extraitMnist=sampleData(testData, tailleSample)
            for extrait in extraitMnist:
                nabla_b = [np.zeros(b.shape) for b in self.biais]
                nabla_w = [np.zeros(w.shape) for w in self.weight]
                
                


        


    def resultat(self,inputVect):
        #calcul les valeurs en sortie en fonction des valeurs en entrée
        for i in range(self.nombreCouche-1): #pour chaque couche
            outputVect=[]
            for j in range(len(self.weight[i])): #pour chaque neuronne dans cette couche
                outputVect.append(np.ndarray.item(np.dot(self.weight[i][j],inputVect)+np.array(self.biais[i][j])))
            inputVect=outputVect
            
        return outputVect
            

            




    #test __init__ dans network
# print(network([3,4,6]).weight[0][0])
# print(network([3,4,6]).biais)

        #test résultat
a=network([3,4,6])
print(a.resultat(np.array([1,2,3])))