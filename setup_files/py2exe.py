
from cx_Freeze import setup, Executable

      setup(
          name="YourAppName",
          version="1.0",
          description="Description of your application",
          executables=[Executable("your_script.py")],
      )

# Navigate to the directory where the script is saved and run the following command in the terminal:
# python setup.py py2exe
