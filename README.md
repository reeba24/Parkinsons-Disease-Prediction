# Parkinson’s Disease Prediction using ML Algorithms via Web Application

Parkinson's disease (PD) significantly impacts 60% of people over 50, posing challenges due to its complexity, which complicates personalized treatment and monitoring. Early detection and intervention offer hope for those affected. As the global population ages, there is a growing need for innovative methods that enable early, accurate, and remote diagnosis of PD. This work explores the use of machine learning (ML) techniques in telemedicine to address this need. By leveraging ML models such as Support Vector Machine (SVM), Random Forest, K-Nearest Neighbors (KNN), and Logistic Regression, this project aims to improve the accuracy and effectiveness of Parkinson's disease diagnosis.

# DATASET ATTRIBUTES

MDVP:Fo(Hz)-Fundamental frequency (Hz), 
MDVP:Fhi(Hz)-Highest fundamental frequency (Hz), 
MDVP:Flo(Hz)-Lowest fundamental frequency (Hz), 
MDVP:Jitter(%)-Percentage of variation in the fundamental frequency, 
MDVP:Jitter(Abs)-Absolute value of jitter, 
MDVP:RAP-Relative average perturbation, 
MDVP:PPQ-Measure frequency variation, 
Jitter:DDP-Derivative of jitter measurement, 
MDVP:Shimmer-Amplitude variation of the voice signal, 
MDVP:Shimmer(dB)-Decibel level of shimmer, 
Shimmer:APQ3-Amplitude perturbation quotient (first three instants), 
Shimmer:APQ5-Amplitude perturbation quotient ( first five instances), 
MDVP:APQ-Average perturbation quotient, 
Shimmer:DDA-Discrete dynamic analysis of shimmer, 
NH-	Noise-to-harmonics ratio, 
HNR-Harmonics-to-noise ratio, 
status-This indicates the presence of Parkinson’s, 
RPDE-Recurrence period density entropy, 
DFA*Detrended fluctuation analysis, 
spread1-Dynamic complexity measure of the voice signal( Nonlinear), 
spread2-Dynamic complexity measure of the voice signal( Nonlinear), 
D2 -Correlation dimension of the voice signal, 
PPE-Pitch period entropy

# Evaluation of the performance of ML Algorithms

# Logistic Regression
Accuracy	89.74,
Precision	88.89,
Recall	100.0,
F1-Score	94.12

CONFUSION MATRIX

![image](https://github.com/user-attachments/assets/50c3bc08-f846-4633-a304-b07ea4f6a6c2)

# SVM	
Accuracy 89.74,
 Precision 88.89,
 Recall 100.0,
 F1-Score 94.12
 
CONFUSION MATRIX

 ![image](https://github.com/user-attachments/assets/62fb39a6-95e6-40af-9ca3-f67303b3dd44)

 
# Decision Tree	
Accuracy 97.44,
Precison 93.94,
Recall 96.88,
F1-Score 95.38

CONFUSION MATRIX

![image](https://github.com/user-attachments/assets/89b26982-5ac5-47dc-8db4-6934fd868580)

# Random Forest
Accuracy 94.87,
Precision 94.12,
Recall 100.0,
F1-Score 96.97

CONFUSION MATRIX

![image](https://github.com/user-attachments/assets/a5654e89-3d05-4b02-b32d-b031dfa05805)

# KNN
Accuracy 94.87,
Precision	94.12,
Recall 100.0,
F1-Score 96.97

CONFUSION MATRIX

![image](https://github.com/user-attachments/assets/359d5bef-8007-456f-ba60-4c8b8ac05a93)

# Web Application

![image](https://github.com/user-attachments/assets/ab529259-dbe5-46c9-ae3f-e5e625b07a4e)

# Result
This project presents a Parkinson’s disease prediction model and evaluates the performance of various machine learning algorithms. To predict the disease, data was first gathered and then processed using different machine learning techniques. The analysis revealed that the Decision Tree approach was the most successful, achieving an accuracy of 97.44%. Decision Trees are favored for their interpretability, ability to capture complex relationships, flexibility with diverse data types, feature importance analysis, and scalability to large datasets. Additionally, the project enhanced the KNN classifier by integrating it with the Decision Tree in a voting classifier, which improved accuracy from 94.87% to 97.44%.
