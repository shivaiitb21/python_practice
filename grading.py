def gradingStudents(grades):
    
    for i in range(0,len(grades)):
        
        if grades[i] < 38:
            print(grades[i])
        else:
            temp = grades[i]
            te = temp % 5
            if te == 3:
                temp = temp + 2
                grades[i] = temp
            elif te == 4:
                temp = temp + 1
                grades[i] = temp
            
    return grades