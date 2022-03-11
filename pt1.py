
class bmi_calculation:

    def calculate_bmi(user, feet, inches, weight):
        user_feet = feet
        user_inches = inches
        user_weight = weight

       
        if user_feet == 0 and user_inches == 0: 
            x = "Height can't be zero."
            return x
        elif user_feet < 0 or user_inches < 0: 
            x = "Height can't be negative."
            return x
        elif user_feet >= 10:
            return("Height can't be greater than or equal to 10 feet.")
        elif user_inches not in range(0,11):
            return ("Inches value should be in between 0 to 11.")
        elif user_weight <= 0:
            return ("Weight can't be negative or zero.")
    
        else:
            length = float(((user_feet*12)+user_inches)*0.025)
            weight = float(user_weight*0.45)
            bmi = float(weight/(length*length))
            if bmi <= 0:
                return ("BMI can't be negative or zero. Something is wrong.")
            elif bmi < 18.5:
                return ("Your bmi is {} and you are considered as under weight.".format(bmi))
            elif bmi >= 18.5 and bmi <=24.9:
                return ("Your bmi is {} and you are considered as normal weight.".format(bmi))
            elif bmi >= 25 and bmi <=29.9:
                return ("Your bmi is {} and you are considered as over weight.".format(bmi))
            elif bmi >= 30:
                return ("Your bmi is {} and you are considered as obese.".format(bmi))

            
