from cx_Freeze import setup, Executable

setup(
    name="Append",
    version="1.0",
    description="Description of your application",
    executables=[Executable("excell_append.py")],
)

# Run the following command in the termial

# python freeze_setup.py build
