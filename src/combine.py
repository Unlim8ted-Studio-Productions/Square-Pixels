combined_script = ""  # Define combined_script as a global variable


def combine_scripts_with_dependencies(script_files, output_file):
    """
    Combines Python scripts and their dependencies into a single file
    Args:
        script_files: List of script file paths
        output_file: Path of the output file
    Returns: 
        None: Writes the combined script to the output file
    - Declare a global variable to store the combined script
    - Define a function to process individual scripts and add them to the combined script
    - Define a function to find dependencies in a script file by parsing import statements  
    - Iterate through script files and recursively process dependencies first
    - Once all dependencies are processed, add the script to the combined script
    - Write the combined script to the output file
    """
    global combined_script  # Declare combined_script as a global variable
    processed_files = set()

    def process_script(script_file):
        global combined_script
        with open(script_file, "r") as file:
            script_contents = file.read()
            combined_script += script_contents
            processed_files.add(script_file)

    def find_dependencies(script_file):
        """
        Find dependencies in a Python script file
        Args:
            script_file: Path to the Python script file 
        Returns:
            dependencies: List of dependencies found in the file
        - Open the script file and read its contents
        - Parse the file line by line to find import statements
        - Extract the module names from import statements
        - Return a list of unique module names"""
        with open(script_file, "r") as file:
            lines = file.readlines()
            dependencies = []

            for line in lines:
                if line.strip().startswith("import") or line.strip().startswith("from"):
                    parts = line.split()
                    if len(parts) >= 2:
                        dependency = parts[1].split(".")[0] + ".py"
                        if (
                            dependency in script_files
                            and dependency not in processed_files
                        ):
                            dependencies.append(dependency)

            return dependencies

    while script_files:
        for script_file in script_files[:]:
            dependencies = find_dependencies(script_file)

            if not dependencies or all(dep in processed_files for dep in dependencies):
                process_script(script_file)
                script_files.remove(script_file)

    # Write the combined script to the output file
    with open(output_file, "w") as output:
        output.write(combined_script)


if __name__ == "__main__":
    # List of script files to combine (in the correct order if they have dependencies)
    script_files = [
        r"SquarePixel.py",
        r"SquarePixels\eastereggs\credits_Easteregg.py",
        r"SquarePixels\enemymanagement\enemy_manager.py",
        r"SquarePixels\enemymanagement\enemy.py",
        r"SquarePixels\game\game.py",
        r"SquarePixels\multiplayer\client.py",
        r"SquarePixels\multiplayer\clientr.py",
        r"SquarePixels\multiplayer\server.py",
        r"SquarePixels\player\player.py",
        r"SquarePixels\render\render.py",
        r"SquarePixels\render\Lighting.py",
        r"SquarePixels\soundmanagement\music.py",
        r"SquarePixels\soundmanagement\MusicManager.py",
        r"SquarePixels\terraingen\terrain_gen.py",
        r"SquarePixels\uimanagement\Character_creation.py",
        r"SquarePixels\uimanagement\client_ui.py",
        r"SquarePixels\uimanagement\death.py",
        r"SquarePixels\uimanagement\inventory.py",
        r"SquarePixels\uimanagement\logo.py",
        r"SquarePixels\uimanagement\MainMen.py",
        r"SquarePixels\uimanagement\server_ui.py",
        r"SquarePixels\uimanagement\button.py",
        r"SquarePixels\uimanagement\input_feild.py",
        r"SquarePixels\uimanagement\clouds.py",
        r"SquarePixels\uimanagement\friends.py",
        r"SquarePixels\uimanagement\TextElement.py",
        r"SquarePixels\uimanagement\easy_ui_maker.py",
        r"SquarePixels\uimanagement\Checkbox.py",
        r"SquarePixels\uimanagement\Image.py",
        r"SquarePixels\uimanagement\Nodes.py",
        r"SquarePixels\uimanagement\UIpanel.py",
        r"SquarePixels\uimanagement\get_user_avatar.py",
        r"SquarePixels\uimanagement\color.py",
    ]  # Add your script file names here
    #with open("SquarePixel.egg-info\SOURCES.txt", "r") as a:
#    for index, line in enumerate(a):
#        line = a.readline(index)
#        if ".py" in line:
#            if (
#                not "combined_script" in line
#                and not "obf-combined_script" in line
#                and not "obs" in line
#                and not "tests" in line
#                and not "unfinished" in line
#            ):
#                line = line.replace("\n", "")
#                script_files.append(line)

    # Output file where the combined script will be saved
    output_file = "combined_scriptV2.py"

    combine_scripts_with_dependencies(script_files, output_file)
    print(f"Combined scripts with dependencies into '{output_file}'")
