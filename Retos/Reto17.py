#!/usr/bin/python3

#Given the names and grades for each student in a Physics class of  students, 
# store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade. 

if __name__ == '__main__':
    students = []
    scores = []
    names = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    for i in students:
        scores.append(i[1])
    
    setScores = set(scores)
    listScores = list(setScores)
    scoresSorted = sorted(listScores)
    
    for i in students:
        if i[1] == scoresSorted[1]:
            names.append(i[0])
    
    namesSorted = sorted(names)
    for i in namesSorted:
        print(i)
            
        
    
        
    