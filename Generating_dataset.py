'''
A script generate dataset from selected column in sequence alignment
design by.https://github.com/SausanCantik

Work proceeding:
0. Perform MSA in Jalview 2.11.0
1. Copy the intended column to be used as features
2. Paste in an excel sheet
3. Repeat 1-2 for all intended columns

Use the following code to:
4. Parse the genotype
5. Build dataset in form of dataframe
'''

#library
import pandas as pd

#A Function to retain genotype from excel sheets
def parsing_genotype():
    #where is the file?
    excel_path = input('Enter the file path : ')
    features_number = int(input('How many features?  '))

    #parsing genotype
    features = {}
    sheets = {}
    for i in range (features_number) :
        genotypes = []
        sheets[i] = pd.read_excel(excel_path, sheet_name=i)
        line = sheets[i].values.tolist()
    
        #parse the genotype
        for j in range (len(line)) :
            if j % 2 == 0:
                genotype = line[j]
                genotype = str(genotype)
                genotype = genotype[2]
                genotypes.append(genotype)
            else :
                pass
        features[i] = genotypes
        
    return features

#A function to store features from list to dataframe
def create_dataset():
    features = parsing_genotype()
    dataset = pd.DataFrame.from_dict(features)
    
    return dataset

#----------------------------------------------------------
#Running the script
dataset = create_dataset()
