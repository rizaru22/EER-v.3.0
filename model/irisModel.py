import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load dataset contoh (Iris dataset)
data = load_iris()
X = data.data
y = data.target
print(y)
# Inisialisasi model yang akan digunakan (contoh: RandomForestClassifier)
model = RandomForestClassifier(n_estimators=100)

# Inisialisasi K-Fold Cross Validation
kfold = KFold(n_splits=10, shuffle=True, random_state=42)

# Lakukan K-Fold Cross Validation
scores = cross_val_score(model, X, y, cv=kfold)

# Output hasil cross-validation
for i, score in enumerate(scores):
    print(f'Fold {i+1}: {score:.4f}')

print(f'Rata-rata skor cross-validation: {np.mean(scores):.4f}')
