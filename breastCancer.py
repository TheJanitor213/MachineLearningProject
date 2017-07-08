import csv
training=''
trainingList=[]
with open("breastCancerData.csv", 'r') as f:
    reader = csv.DictReader(f)

    for i, line in enumerate(reader):
        s = line['diagnosis']
        if(s=="B"):
            training = "1 1:"+line['radius_mean'] + " 2:"+line['texture_mean'] + " 3:"+ line['perimeter_mean'] + " 4:"+ line['area_mean'] + " 5:"+line['smoothness_mean'] + " 6:"+ line['compactness_mean'] + " 7:"+ line['concavity_mean'] + " 8:"+line['concave points_mean'] + " 9:"+ line['symmetry_mean'] +" 10:"+ line['fractal_dimension_mean']
            trainingList.append(training)
        else:
            training = "-1 1:"+line['radius_mean'] + " 2:"+line['texture_mean'] + " 3:"+ line['perimeter_mean'] + " 4:"+ line['area_mean'] + " 5:"+line['smoothness_mean'] + " 6:"+ line['compactness_mean'] + " 7:"+ line['concavity_mean'] + " 8:"+line['concave points_mean'] + " 9:"+ line['symmetry_mean'] +" 10:"+ line['fractal_dimension_mean']
            trainingList.append(training)
for i in trainingList:
    print(i)

thefile = open('trainingdata.txt', 'w')
for item in trainingList:
  thefile.write("%s\n" % item)
