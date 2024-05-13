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
        patten = r"(['\"])(\d+)(['\"])"
        date = re.findall(patten, line)
        date = date[0][1]
        output = 'done'

        
        while True:
            return_code = process.poll()
            output = process.stdout.readline().strip()
            if output != '':
                print(1, output)
                date = output[16:30]
                newC = f"start_time = datetime.strptime('{date}', '%Y%m%d_%H_%M')"    # Due to the different file you want to download, the date here may need to be changed
                modify_script_line(script_path, lineNumber, newC)        # `17` here means the time needed to be rewritten is on line 17
            print(output)
            if return_code is not None:
                print(date)
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


run_and_monitor(r"EXAMPLE\rda-download.py")         # EXAMPLE adress of rda-download.py


