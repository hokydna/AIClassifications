---------------------------

Classification Algorithms

---------------------------

To run these tasks please use commands:

    python3 naivebayes.py

    AND

    python3 knearestneighbour.py

The sample dataset for this program is the Pima Indian Diabetes dataset. It contains 768 instances 
described by 8 numeric attributes. There are two classes - yes and no. Each entry in the dataset 
corresponds to a patient’s record; the attributes are personal characteristics and test measurements;
the class shows if the person shows signs of diabetes or not. The patients are from Pima Indian heritage, 
hence the name of the dataset.

These programs require up to 3 inputs:
1. The original set of data for the algorithm to learn
2. The new set of data to classify
3. The specified distance between the data to classify and the original data based on euclidian distance
(for k nearest neighbour algorithm)

The programs will output:
A list of classifications for the 3 entries of new data yes or no.
