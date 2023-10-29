'''
    Breast cancer wisconsin dataset analysis :
        1- Train an ML model to classify the data (target : tumeur malignes/benignes)
        2- Docker work


'''

#imports
import pandas as pd 
import numpy as np 


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

#import the dataset 
from sklearn.datasets import load_breast_cancer



#get the data 
brCancer = load_breast_cancer()


print(brCancer.DESCR)

print(brCancer.target_names)


#print(brCancer.feature_names)


#convert to dataframe 
brCancerData = pd.DataFrame(data=brCancer.data, columns=brCancer.feature_names)
print(brCancerData.head())



#step 1 : define the features and the target

X = brCancerData #Features
y = brCancer.target #Target 



#step 2 : split dataset into training and test sets
X_train , X_test, y_train, y_test = train_test_split(X, y , test_size=0.2, random_state=42)


#step 3 : initialize the rfc 
rfc = RandomForestClassifier(n_estimators=100, random_state=42)

#step 4 : train the classifier on the training data 
rfc.fit(X_train, y_train)

#step 5 : make predictions on the test data 
y_pred = rfc.predict(X_test)


#model performance 
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

#display classif report (precision, recall , f1 score)
print(classification_report(y_test, y_pred, target_names=brCancer.target_names))


'''
    Save the model 

'''

import joblib

joblib.dump(rfc, 'model.pkl')















