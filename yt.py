

# #     rows=csv.reader(custfile,delimiter=',')
# # with open("C:\\Users\\saura\\Downloads\\training.1600000.processed.noemoticon.csv",'r') as custfile:
# # for r in rows:
# #      print(r)
# import csv

# with open("C:\\Users\\saura\\Downloads\\training.1600000.processed.noemoticon.csv", "r") as students:
#     read_file = csv.reader(students)
# for r in read_file:
#     print(r)
import csv
students = open("C:\\Users\\saura\\Downloads\\training.1600000.processed.noemoticon.csv", "r")
read_file = csv.reader(students)
for r in students:
    print(r)