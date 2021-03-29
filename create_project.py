from subprocess import Popen, PIPE
import subprocess


user_input = input('Enter NEW Project Name: ')


# bash/shell/zsh commands
FIREBASE_TOOLS_INSTALL_CMD = 'npm install -g firebase-tools'.split()
FIREBASE_LOGIN_CMD = 'firebase login --reauth'.split()
FIREBASE_INIT_CMD = 'firebase init'.split()
FIREBASE_CREATE_PROJECT_CMD = 'firebase projects:create -n {user_input} {user_input}'.format(user_input=user_input).split()


def print_output_or_error(output, error):
    if output:
        print(output)
    if error:
        print(error)
        exit(error)


def open_command(cmd):
    process = Popen(cmd, cwd='.', shell=True, text=True)
    output, error = process.communicate()
    print_output_or_error(output, error)


def run_command(cmd):
    print(subprocess.run(cmd, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))


# run_command(FIREBASE_TOOLS_INSTALL_CMD)
open_command(FIREBASE_LOGIN_CMD)
run_command(FIREBASE_INIT_CMD)
open_command(FIREBASE_CREATE_PROJECT_CMD)


