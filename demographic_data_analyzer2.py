import pandas as pd

def calculate_demographic_data(df):
    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with Bachelor's degree
    total_count = df.shape[0]
    num_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((num_bachelors / total_count) * 100, 1)

    # 4 & 5. Percentage with and without advanced education earning >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]

    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1
    )
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1
    )

    # 6. Minimum number of hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people who work minimum hours and earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round(
        (min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1
    )

    # 8. Country with highest percentage of >50K earners
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (country_rich_counts / country_counts * 100).fillna(0)
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Most popular occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Return all results as a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
