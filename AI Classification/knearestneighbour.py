import math
import csv

def load_csv(file): 
    with open(file, "r") as csvfile:
        csvread = csv.reader(csvfile)
        data = list(csvread)
        
        return data
    
def euclidean(Arow, Brow):
    distance = 0.0

    for i in range(len(Arow) - 1):
        distance += (float(Arow[i]) - float(Brow[i]))**2

    return math.sqrt(distance)

def neighbours_k(training, test, k):
    distance = []
    for row in training:
        dist = euclidean(row, test)
        distance.append((row, dist))

    distance.sort(key=lambda x: x[1]) # sort by distance
    neighbours = []
    for dist in distance[:k]:
        neighbours.append(dist[0])

    classes = []

    for neighbour in neighbours:
        classes.append(neighbour[-1])
        # print(neighbour[-1])
    
    yes_count = classes.count("yes")
    no_count = classes.count("no")
    if yes_count > no_count:
        return "yes"
    elif no_count > yes_count:
        return "no"
    else: 
        return "yes"
    # return max(set(classes), key=classes.count)

    
def classify_nn(training_filename, testing_filename, k):
    training_data = load_csv(training_filename)
    testing_data = load_csv(testing_filename)   
    predictions = []

    for row in testing_data:
        predictions.append(neighbours_k(training_data, row, k))
        # print("nio")
       
    return predictions

print(classify_nn('pima.csv', 'testing_data.csv', 3))