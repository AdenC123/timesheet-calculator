import argparse
import re
import datetime

# regex for finding times
time_regex = r'\d\d\d\d to \d\d\d\d'


def get_total_time() -> str:
    # get filename from argparse
    parser = argparse.ArgumentParser(description='Add all hours on a timecard. Hours must be in 24 hour format with '
                                                 'the word \'to\' between them. Ex: 0900 to 1700')
    parser.add_argument('filename', type=str, help='The path to a .txt file in the same directory as this script')
    filename = parser.parse_args().filename

    # get file data
    data = ''
    with open(filename, 'r') as file:
        data = file.read()

    # find all dates
    times = re.findall(time_regex, data)

    # add up times
    seconds = 0
    for time in times:
        t1 = datetime.datetime.strptime(time[0:4], '%H%M')
        t2 = datetime.datetime.strptime(time[8:12], '%H%M')
        td = t2 - t1
        seconds += td.total_seconds()

    # calculate total hours and minutes
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    # return formatted string
    return f'{int(hours):d} hours, {int(minutes):d} minutes'


if __name__ == '__main__':
    print(get_total_time())
