from datetime import datetime, date, timedelta
from os import path
import configparser

try:
    # Configuration setup
    parser = configparser.ConfigParser()
    parser.read('conf.ini')
    section_header = 'Conf'
    debug_mode = parser.get(section_header, 'debug_mode')
    appended_text = parser.get(section_header, 'appended_text')
except:
    print('Config setup failed to initialize.')
    # Configurations
    debug_mode = 'False'
    appended_text = ''


# Date information
current_day = datetime.strftime(datetime.now(),'%m/%d/%Y')
week_day = date.weekday(date.today())
monday = datetime.strptime(current_day, '%m/%d/%Y') - timedelta(days=week_day)


def generate_file_text():
    days = []
    for i in range(5):
        days.append(monday + timedelta(days=i))
    s = ''
    for day in days:
        s += f"{datetime.strftime(day, '%a (%m/%d)')}\nAdmin -  hours\n\n\n"
    s += appended_text
    return s


def execute():
    file_name = datetime.strftime(monday, '%m%d%Y.txt')
    abs_path = path.abspath(file_name).rsplit("\\", 1)
    if debug_mode != 'True':
        if path.exists(file_name):
            print(f'{file_name} already exists in {abs_path[0]}')
            return None
    with open(file_name, 'w') as time_sheet:
        time_sheet.write(generate_file_text())
    print(f'Time sheet file {file_name} created successfully.')


if __name__ == '__main__':
    execute()
