import math
import csv
import statistics

def load_csv(file): 
    with open(file, "r") as csvfile:
        csvread = csv.reader(csvfile)
        data = list(csvread)
        
        return data

def seperate_class(data): # data seperated in 2 lists of yes or no
    seperated = {}
    for row in data:
        classification = row[-1]
        if classification not in seperated:
            seperated[classification] = []

        seperated[classification].append(row)

    return seperated

def class_P(seperated, classi):
    total = len(seperated["yes"]) + len(seperated["no"])

    count = len(seperated[classi])
    # print("{}/{}".format(count, total))
    return count / float(total)

def mean(values):
    return statistics.mean(values)
    # return sum(values) / float(len(values))

def stdev(values):
  
    return statistics.stdev(values)

def column_index(index, classi, seperated):
    values = []
    counter = 0
    for row in seperated[classi]:
     
        values.append(float(row[index]))

    return values

def PDF(value, mean, stdev):
    exponent = math.exp(-(math.pow(value - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

    # bottom = (math.e / (stdev * math.sqrt(2 * math.pi)))
    # power = ((value - mean) ** 2) / (2 * (stdev ** 2))

    # return bottom ** -power

def calculate_CP(seperated, classi, test_row): #calculates probability for all columns in tranining data
    
    prob = 1
    for i in range(0,len(test_row)):
     
        values = column_index(i,classi,seperated)
        mean_ = mean(values)
        stdev_ = stdev(values)
        
        pdf = PDF(float(test_row[i]), mean_,stdev_)
        prob = prob * pdf

    return prob

def predict_class(training_data, test_row):
    seperated = seperate_class(training_data)
    p_no = calculate_CP(seperated, "no", test_row) * class_P(seperated, "no")
    p_yes = calculate_CP(seperated, "yes", test_row) * class_P(seperated, "yes")
  
    if p_yes > p_no:
        return "yes"
    elif p_no > p_yes:
        return "no"
    else:
        return "yes"

def classify_nb(training_filename, testing_filename):
    training_data = load_csv(training_filename)
    testing_data = load_csv(testing_filename)   
    predictions = []
    for row in testing_data:
        predictions.append(predict_class(training_data, row))
    

    return predictions

print(classify_nb("pima.csv", "testing_data.csv"))