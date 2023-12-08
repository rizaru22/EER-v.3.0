import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score,KFold
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import numpy as np

dataset=pd.read_csv('training-2.csv')
# dataset['Label']=dataset['Label'].replace([0.0,1.0,2.0,3.0],['fear','sad','joy','anger'])
dataset=dataset.dropna()
X=dataset.drop(["Label"],axis=1)
Y=dataset["Label"]
rfModel=GradientBoostingClassifier(n_estimators=143,max_features="sqrt",random_state=42)
# rfModel.fit(X,Y)

# importance=rfModel.feature_importances_
# featureCek=pd.Series(importance)
# featurePenting=featureCek.nlargest(254)
# indexFeaturePenting=featurePenting.index.array

# X_fit=X.iloc[:,indexFeaturePenting]

kf=KFold(n_splits=10, shuffle=True, random_state=42)

scores=cross_val_score(rfModel,X,Y,cv=kf)


# Output hasil cross-validation
for i, score in enumerate(scores):
    print(f'Fold {i+1}: {score:.4f}')

print(f'Rata-rata skor cross-validation: {np.mean(scores):.4f}')


# fileModel='modelRF.sav'
# pickle.dump(rfModel,open(fileModel,'wb'))


# loadModel=pickle.load(open(fileModel,'rb'))
# hasil=loadModel.score(X_fit,Y)
# print(hasil)