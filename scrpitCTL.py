import subprocess
import time
import re


def run_and_monitor(script_path):
    try:
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, text=True)
        with open(script_path, 'r') as file:
            lines = file.readlines()
        flag = False
        for lineNumber in range(len(lines)):
            line = lines[lineNumber]
            if line.startswith('start_time'):
                lineNumber += 1
                flag = True
                break
        if not flag:
            print('variable name not found, please do not change the variable name in download script.')
        pattenDate = "(['\"])(\d_?)+(['\"])"
        pattenFormat = "['\"](%[MmYyDdHh]_?)+['\"]"
        date = re.search(pattenDate, line).group()
        formatStr = re.search(pattenFormat, line).group()
        output = 'done!'


        while True:
            return_code = process.poll()
            output = process.stdout.readline().strip()
            if output != '':
                dateFormat = datetime_to_regex(formatStr)
                date = re.search(dateFormat, output).group()
                newC = f"start_time = datetime.strptime({date}, {formatStr})"
                modify_script_line(script_path, lineNumber, newC)
            print(output)
            if return_code is not None:
                process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, text=True)
            time.sleep(0.1)
    except subprocess.CalledProcessError as e:
        print("error:", e)


def modify_script_line(script_path, line_number, new_content):
    try:
        with open(script_path, 'r') as file:
            lines = file.readlines()
        if 0 < line_number <= len(lines):
            lines[line_number - 1] = new_content + '\n'
            with open(script_path, 'w') as file:
                file.writelines(lines)
        else:
            print("out of range")
    except IOError as e:
        print("operation error:", e)


def datetime_to_regex(format_str):
    regex_pattern = format_str.replace("%Y", "\d{4}")
    regex_pattern = regex_pattern.replace("%m", "\d{2}")
    regex_pattern = regex_pattern.replace("%d", "\d{2}")
    regex_pattern = regex_pattern.replace("%H", "\d{2}")
    regex_pattern = regex_pattern.replace("%M", "\d{2}")
    regex_pattern = regex_pattern.replace("%S", "\d{2}")
    if regex_pattern.startswith('"') and regex_pattern.endswith('"'):
        return regex_pattern[1:-1]
    elif regex_pattern.startswith("'") and regex_pattern.endswith("'"):
        return regex_pattern[1:-1]
    return regex_pattern


run_and_monitor(r"rda-download.py")         # address of rda-download.py


