import sys
import os
import site


if (__name__ == "__main__"):
    if ("VIRTUAL_ENV" in os.environ):
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.environ['VIRTUAL_ENV_PROMPT']}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment !")
        print("Safe to install package without \
affecting the global systeme.\n")
        print("Package installation path:")
        print(site.USER_SITE)

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment !")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate    # On Windows\n")

        print("Then run this programe again")
