def calculate_macros(gender, height, weight, age, activity_level):
    # Mifflin-St Jeor Equation
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    # Activity Level Multiplier
    if activity_level == 'sedentary':
        calories = bmr * 1.2
    elif activity_level == 'lightly active':
        calories = bmr * 1.375
    elif activity_level == 'moderately active':
        calories = bmr * 1.55
    elif activity_level == 'very active':
        calories = bmr * 1.725
    else:
        calories = bmr * 1.9  # extra active
    
    # Macronutrient Distribution (protein 25%, fats 30%, carbs 45%)
    protein_g = (calories * 0.25) / 4
    fat_g = (calories * 0.30) / 9
    carbs_g = (calories * 0.45) / 4
    
    return protein_g, fat_g, carbs_g, calories

def print_values(protein, fat, carbs, calories):
    print(f"Calories: {calories:.2f} kcal")
    print(f"Protein: {protein:.2f} g")
    print(f"Fats: {fat:.2f} g")
    print(f"Carbohydrates: {carbs:.2f} g")

def main():
    print("Welcome to the Macro Calculator")
    
    # User Inputs
    gender = input("Enter your gender (male/female): ")
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    age = int(input("Enter your age in years: "))
    activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ")
    
    protein, fat, carbs, calories = calculate_macros(gender, height, weight, age, activity_level)

if __name__ == "__main__":
    main()
