import csv
import os
import pandas as pd


def GetData():

    Name = input("Enter Student Name :- ")
    RollNo = int(input("Enter Student Roll Number :- "))

    try:
        Marks = list(map(int, input("Enter Student marks in there subject (Space Separated):- ").split()))
        if len(Marks) != 3:
            print("Enter only 3 subject marks.")
            return
    except ValueError:
        print("Please Enter numeric marks.")
        return
    StudentData = {'Name' : Name, 'RollNo' : RollNo, 'Marks' : Marks}
    StudentsData.append(StudentData)
    CalculateAverage()
    


def DisplayData():
    if not os.path.exists(filename):
        print("Data File not found. please save some data first")
        return
    try:
        df = pd.read_csv(filename)
        
        if df.empty:
            print("File is empty")
        else:
            print("\n--- Student Records ---")
            print(df)
    except Exception as e:
        print('failed to read file: ',e)
    
    
def CalculateAverage():
    if not StudentsData:
        print("No Student data to calculate.")
        return
    for i in range(len(StudentsData)):
        Marks = StudentsData[i]['Marks']
        AvgMarks = sum(Marks) / len(Marks)
        StudentsData[i].update({'AvgMarks': round(AvgMarks,2)})
        
def SaveToCSV():
    FileExists = os.path.exists(filename)
    is_empty = not FileExists or os.stat(filename).st_size == 0
    
    with open(filename, "a", newline='') as StudentsDataFile:
        writer = csv.writer(StudentsDataFile)
        if is_empty:
            writer.writerow(['Name', 'RollNumber', 'Mark1', 'Mark2', 'Mark3', 'AvgMarks'])
        for student in StudentsData:
            row = [
                student['Name'],
                student['RollNo'],
                student['Marks'][0],
                student['Marks'][1],
                student['Marks'][2],
                student['AvgMarks']
            ]
            writer.writerow(row)
    print("Data stored to StudentsData.csv")
    StudentsData.clear()

def main():
    while True:
        print("\n***** Student Data Tracker *****")
        print('1. Add Student data')
        print('2. Display all Students')
        print('3. Save To CSV')
        print('0. Exit')
        choice = input("Enter your Choice:- ")

        if choice == '1':
            GetData()
        elif choice == '2':
            DisplayData()
        elif choice == '3':
            SaveToCSV()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Enter Valid Choice. Please try again.")

filename = 'StudentsDataFile.csv'
StudentsData = list()
main()