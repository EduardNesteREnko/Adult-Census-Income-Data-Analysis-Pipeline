import pandas as pd
import numpy as np

df = pd.read_csv('adult.data.csv')

df = df.replace(r'^\s*\?\s*$', None, regex=True)

df_clean = df.dropna(subset=['workclass', 'occupation', 'native-country'])

gender_counts = df['sex'].value_counts()

print(gender_counts)

average_age_women = df[df['sex'] == 'Female']['age'].mean()

years = int(average_age_women)
months = round((average_age_women - years)* 12)

print(f"{years} років {months} місяців")


germany_people = df['native-country'].value_counts(normalize=True)['Germany'] * 100

print(f"{germany_people:.2f}%")

age_stats = df.groupby('salary')['age'].agg(['mean', 'std'])

print(age_stats)

df['salary'] = df['salary'].str.strip()
df['education'] = df['education'].str.strip()

higher_education = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']

all_have_higher_education = df[df['salary'] == '>50K']['education'].isin(higher_education).all()

print(all_have_higher_education)
df['race'] = df['race'].str.strip()
df['sex'] = df['sex'].str.strip()

age_stats = df.groupby(['race', 'sex'])['age'].describe()
print(age_stats)

max_age_amer_indian = age_stats.loc['Amer-Indian-Eskimo', 'max']
print(f"\nМаксимальний вік раси Amer-Indian-Eskimo: {max_age_amer_indian}")


rich_share = (
    df[df['sex'].str.strip() == 'Male']
    .assign(is_married=lambda x: x['marital-status'].str.strip().str.startswith('Married'))
    .groupby('is_married')['salary']
    .apply(lambda x: (x.str.strip() == '>50K').mean() * 100)
    .rename({True: 'Одружені', False: 'Не одружених'})
)


if rich_share['Одружені'] > rich_share['Не одружених']:
    print("\nВідповідь: Доля багатших (>50K) більша серед одружених чоловіків.")
else:
    print("\nВідповідь: Доля багатших (>50K) більша серед неодружених чоловіків.")


max_hours = df['hours-per-week'].max()

num_people = (df['hours-per-week'] == max_hours).sum()

subset = df[df['hours-per-week'] == max_hours]
rich_percentage = (subset['salary'] == '>50K').mean() * 100

print(f"Максимальна кількість годин: {max_hours}")
print(f"Кількість людей: {num_people}")
print(f"Відсоток багатих серед них: {rich_percentage:.2f}%")


avg_hours_by_country = (
    df.groupby(['native-country', 'salary'])['hours-per-week']
    .mean()
    .unstack()
)

print(avg_hours_by_country)
