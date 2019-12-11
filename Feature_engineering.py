'''
A script to perform chi squeare based feature selection
design by.https://github.com/SausanCantik

Use the following code to:
0. Locate the file containing the dataset in excel format
1. Encode the dataset
2. Select relevant features
3. Save output in excel file
'''

#libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2

#Load the data and identify the number of rows from each data
#--------------------------------------------------------------
def loaddata():
    excel_path = input('Enter the file path : ')
    # read the .xlsx file
    dataframe = pd.read_excel(excel_path, sheet_name=0)
    return dataframe

#A function to store features from list to dataframe
def create_dataset():
    features = parsing_genotype()
    dataset = pd.DataFrame.from_dict(features)
    
    return dataset

#Encoding the data
#--------------------------------------------------------------
def genotype_encoder(dataset) :
    genotype_data.drop(columns='Samples', axis = 1, inplace=True)
    encoded_genotype = genotype_data.apply(LabelEncoder().fit_transform)
    return encoded_dataset

#Features selection using chi2 independent test
#---------------------------------------------------------------
def feature_selection(encoded_dataset):
    # Create features and target
    X = encoded_dataset.iloc[:, :23]
    y = encoded_dataset['Label']

    # Select two features with highest chi-squared statistics
    chi2_selector = SelectKBest(chi2, k=10)
    chi2_selector.fit(X, y)

    # Look at scores returned from the selector for each feature
    chi2_scores = pd.DataFrame(list(zip(list(X), chi2_selector.pvalues_)), columns=['feature', 'pval'])
    chi2_scores.sort_values('pval', ascending=True, inplace=True)
                
    #Features with the highest score
    kbest = np.asarray(list(encoded_dataset))[chi2_selector.get_support()]
            
    #write the sheet as excel sheet
    chi2_scores.to_excel('Feature_selection.xlsx')
#----------------------------------------------------------
    
#Running the script
dataset = loaddata()
encoded_dataset = genotype_encoder(dataset)
feature_selection(encoded_dataset)
