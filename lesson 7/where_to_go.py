def where_to_go(age = None):
    def kindergarden():
        return print('should go to kindergarden')
    def school():
        return print('should go to school')
    def university():
        return print('it is never too late to go to university')

    if age <= 6:
        kindergarden()    
    elif age > 6 and age <= 17:
        school()        
    elif age > 17:
        university()
            

where_to_go(3)
where_to_go(9)
where_to_go(70)
