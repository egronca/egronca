import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_value = list()
    race_index = list()
    
    for race in df["race"].unique():
        total = len(df[df["race"] == race])
        race_value.append(total)
        race_index.append(race)
        
    race_count = pd.Series(race_value, index = race_index)

    
    # What is the average age of men?
    
    men = df[df["sex"] == "Male"]
    average_age_men = round(men["age"].mean(), 1)

    
    # What is the percentage of people who have a Bachelor's degree?
    
    bach = df[df["education"] == "Bachelors"]
    len(bach)
    percentage_bachelors = round(len(bach)/len(df)*100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    hi_ed = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    low_ed = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(hi_ed)
    lower_education = len(low_ed)

    # percentage with salary >50K
    hi_ed_hi_in = hi_ed[hi_ed["salary"] == ">50K"]
    higher_education_rich = round(len(hi_ed_hi_in)/len(hi_ed)*100, 1)
    
    low_ed_hi_in = low_ed[low_ed["salary"] == ">50K"]
    lower_education_rich = round(len(low_ed_hi_in)/len(low_ed)*100, 1)

    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours_df = df[df["hours-per-week"] ==1]
    num_min_workers = len(min_work_hours_df)

    rich_percentage = len(min_work_hours_df[min_work_hours_df["salary"] == ">50K"])/len(min_work_hours_df)*100
    

    # What country has the highest percentage of people that earn >50K?
    
    highest_earning_country_percentage = 0 
    highest_earning_country = None
    
    for country in df["native-country"].unique():
        temp_df = df[df["native-country"] == country]
        temp_hi_in_df = temp_df[temp_df["salary"] == ">50K"]
        temp_pct = round(len(temp_hi_in_df)/len(temp_df)*100, 1)
        if temp_pct > highest_earning_country_percentage:
            highest_earning_country_percentage = temp_pct
            highest_earning_country = country

            
    # Identify the most popular occupation for those who earn >50K in India.
    
    india = df[df["native-country"] == "India"]
    india_hi_in = india[india["salary"] == ">50K"]
    
    count = 0 
    occupation = None 

    for job in india_hi_in["occupation"].unique():
        temp_df = india_hi_in[india_hi_in["occupation"] == job]
        number = len(temp_df)
        if number > count:
            count = number
            occupation = job 

    top_IN_occupation = occupation
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
