import subprocess

# ask the user for the desired project name
user_input = input('Enter NEW Project Name: ')

# bash/shell/zsh commands
FIREBASE_TOOLS_INSTALL_CMD = 'npm install -g firebase-tools'.split()
FIREBASE_LOGOUT_CMD = 'firebase logout'.split()
FIREBASE_LOGIN_CMD = 'firebase login --reauth'.split()
FIREBASE_CREATE_PROJECT_CMD = 'firebase projects:create -n {user_input} {user_input}'.format(user_input=user_input).split()
FIREBASE_INIT_CMD = 'firebase init'.split()


def print_output_or_error(output, error):
    if output:
        print('output: ', output)
    if error:
        print('error: ', error)
        exit(error)


def check_call(cmd):
    exit_code = subprocess.check_call(cmd)
    print('Exit Code: ', exit_code)


check_call(FIREBASE_TOOLS_INSTALL_CMD)
check_call(FIREBASE_LOGOUT_CMD)
check_call(FIREBASE_LOGIN_CMD)
check_call(FIREBASE_CREATE_PROJECT_CMD)
check_call(FIREBASE_INIT_CMD)

