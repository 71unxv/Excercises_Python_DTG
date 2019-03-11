import pickle
def read(filename):
    with open(filename,'rb') as inputdata: #python3 :open(....,'rb')
        hasilread = pickle.load(inputdata)
    return hasilread

data = read('dataDummy.MT')

#    data
#    self.Appres = AppRes
#    self.Phase = Phase
#    self.Frequency = Frequency
#    
#    model
#    
    

