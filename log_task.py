import re
import logging

logging.basicConfig(level=logging.CRITICAL)


def find_and_log_errors(log_path):
    try:
        with open(log_path, 'r') as log_file:
            log_content = log_file.read()

        error_pattern = re.compile(r'.*(\d{2}:\d{2}:\d{2}.*(?:ERROR|LastError).*)', re.MULTILINE)
        critical_error_pattern = re.compile(r'.*CRITICAL ERROR.*$', re.MULTILINE)

        error_matches = error_pattern.findall(log_content)
        critical_error_matches = critical_error_pattern.findall(log_content)

        if error_matches:
            with open('found_errors.log', 'w') as error_log_file:
                for error_line in error_matches:
                    error_log_file.write(error_line + '\n')
            print(f'Lines with "ERROR" found and logged in found_errors.log.')
        else:
            print('No lines with "ERROR" found in the log.')
        if critical_error_matches:
            for critical_error_line in critical_error_matches:
                logging.critical(critical_error_line)

    except FileNotFoundError:
        print(f'Error: File "{log_path}" not found.')


log_file_path = r'C:\Users\DrillSergeant\Desktop\gupdate.log'

find_and_log_errors(log_file_path)
