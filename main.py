import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'Impact',
        'color':  'blue',
        'weight': 'bold',
        'size': 30,
        }

df = pd.read_csv('crime_rate_Spain.csv')  # read file csv that contain data
#print(df)
sorted_crime_df = df.sort_values(["Location", "Year", "Crime"])
crime = list(set(df['Crime'])) #list of crime
year = list(set(df['Year']))#list of year
location = list(set(df['Location'])) #list of location
print(len(crime)) #num. of the crime
print(len(year)) #num. of the year
print(len(location)) #num of the loacaton
print('---------------------------------------')
print(' List of the Crime' , crime )

#_________________________Task 1_________________________________________
def plot_trend_task1():
    speici_crime = 'Drug trafficking'  # filter with specific crime  ex: Theft
    specific_crime = df.loc[df['Crime'].str.contains(speici_crime)]
    # بدي ابحث في العمود اللي اسمه crime  على الجريمة اللي انا حددتها اللي هي theft

    Year = specific_crime['Year'].unique()
    # حتى ما يتكرر اكثر من مرة عدد السنوات فانا بوخذ التكرار مرة وحدة فقط
    sumyear = specific_crime.groupby('Year').sum()
    # بدي اجمع كل جريمة في السنة نفسها
    # قديش عدد كل جريمة في السنة نفسها لمل المدن
    sums = sumyear['Total cases'].to_numpy()  # حتى اخليها مصفوفة بالنسبة لعدد السنوات
    pos1 = np.arange(len(Year))

    n = len(Year)  # عدد السنوات اللي عندي بدون تكرار
    print(n)
    for i in range(n):  # بدي اعمل لوب على المصفوفة علشان نحط القيم جميع الحرائم بالنسبة للسنه على المصفوفة
        for j in range(0, n - i - 1):
            if Year[j] > Year[j + 1]:
                Year[j], Year[j + 1] = Year[j + 1], Year[j]
                sums[j], sums[j + 1] = sums[j + 1], sums[j]
                print(Year[j], Year[j + 1])

    #properties of the plot
    plt.plot(sums)
    plt.xticks(pos1, Year)
    plt.title("Trend of a ' " + speici_crime + " ' over time.", fontdict=font)
    plt.xlabel('Years', fontdict=font)
    plt.ylabel("Total Cost Of " + speici_crime, fontdict=font)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()
    print('Task 1 done :)')

#___________________________Task 2_________________________________
def pie_chart_task2():
    lables = df['Crime'].unique()
    # get the num of crime on each categories عدد الجرائم من كل نوع في جميع المدن

    # get the sum number of crime in each categoriy
    crime_per_year = df.groupby(['Crime'])['Total cases'].sum()
    # عدد الجرائم على مستوى الدولة
    #  كل جريمة بوخذ قديش صارت في هاي السنة ع مستوى الدولة كلها بالنسبة ل اسبانيا كلها

    #properties of the plot
    colors = ['darkturquoise', 'lightskyblue', 'teal', 'turquoise', 'deepskyblue', 'steelblue', 'lightsteelblue',
              'cornflowerblue', 'paleturquoise']
    plt.figure(figsize=(10, 5))
    ax = plt.axes()
    ax.set_facecolor("lightblue")
    plt.title('Percentage of  distribution of different crimes in the country \n', fontdict=font)
    ab = plt.pie(crime_per_year, labels=lables, colors=colors, startangle=90, autopct='%1.1f%%',
                 textprops={'fontsize': 14, 'color': 'darkblue'})
    plt.show()
    print('Task 2 done :)')
#_____________________Task 3______________________________
#يظهر توزيع الجرائم على المدن كلها
#يعني اول اشي بعمل مصفوفة بين الموقع وعدد الجرائم بعدين برسمها بالنسبة لكل موقع
def bar_chart_task3():
    bar1 = df.groupby(['Location']).sum()['Total cases']
    plt.xlabel('Locations', fontdict= font)
    plt.ylabel('Total Cases', fontdict= font)
    plt.title('Crimes in  City', fontdict= font)
    plt.xticks(np.arange(len(location)), rotation=45)
    plt.bar(location, bar1)
    plt.show()
    print('Task 3 done :)')


#_______________________main______________________________
print('''
1. Task 1 (The trend of a phenomenon (e.g., specific crime) over time.
2. Task 2: A pie chart showing the distribution of different crimes in the country or in a specific city
3. Task 3: A bar chart showing a comparison of number of crimes in a few cities (at least five)
''')
choise = int(input('Enter your choice >>> ')) #inter your choise task
if choise == 1:
    plot_trend_task1()

if choise == 2:
   pie_chart_task2()

if choise == 3:
   bar_chart_task3()
