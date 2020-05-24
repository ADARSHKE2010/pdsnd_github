import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        city = input("\n Enter the city you want to filter by\n").lower()
        if(city=='chicago' or city == 'new york' or city == 'washington'):
            break

        else:
            city = input('Enter Correct city: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while (True):
        month = input("\nWhich month would you like to filter by between january to june or type 'all' for no preference?\n").lower()
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month=input("Enter a correct month: ").lower()  #converting to lowercase

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Enter the day you are looking for or type 'all' for no preference.\n")
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
            
        else:
            day=input("enter a correct day: ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])    #Obtaining datetime from start time column

    df['month'] = df['Start Time'].dt.month      #Creating new columns of month and day of week    
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':      # filtering by month
        months = ['january', 'february', 'march', 'april', 'may', 'june']  
        month = months.index(month) + 1       #use to get the index of the months.

        df = df[df['month'] == month]    #Creating new data frame, filter by month.

    if day != 'all':       #filtering by day
        df = df[df['day_of_week'] == day.title()]    #Creating new data frame, filter by day.
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Common_Month = df['month'].mode()[0]
    print('Most Common Month:', Common_Month)

    # TO DO: display the most common day of week
    Common_Day = df['day_of_week'].mode()[0]
    print('Most Common day:', Common_Day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Common_Hour = df['hour'].mode()[0]
    print('Most Common Hour:', Common_Hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('\nMost commonly used start station is {}\n'.format(Start_Station))

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station is {}\n'.format(End_Station))

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip is {} and {}'.format(Start_Station, End_Station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('User Types:\n', User_Types)

    # TO DO: Display counts of gender
    if('Gender' in df):
        Male_Count = df['Gender'].str.count('Male').sum()
        Female_Count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(Male_Count)))
        print('\nNumber of female users are {}\n'.format(int(Female_Count)))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        Earliest = df['Birth Year'].min()
        Recent = df['Birth Year'].max()
        Most_Common =  df['Birth Year'].value_counts().idxmax()
        print('\n Earliest Year is {}\n Recent Year is {}\n Most Common Year is {}\n'.format(int(Earliest), int(Recent), int(Most_Common)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def disp_data(df):
    head=0
    tail=5
    user_choise = input('\n Do you want to see the data of the trip? reply with "yes" or "no"\n')
<<<<<<< HEAD
<<<<<<< HEAD
  
=======
>>>>>>> ddcbe347fa07671ee724ce660ec5274ad1134a44
=======
  
>>>>>>> documentation
    if user_choise.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        want_again = ''
        while want_again.lower() != 'no':
                want_again = input('\n Do you want to see some more data of the trip? reply with "yes" or "no"\n')
                if want_again.lower() == 'yes':
                    head += 5
                    tail += 5
                    print(df[df.columns[0:-1]].iloc[head:tail])
                elif want_again.lower() == 'no':
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            



if __name__ == "__main__":
	main()
