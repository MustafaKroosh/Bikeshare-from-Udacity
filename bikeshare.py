import time
import pandas as pd
import numpy as np
import datetime

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
    print('\nto begin our analysis you should choose one of the three cities \nchicago, new york city, washington')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():

        city = input('enter the name of the city: ').lower()
        if city in CITY_DATA.keys():
            print('\nyou have choosen {}'.format(city).title())
        else:
            print('you did not choose the right city to begin your analysis with \n please try one from \n chicago, new york city, washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    list_of_available = ['all', 'january', 'february', 'march', 'april', 'may', 'june' ]
    print('\nnow we want to select either you want to go to filter the month or doing your analysis on all the 6 months of the city you have chosen')
    print('please select one of', list_of_available)
    month = ''
    while month not in list_of_available:
        month = input('select all \nor \nthe month of the the data you want to filter ')
        if month in list_of_available:
            print('you have choosen {}'.format(month).title())
        else:
            'please enter month you want to filter again'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week = ['all', 'saturday', 'sunday', 'monday','tuesday', 'wednesday', 'thursday', 'friday']
    print('\nnow we want to know if you want to select specific day of the week or you want to do yor analysis on all week days \n')
    print('\nplease select all or \nthe day of the week you want to filter.')
    day = ''
    while day.lower() not in days_of_week:
        day = input('select all \nor \nthe day you want to filter:  ')
        if day in days_of_week:
            print('you have chosen {}'.format(day).title())
        else:
            print('you did not enter the day of the week please try again')
    print('\nyou have chose {} and the analysis month is {} and the weekday is {},\nthe analysis will be according to your choices'.format(city,month,day))

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print('would you like to take a look to a sample of the data')
    print('\nif you want to view the first five rows of the data\nplease enter yes\nif not and you like to go to the analysis directly please press any key then press enter')
    choice = ''
    choice = input('write yes to view the data or press any key then enter to go directly to the analysis: ')
    
    
    variable_1 = 0
    variable_2 = 5
    while choice == 'yes':
        print(df.iloc[variable_1:variable_2])
        variable_1 +=5
        variable_2 +=5
        choice = input('if you like to see another five rows of the filterd data you have chosen\nplease enter yes\nif not and it is enough for you and you want to proceed to the analysis\nplease press any key then press enter: ')
        
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    month_dict = {1:'Jan', 2:'Feb', 3:'March', 4:'APril', 5:'May', 6:'june'}
    print('popular month is: {}'.format(month_dict[popular_month]))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('popular day is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('popular hour to start  is: {}'.format(popular_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print('the most commonly used start station  is: {}'.format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print('the most commonly used end station  is: {}'.format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+' to '+df['End Station']
    most_used_combination = df['combination'].value_counts().idxmax()
    print('most frequent combination of start station and end station trip is: from {}'.format(most_used_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =df['Trip Duration'].sum()
    minutes, second = divmod(total_travel_time, 60)
    hour, minutes = divmod(minutes, 60)
    print('total travel time is: {} hours, {} minutes'.format(hour,minutes))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    minutes_m, seconds_m = divmod(mean_travel_time, 60)
    hour_m, minutes_m = divmod(minutes_m, 60)
    
    print('mean travel time is: {} hours, {} minutes and {} seconds'.format(hour_m, minutes_m, seconds_m))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('counts of user types is:\n{}'.format(counts_of_user_types))

    # TO DO: Display counts of gender
    try:
        
        gender_count = df['Gender'].value_counts()
        print('counts of gender is:\n{}'.format(gender_count))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_year = df['Birth Year'].value_counts().idxmax()
        print('\nearlist is: {} , \nrecent is: {}, \nand the common year of birth is: {}'.format(int(earliest), int(recent), int(common_year)))
    except:
        print('\ndata for Gender and Birthday year is not available for Washington')
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
