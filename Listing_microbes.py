'''
A script to list sample
design by.https://github.com/SausanCantik

Use the following code to:
0. List microbes based on its accession number and class

Requirements:
0. Path to folder where the listed sample is stored
1. sample.txt file containing list of the fasta within a folder
# to create sample.txt use : dir /s *fasta > sample.txt in CLI
'''

#Libraries
import pandas as pd

#parsing accession number, microbes name and the create the label
def listing_microbes ():
    extreme_class = 'Achidophile', 'Alkaliphile', 'Halophile', 'Thermophile'
    fasta_list = []
    labels = []
    accessions = []
    microbes = []
    for label in extreme_class :
        path = 'C:\\Users\\Sausan Cantik\\Documents\\Extremophile_study\\16S rRNA-20191206T062226Z-001\\16S rRNA\\{0}\\{0}.txt'.format(label)
        sample_list = open(path)
    
        for line in sample_list:
            fasta = line.split()[4]
            fasta_list.append(fasta)
            labels.append(label)
     
            #retain the first line
            path_sample = 'C:\\Users\\Sausan Cantik\\Documents\\Extremophile_study\\16S rRNA-20191206T062226Z-001\\16S rRNA\\{}\\{}' .format(label, fasta)
            fasta_sample = open(path_sample)
            first_line = []
            for line in fasta_sample :
                if line.startswith('>'):
                    first_line.append(line)
                else :
                    pass
                
            fasta_sample.close()
            
            #retain the accession and microbe name
            for item in first_line:
                accession = item.split(' ', 1)[0]
                accession = accession.split('>')[1]
                accessions.append(accession)
                ID = item.split(' ', 1)[1]
                first = ID.split(' ')[0]
                second = ID.split(' ')[1]
                microbe = first + ' ' + second
                microbes.append(microbe)
                
        sample_list.close()
        
    data = list(zip(accessions, microbes, labels))
    data = pd.DataFrame(data, columns = ['Accession', 'Microbe', 'Class'])

    return data
#---------------------------------------------------------------------------
#RUNNING
data = listing_microbes()
data.to_excel('List Microbes.xlsx')
