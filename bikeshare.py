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
    #For error checking we'll utilize if/else statements to error check users so that they don't make any inputs that could mess up the script
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ["chicago","washington","new york city"]
    months = ['all','january','febuary','march','april','may','june']
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    #First while loop will have users keep inputting inputs for city until a valid choice is made
    while True: 
        city = input('Input a City').lower()
        if city not in cities:
            print(f"{city} is not a valid city")
            continue
        else:
            break
    
    #Second while loop will have users keep inputting inputs for month until a valid choice is made
    while True: 
      month = input('Input a month').lower()
      if month not in months:
            print(f"{month} is not a valid month")
            continue
      else:
            break

    #Third while loop will have users keep inputting inputs for day until a valid choice is made
    while True: 
        day = input('Input a day').lower()
        if day not in days:
            print(f"{day} is not a valid day")
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA.get(city))
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'all':
        df = df[df['Start Time'].dt.month_name().str.lower() == month]
    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['Start Time'].dt.month_name().mode()[0]

    ### most common day
    common_day = df['Start Time'].dt.day_name().mode()[0]


    ### most common hour 
    common_hour = df['Start Time'].dt.hour.mode()[0]
    
    print(f"Common Month: {common_month}\n")
    print(f"Common Day: {common_day}\n")
    print(f"Common Hour: {common_hour}\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start = df['Start Station'].mode()[0]
    common_end = df['End Station'].mode()[0]
    df['Full Trip'] = df['Start Station'] + ' - ' + df['End Station']
    common_full = df['Full Trip'].mode()[0]
    
    print(f"Common Start Station: {common_start}\n")
    print(f"Common End Station: {common_end}\n")
    print(f"Common Start & End Station: {common_full}\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    average_travel = df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if 'Gender' in df.columns:
        user_types = df['User Type'].value_counts()
        genders = df['Gender'].value_counts()
        min_year = df['Birth Year'].min()
        max_year = df['Birth Year'].max()
        mode_year = df['Birth Year'].mode()[0]

        print(f"User Types: {user_types}\n")
        print(f"Genders: {genders}\n")
        print(f"Min Year: {min_year}\n")
        print(f"Recent Year: {max_year}\n")
        print(f"Most Common Year: {mode_year}\n")
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """displays 5 rows of data to user"""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    if view_data == 'yes':
      start_loc = 0
      while (start_loc + 5 < len(df)):
          print(df.iloc[start_loc:start_loc+5])
          start_loc += 5
          view_display = input("Do you wish to continue?: Enter yes or no").lower()
          if view_display == 'no':
            break


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
