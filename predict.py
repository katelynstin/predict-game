import numpy as np
from joblib import load
import json

#my_graph = load('Boardgame.pkl')

#but how do 

def prediction(gamename):
    my_model = load('Boardgame.pkl')
    dummy = np.array(gamename)
    dummyT = dummy.reshape(1,-1)
    prediction = my_model.predict(dummyT)
    name_str = json.dumps(str(prediction[0]))
    return name_str

#def prediction(gamename):
 #   data = np.array(gamename)
 #   print(data)
  #  data = data.reshape(1, -1)
   # prediction = my_graph.predict(data)
    #print(prediction)



#test predict
print(prediction((8.02304,7.75493,32165,80,20000,2,5)))
