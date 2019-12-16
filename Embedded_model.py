'''
A script to perform MNB classifier
design by.https://github.com/SausanCantik

Use the following code to:
0. Locate the files containing the dataset and selected features in excel format
1. Encode the dataset
2. Run the classifier with combination of selected features
3. Save output in excel file
'''

#libraries
#--------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from itertools import combinations
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from itertools import combinations
from sklearn.model_selection import cross_val_score

#Load the data and identify the number of rows from each data
#--------------------------------------------------------------
def loaddata():
    excel_path = input('Enter the file path : ')
    # read the .xlsx file
    dataframe = pd.read_excel(excel_path, sheet_name=0)
    return dataframe

#Encoding the data
#--------------------------------------------------------------
def genotype_encoder(dataset) :
    dataset.drop(columns='Samples', axis = 1, inplace=True)
    encoded_dataset = dataset.apply(LabelEncoder().fit_transform)
    return encoded_dataset

#Defining selected markers
#--------------------------------------------------------------
def selecting_markers (feature_selection_path):
    k = int(input('How many markers to use?    '))
    dataframe = pd.read_excel(feature_selection_path)
    feature = dataframe['feature'].loc[:m]
    column = feature.tolist()
                
    return column, k

#Embedded model
#--------------------------------------------------------------
def embedded_model(column, k):
    X = encoded_dataset[column]
    y = encoded_dataset['Label']
    
    #Splitting the dataset into X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=13)
    
    #MNB Model
    selected_markers = []
    mnb_accuracy = []
    for i in range (k) :
        i = i+1
    
        #Check point i
        #print ('Iteration with number of markers :  {}' .format(i), '\n')
    
        #create a combination of marker
        markers = list(combinations(column,i))
    
        #create a dictionary for marker and the model accuracy
        model_list = {}
    
        #for each combination, generate the Classifier, obtain the model accuracy
        for marker in markers:
            selected = list(marker)
            #marker_model['Marker'] = marker
            trainX = X_train[selected]
            testX = X_test[selected]
                        
            #build the svm model using training data
            model = MultinomialNB()       
            model.fit(trainX, y_train)

            #testing the model
            predictions = model.predict(testX)

            #model evaluation
            scores = cross_val_score(model, trainX, y_train, cv=5)
            #marker_model['SVC Accuracy'] = scores.mean()
            #marker_model['SVC std'] = scores.std()*2
            marker_accuracy = scores.mean()
                
            #store the marker evaluation score
            model_list[marker] = marker_accuracy
        
            #check point
            #print (model_list)
        
            #select the most accurate model
            optimum = max(list(model_list.values()))
        
            #for each combination class get the optimum combination based on max accuracy
            mark = list(model_list.keys())[list(model_list.values()).index(optimum)]
        selected_markers.append(mark)
        optimum = round(optimum, 2)
        mnb_accuracy.append(optimum)
    
    #final output
    df1 = pd.DataFrame(list(zip(selected_markers, mnb_accuracy)), columns = ['Markers', 'Accuracy'])
        
    #write the sheet as excel sheet
    df1.to_excel('Extremophile_classifier.xlsx')

#Running program
#--------------------------------------------------------------
print('LOADING THE EXCEL FILES')
print('=======================================')
print('Enter the path to the dataset')
dataset = loaddata()
print ('Dataset loaded. Dimension : ' , dataset.shape)

print('Enter the PATH of Feature_selection.xlsx')
feature_selection_path = input()
print ('Feature_selection.xlsx loaded')
print('\n')

print('currently running : DATA ENCODING')
print('=======================================')
encoded_dataset = genotype_encoder(dataset)
print('\n')

print('SELECTING MARKERS')
print('=======================================')
column, m = selecting_markers (feature_selection_path)

print('currently runing : EMBEDDED MODEL')
print('=======================================')
embedded_model(column, m)
print('you now have a file called: Extremophile_classifier.xlsx ')
