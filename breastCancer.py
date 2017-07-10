import csv
training=''
trainingList=[]
with open("breastCancerData.csv", 'r') as f:
    reader = csv.DictReader(f)

    for i, line in enumerate(reader):
        s = line['diagnosis']
        if(s=="B"):
            training = "1 1:"+line['texture_mean'] + " 2:"+ line['area_mean'] + " 3:"+line['smoothness_mean'] + " 4:"+line['concave points_mean']
            trainingList.append(training)
        else:
            training = "-1 1:"+line['texture_mean'] + " 2:"+ line['area_mean'] + " 3:"+line['smoothness_mean'] + " 4:"+line['concave points_mean']
            trainingList.append(training)
for i in trainingList:
    print(i)

thefile = open('trainingdata.txt', 'w')
for item in trainingList:
  thefile.write("%s\n" % item)
