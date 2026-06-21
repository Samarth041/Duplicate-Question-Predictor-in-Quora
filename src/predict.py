#import warning
import os
import warnings

# Hide TensorFlow INFO and WARNING messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Hide oneDNN messages
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)
# Hide sklearn warnings
warnings.filterwarnings('ignore')
#--------------------------------------------------------------------------
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from src.preprocessing import preprocess
from src.feature_engineering import extract_features


model=load_model('models/hybrid_bilstm.keras')

with open('models/tokenizer.pkl','rb') as f:
    tokenizer=pickle.load(f)

with open('models/scaler.pkl','rb') as f:
    scaler=pickle.load(f)

MAX_LEN=50

def predict_duplicate(q1,q2):
    #preprocess
    q1=preprocess(q1)
    q2=preprocess(q2)

    #tokenize

    q1_seq=tokenizer.texts_to_sequences([q1])
    q2_seq=tokenizer.texts_to_sequences([q2])

    #padding
    q1_pad=pad_sequences(q1_seq,maxlen=MAX_LEN,padding='post')
    q2_pad=pad_sequences(q2_seq,maxlen=MAX_LEN,padding='post')

    #num_features

    num_features=extract_features(q1,q2)
    num_features = scaler.transform(num_features)

    #predict

    probability=model.predict([q1_pad,q2_pad,num_features],verbose=0)[0][0]

    print("\n************************************")

    print("Result")
    print("**************************************")

    if probability>=0.5:
        print("It is duplicate Question ✅")

    else:
        print("It is different question , not duplicate ❌")

    print(f"Probability : {probability:.4f}")
    print("------------------------")

    return probability



if __name__=="__main__":

    q1=input("Enter Question 1 :    ")
    q2=input("Enter Question 2 :    ")

    predict_duplicate(q1,q2)