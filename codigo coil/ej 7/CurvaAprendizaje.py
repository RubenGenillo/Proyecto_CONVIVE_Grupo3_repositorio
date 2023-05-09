from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# cargar el conjunto de datos
df = pd.read_csv('codigo coil/clusterizado_1.csv', sep=';')

# separar en X e y
X = df.drop(['cluster'], axis=1)
y = df['cluster']

# dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)
accuracy_gnb = accuracy_score(y_test, y_pred_gnb)
f1_gnb = f1_score(y_test, y_pred_gnb, average='weighted')
report_gnb = classification_report(y_test, y_pred_gnb, zero_division=0)

# MultinomialNB
mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_pred_mnb = mnb.predict(X_test)
accuracy_mnb = accuracy_score(y_test, y_pred_mnb)
f1_mnb = f1_score(y_test, y_pred_mnb, average='weighted')
report_mnb = classification_report(y_test, y_pred_mnb, zero_division=0)

# ComplementNB
cnb = ComplementNB()
cnb.fit(X_train, y_train)
y_pred_cnb = cnb.predict(X_test)
accuracy_cnb = accuracy_score(y_test, y_pred_cnb)
f1_cnb = f1_score(y_test, y_pred_cnb, average='weighted')
report_cnb = classification_report(y_test, y_pred_cnb, zero_division=0)

# BernoulliNB
bnb = BernoulliNB()
bnb.fit(X_train, y_train)
y_pred_bnb = bnb.predict(X_test)
accuracy_bnb = accuracy_score(y_test, y_pred_bnb)
f1_bnb = f1_score(y_test, y_pred_bnb, average='weighted')
report_bnb = classification_report(y_test, y_pred_bnb, zero_division=0)

print("GaussianNB Accuracy:", accuracy_gnb)
print("GaussianNB F1 Score:", f1_gnb)
print("GaussianNB Classification Report:\n", report_gnb)

print("MultinomialNB Accuracy:", accuracy_mnb)
print("MultinomialNB F1 Score:", f1_mnb)
print("MultinomialNB Classification Report:\n", report_mnb)

print("ComplementNB Accuracy:", accuracy_cnb)
print("ComplementNB F1 Score:", f1_cnb)
print("ComplementNB Classification Report:\n", report_cnb)

print("BernoulliNB Accuracy:", accuracy_bnb)
print("BernoulliNB F1 Score:", f1_bnb)
print("BernoulliNB Classification Report:\n", report_bnb)

# Plot learning curve for GaussianNB
train_sizes, train_scores, test_scores = learning_curve(gnb, X, y, cv=5, scoring='f1_weighted', n_jobs=-1, 
                                                         train_sizes=np.linspace(0.1, 1.0, 10), random_state=100)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure(figsize=(8, 6))
plt.title("Learning Curve - GaussianNB")
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.grid()

plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1,
                 color="r")
plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1,
                    color="g")
plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")
plt.legend(loc="best")
plt.show()
