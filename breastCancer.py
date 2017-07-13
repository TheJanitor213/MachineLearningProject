import csv
training=''
trainingList=[]
with open("breastCancerData.csv", 'r') as f:
    reader = csv.DictReader(f)

    for i, line in enumerate(reader):
        s = line['diagnosis']
        if(s=="B"):
            training = "1 1:"+line['radius_mean'] + " 2:"+line['texture_mean'] + " 3:"+ line['perimeter_mean'] + " 4:"+ line['area_mean'] + " 5:"+line['smoothness_mean'] + " 6:"+ line['compactness_mean'] + " 7:"+ line['concavity_mean'] + " 8:"+line['concave points_mean'] + " 9:"+ line['symmetry_mean'] +" 10:"+ line['fractal_dimension_mean'] + " 11:" + line['radius_se'] + " 12:"+line['texture_se'] + " 13:" +line['perimeter_se'] + " 14:"+line['area_se'] + " 15:"+line['smoothness_se'] + " 16:"+line['compactness_se'] + " 17:"+line['concavity_se'] + " 18:" +line['concave points_se'] +" 19:"+ line['symmetry_se'] + " 20:"+line['fractal_dimension_se'] + " 21:"+line['radius_worst'] + " 22:"+line['texture_worst'] +  " 23:"+line['perimeter_worst'] + " 24:" +line['area_worst'] + " 25:" +line['smoothness_worst'] + " 26:"+ line['compactness_worst'] + " 27:"+ line['concavity_worst'] + " 28:" + line['concave points_worst'] + " 29:" +line['symmetry_worst'] + " 30:"+line['fractal_dimension_worst']
            trainingList.append(training)
        else:
            training = "-1 1:"+line['radius_mean'] + " 2:"+line['texture_mean'] + " 3:"+ line['perimeter_mean'] + " 4:"+ line['area_mean'] + " 5:"+line['smoothness_mean'] + " 6:"+ line['compactness_mean'] + " 7:"+ line['concavity_mean'] + " 8:"+line['concave points_mean'] + " 9:"+ line['symmetry_mean'] +" 10:"+ line['fractal_dimension_mean'] + " 11:" + line['radius_se'] + " 12:"+line['texture_se'] + " 13:" +line['perimeter_se'] + " 14:"+line['area_se'] + " 15:"+line['smoothness_se'] + " 16:"+line['compactness_se'] + " 17:"+line['concavity_se'] + " 18:" +line['concave points_se'] +" 19:"+ line['symmetry_se'] + " 20:"+line['fractal_dimension_se'] + " 21:"+line['radius_worst'] + " 22:"+line['texture_worst'] +  " 23:"+line['perimeter_worst'] + " 24:" +line['area_worst'] + " 25:" +line['smoothness_worst'] + " 26:"+ line['compactness_worst'] + " 27:"+ line['concavity_worst'] + " 28:" + line['concave points_worst'] + " 29:" +line['symmetry_worst'] + " 30:"+line['fractal_dimension_worst']
            trainingList.append(training)
for i in trainingList:
    print(i)

thefile = open('trainingdata.txt', 'w')
for item in trainingList:
  thefile.write("%s\n" % item)
