import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS ={'january':1,
         'jebruary':2,
         'march':3,
         'april':4,
         'may':5,
         'june':6,
         'july':7,
         'august':8,
         'september':9,
         'october':10,
         'november':11,
         'december':12,
         'all': 14}

DAYS ={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6,'all':10}
print('Hello! Let\'s explore some US bikeshare data!')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=""
    month=""
    day=""
    print("Enter the City name -\n 1.chicago \n 2.new york city \n 3.washington")
    while(True):
        a=input().lower()
        if a not in CITY_DATA:
            print("Invalid input:-Please enter one of the following cities \n 1.chicago \n 2.new york city \n 3.washington")
        else:
            city=a
            break
    print("Enter name of the month all, january, february, march, april,may, june, july, august, september, october, november, december")        
    while(True):
        b=input().lower()
        if b in MONTHS:
            month=b
            break 
        else:
            print("Invalid input:-Please enter one of  :all, january, february, march, april, may, june, july, august, september, october, november, december")
            
    print("Enter name of the day of week -all, monday, tuesday, wednesday, thursday, friday, saturday, sunday :")        
    while(True):
        c=input().lower()
        if c in DAYS:
            day=c
            break 
        else:
            print("Invalid input:-Please enter one of- all, monday, tuesday, wednesday, thursday, friday, saturday, sunday ")
            
                  

    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    data = pd.read_csv(CITY_DATA[city])
    df=pd.DataFrame()
    if month=="all" and day =="all":
        df=data
    elif month=="all" and day !="all": 
        df= data.loc[(pd.DatetimeIndex(data['Start Time']).day == DAYS[day])]
    elif  month!="all" and day =="all": 
        df= data.loc[(pd.DatetimeIndex(data['Start Time']).month ==MONTHS[month])] 
    else:
        df=data.loc[(pd.DatetimeIndex(data['Start Time']).month ==MONTHS[month])
                     & (pd.DatetimeIndex(data['Start Time']).day == DAYS[day])]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=pd.DatetimeIndex(df['Start Time']).month.value_counts().idxmax()
    
    for key in MONTHS:
        if MONTHS[key]==common_month:
            print("Most common month is "+str(key))

    # TO DO: display the most common day of week
    common_day=pd.DatetimeIndex(df['Start Time']).day.value_counts().idxmax()
    
    for key in DAYS:
        if DAYS[key]==common_day:
            print("Most common day of week is "+str(key))

    # TO DO: display the most common start hour
    common_hour=pd.DatetimeIndex(df['Start Time']).hour.value_counts().idxmax()
    print("Most common start hour is "+str(common_hour+1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station is "+str(start_station))
    
    # TO DO: display most commonly used end station
    end_station=df['End Station'].value_counts().idxmax()
    print("Most commonly used end station is "+str(end_station))
    
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End']=df['Start Station']+"-"+df['End Station']
    start_end=df['Start_End'].value_counts().idxmax()
    print("Most frequent combination of start station and end station trip is "+str(start_end))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time "+str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("Most commonly used end station "+str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts=df['User Type'].value_counts()
    print("counts of user types")
    print(user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts=df['Gender'].value_counts()
        print("counts of Gender")
        print(gender_counts)
    except:
        print("Gender data is not avaliable for selected city")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year=min(df['Birth Year'])
        recent_birth_year=max(df['Birth Year'])
        common_birth_year=df['Birth Year'].value_counts().idxmax()
        print("Earliest birth year is "+str(earliest_birth_year))
        print("Recent birth year is "+str(recent_birth_year))
        print("Most common birth year is "+str(common_birth_year))
        
    except: 
        print("Date of birth data is not avaliable for selected city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def raw_data(df):
    """Displays the raws data."""
    
    print("nWould you like to display the raw ? Enter yes or no.\n")
    previous=0
    current=5
    response=""
    while True:
        response=input().lower()
        if response not in ['yes','no']:
            print("Invalid input:- Please enter one of - yes or no")
            continue
            
        if response =="no":
            return
        
        while(response=="yes"):
            if(df.shape[0] >current):
                print(df[previous:current:])
                previous=previous+5
                current=current+5
                
            elif(df.shape[0]<current and df.shape[0]>previous):
                print(df[previous::])
                return
            
            else:
                print("There is no more data to dispay")
                return
                
            print("nWould you like to display additional raw data ? Enter yes or no.\n")    
            while True:
                response=input().lower()
                if response not in ['yes','no']:
                    print("Invalid input:- Please enter one of -yes or no")
                    continue
                    
                if response =="no":
                    return    
                if response =="yes":
                    break
            
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty==True:
            print("There is no data avaliable for selected city,month, day. Please select different value")
            continue
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
