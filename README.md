# Stand-alone
Documentation to create .exe files
All examples can be found in the main folder.

############################  pyinstaller  ############################ 

The advantage of using pyinstaller is that no setup file is needed to create a .exe from a python script.

In order to install pyinstaller:

    pip install pyinstaller

In the terminal navigate to the folder where the Python script is saved, this step is important to complete the execution.
To navigate in the terminal you need the following commands:

    View the current directory location: ls
    Navigate to the next folder: cd _folder/file_name
    Go back to the previous folder: cd ..

It is important for the file to be saved for any changes made to appear on the .exe
Once in the correct directory, the following line must be run in the terminal:

    pyinstaller 'your script file name'

After running the command above you will have to wait some time, depending on the complexity of the program it can take more or less time, let it run 
until it has clearly finished, either giving you the usual prompt in the terminal with your current directory location, or an error.

This will create two main folders:

    - A dist folder (distribution) meant to distribute to users
    - A build folder with secondary documents (non important)


############################ IMPORTANT ############################

When creating a stand-alone python script you need to take into consideration that once the last
function of the code is executed, the program will
close automatically.

In order to avoid this from happening a main function has to be definde to keep the window open until the user chooses to close it.

    def main()

    # Your code here

    input("Press Enter to exit...")

    if __name__ == "__main__":
    main()


############# 1st example: NO library and NO GUI #############

In order to find the limtations on pyinstaller for our systems we will start by creating a standalone app with a very simple script that contains no libraries and no GUI.

    def main():
        answer = input("Y/N: ")
        a = answer.upper()

        if a == 'Y':
            print("Your input was Y")

        elif a == 'N':
            print("Your input was N")

        input("Press Enter to exit...")

    if __name__ == "__main__":
        main()

This example works in the correctly in the terminal and in the .exe version of the script.


############# 2nd example: YES library and NO GUI #############

We will make a .exe file from the follwing python scipt. 
The additional step on this version is including a library, in this ca numpy.

    import numpy as np
    def main(): 
        
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))

        arr1 = np.array([a, b, c])
        arr2 = np.array([2, 5, 7])

        result = arr1 + arr2

        print("Result of addition:", result)

        result = arr1 * arr2

        print("Result of multiplication:", result)


    if __name__ == "__main__":
        main()

This version also works when including th pyinstaller step, the .exe provides the correct functions that the code includes.


############# 3rd example: YES GUI #############

The following script creates a window with two buttons (using PYQT) when the red button is clicked the page turns red and the same happend for the green button.

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            
            self.setWindowTitle("Color Changer")
            self.setGeometry(200, 200, 400, 300)

            self.button_green = QPushButton("Green", self)
            self.button_green.setGeometry(100, 100, 100, 50)
            self.button_green.clicked.connect(self.change_to_green)

            self.button_red = QPushButton("Red", self)
            self.button_red.setGeometry(200, 100, 100, 50)
            self.button_red.clicked.connect(self.change_to_red)

        def change_to_green(self):
            self.setStyleSheet("background-color: green;")

        def change_to_red(self):
            self.setStyleSheet("background-color: red;")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

The functions set in the script work correctly and the GUI appears correctly.

With all GUI .exe files a secondary console is created in the background. This isn't an issue, however it could be annoying for the user.
In order to avoid the console from appearing the following promt can beadded to the pyinstaller command:

    pyinstaller --noconsole your_script.py

However in my experience the following message and error occur:

    Operation did not complete successfully because the file contains a virus or potentially unwanted software.'


For more complex scripts additional research is still underway.




############# Distribution of .exe files #############

Once the file has been created, the main goal is to share the application with the user, however most of the time sending just a .exe file will not work.

Here are the following steps to share a .exe file for it to work on the users device:

    - Create a folder where you can place all files generated when using the      pyinstaller command: build, dist and .spec files.

    - Compress the folder and upload it to one-drive

    - The user should un-zip the file and navigate to the .exe file on the dist folder


######################## OTHER TOOLS ############################

There are more tools to create.exe files. Pyinstaller is the most common you can find, however here are some others that provide more options. 



############################  cx_Freeze  ############################

Installing cx_freeze:

    pip install cx_Freeze

An additional file is required in the same directory as the python script that contains the desired code.
Create a .py file containing the following setup code:

    from cx_Freeze import setup, Executable

        setup(
            name="YourAppName",
            version="1.0",
            description="Description of your application",
            executables=[Executable("your_script.py")],
        )

Navigate to the directory where the script is saved and run the following command in the terminal:

    python setup.py build

Wait a few seconds, the terminal should show the function running.

When using this function the following error appears:
"RecursinError: maximum recursion depth exceeded while calling a Python object"



############################  py2exe  ############################

Installing py2exe:

    pip install py2exe

An additional file is required in the same directory as the python script that contains the desired code.
Create a .py file containing the following setup code:

    from cx_Freeze import setup, Executable

        setup(
            name="YourAppName",
            version="1.0",
            description="Description of your application",
            executables=[Executable("your_script.py")],
        )

Navigate to the directory where the script is saved and run the following command in the terminal:

    python setup.py py2exe

Wait a few seconds, the terminal should show the function running.

The following error appears:
"AttributeError: 'NoneType' object has no attribute 'get_source'"


############################  auto-py-to-exe  ############################

Google Chrome is required to use the auto-py-to-exe converter, it can be installed on the IT-shop.

Once Chrome is installed the same has to be done with auto-py-to-exe:

    pip install auto-py-to-exe

Then the following prompt has to be run in the terminal:

    auto-py-to-exe

This command will open a Google Chrome window where all the data from the python script should be completed.

With this method the antivirus triggers a stop command:

    win32ctypes.pywin32.pywintypes.error: (225, 'BeginUpdateResourceW', 'Operation did not complete successfully because the file contains a virus or potentially unwanted software.')

    Project output will not be moved to output folder
    Complete.


############################  Nuitka  ############################

As with the previous methods:

    pip install nuitka

In the terminal the following command needs to be run:

    nuitka --standalone your_script_name.py

This method is longer it will take about 1 hour or more and no final result
