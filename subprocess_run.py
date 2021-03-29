import subprocess

user_input = input("Enter a name for you Firebase project: ")

FIREBASE_CREATE_PROJ_CMD = 'firebase projects:create -n {user_input} {user_input}'.format(user_input=user_input).split()
FIREBASE_INIT_CMD = 'firebase init'.split()

print(subprocess.run(FIREBASE_CREATE_PROJ_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
print(subprocess.run(FIREBASE_INIT_CMD, stdin=subprocess.PIPE, capture_output=True, cwd='.', check=True, timeout=None))
