import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score,KFold
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import csv
import numpy as np


dataset=pd.read_csv('training-1.csv')
dataset['Label']=dataset['Label'].replace([0.0,1.0,2.0,3.0],['fear','sad','joy','anger'])
dataset=dataset.dropna()
X=dataset.drop(["Label"],axis=1)
Y=dataset["Label"]
gbModel=GradientBoostingClassifier(n_estimators=500,max_features="sqrt",random_state=42, subsample=1.0)
gbModel.fit(X,Y)
importance=gbModel.feature_importances_
featureCek=pd.Series(importance)
featurePenting=featureCek.nlargest(256)
indexFeaturePenting=featurePenting.index.array

print(indexFeaturePenting.tolist())

# pd.DataFrame(indexFeaturePenting).to_csv('sample.csv', header=False, index=False)  

X_fit=X.iloc[:,indexFeaturePenting]
Xtrain,Xtest,Ytrain,Ytest=train_test_split(X_fit,Y,test_size=0.3,random_state=42, stratify=Y)
# # print (type(X_fit))
# # print (list(X_fit))
#         # print(Ytest)
#         # import collections
#         # counter=collections.Counter(Ytest)
#         # print(counter)

# gbModel.fit(Xtrain,Ytrain)
# accuracy = gbModel.score(Xtest, Ytest)
# print(f'Accuracy: {accuracy}')


kf=KFold(n_splits=10, shuffle=True, random_state=42)

scores=cross_val_score(gbModel,X_fit,Y,cv=kf)


# Output hasil cross-validation
for i, score in enumerate(scores):
        print(f'Fold {i+1}: {score:.4f}')

print(f'Rata-rata skor cross-validation: {np.mean(scores):.4f}')

gbModel.fit(X_fit,Y)
fileModel='modelGB1.sav'
pickle.dump(gbModel,open(fileModel,'wb'))


loadModel=pickle.load(open(fileModel,'rb'))
hasil=loadModel.score(Xtest,Ytest)

print(hasil)