import time
import datetime
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
   
    # Get user input for city (chicago, new york city, washington)
    
    city = str(input("\nWhich city would you like explore? We have data from Chicago, New York City and Washington: ")).lower()
    
    while city not in ("chicago", "new york city", "washington"):
        city = str(input("Please enter a valid city. Either Chicago, New York City, or Washington: ")).lower()

    # Get user input for month (all, january, february, ... , june)

    month = str(input("Which month would you like data from? Data is available from January through June. To explore all months choose 'All': ")).lower()
 
    while month not in ("january", "february", "march", "april", "may", "june", "all"):
        month = str(input("Please enter a valid month. Either January, February, March, April, May, June or All: ")).lower()
    
    # Get user input for day of week (all, monday, tuesday, ... sunday)

    day = str(input("Which day of the week would you like data from? To explore all days choose 'All': ")).lower()
 
    while day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday","all"):
        day = str(input("Please enter a valid day of the week. Either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All: ")).lower()
    

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])


    # extract month and day of week  and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =  df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    if month == 'all':
        month_counts = df['month'].value_counts()
        popular_month = month_counts.index[0]
        popular_month_count = month_counts[popular_month]
        popular_month_name = datetime.date(2020, popular_month, 1).strftime('%B')
        print("\nThe most popular month to travel is {} with a total of {} trips.".format(popular_month_name, popular_month_count))

    
    # display the most common day of week

    if day == 'all':
        day_counts = df['day_of_week'].value_counts()
        popular_day = day_counts.index[0]
        popular_day_count = day_counts[popular_day]
        print("\nThe most popular day to travel is {} with a total of {} trips.".format(popular_day, popular_day_count))

    
    #  display the most common start hour

    hour_counts = df['hour'].value_counts()
    popular_hour = hour_counts.index[0]
    popular_hour_count = hour_counts[popular_hour]
        
    print("\nThe most popular hour to start travel is {} with a total of {} trips.".format(popular_hour, popular_hour_count))    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations ...\n')
    start_time = time.time()

    #  display most commonly used start station

    start_station_counts = df['Start Station'].value_counts()
    common_start_station = start_station_counts.index[0]
    common_start_station_count = start_station_counts[common_start_station]
    
    print("\nThe most common station to start a trip is {} with a total of {} trips.".format(common_start_station, common_start_station_count))    


    #  display most commonly used end station

    end_station_counts = df['End Station'].value_counts()
    common_end_station = end_station_counts.index[0]
    common_end_station_count = end_station_counts[common_end_station]
    
    print("\nThe most common destination station is {} with a total of {} trips.".format(common_end_station, common_end_station_count))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    df['Travel Time'] = df['End Time'] - df['Start Time']
    
    total_travel_time = df['Travel Time'].sum()
    total_travel_days = total_travel_time.components[0]
    total_travel_hours = total_travel_time.components[1]
    total_travel_minutes = total_travel_time.components[2]
    
    print("\nThe total trip duration was {} days, {} hours and {} minutes.".format(total_travel_days,total_travel_hours,total_travel_minutes))

    # display mean travel time

    avg_travel_time = df['Travel Time'].mean()
    avg_travel_hours = avg_travel_time.components[1]
    avg_travel_minutes = avg_travel_time.components[2]
    
    print("\nThe average trip duration was {} hours and {} minutes.".format(avg_travel_hours,avg_travel_minutes))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_counts = df['User Type'].value_counts()
    
    print("\nHere are the counts of user type:\n{}".format(user_counts))

    # Display counts of gender
    
    if city != 'washington':
          gender_counts = df['Gender'].value_counts()
          print("\nHere is the trip breakdown by gender:\n{}".format(gender_counts))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    
    start_row = 0
    end_row = 4
    df = df.reindex()
    raw_data_response = str(input("\nWould you like to see 5 lines of raw data? ")).lower()
    
    while raw_data_response == 'yes':
        print(df.iloc[start_row:end_row + 1])
        start_row = start_row + 5
        end_row = end_row + 5
        raw_data_response = str(input("\nWould you like to see 5 more lines of raw data? ")).lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
