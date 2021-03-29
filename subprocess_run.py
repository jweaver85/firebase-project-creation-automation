import subprocess

# ask the user for the desired project name
user_input = input('Enter NEW Project Name: ')

# bash/shell/zsh commands
FIREBASE_TOOLS_INSTALL_CMD = 'npm install -g firebase-tools'.split()
FIREBASE_LOGOUT_CMD = 'firebase logout'.split()
FIREBASE_LOGIN_CMD = 'firebase login --reauth'.split()
FIREBASE_CREATE_PROJECT_CMD = 'firebase projects:create -n {user_input} {user_input}'.format(user_input=user_input).split()
FIREBASE_INIT_CMD = 'firebase init'.split()

print(subprocess.run(FIREBASE_TOOLS_INSTALL_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
print(subprocess.run(FIREBASE_LOGOUT_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
print(subprocess.run(FIREBASE_LOGIN_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
print(subprocess.run(FIREBASE_CREATE_PROJECT_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
print(subprocess.run(FIREBASE_INIT_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
