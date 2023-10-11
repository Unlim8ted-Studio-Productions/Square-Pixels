combined_script = ""  # Define combined_script as a global variable


def combine_scripts_with_dependencies(script_files, output_file):
    global combined_script  # Declare combined_script as a global variable
    processed_files = set()

    def process_script(script_file):
        global combined_script
        with open(script_file, "r") as file:
            script_contents = file.read()
            combined_script += script_contents
            processed_files.add(script_file)

    def find_dependencies(script_file):
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
        "SquarePixel.py",
        "eastereggs\credits_Easteregg.py",
        "enemymanagement\enemy_manager.py",
        "enemymanagement\enemy.py",
        "game\game.py",
        "multiplayer\client.py",
        "multiplayer\clientr.py",
        "multiplayer\server.py",
        "player\player.py",
        r"render\render.py",
        "render\Lighting.py",
        "soundmanagement\music.py",
        "soundmanagement\MusicManager.py",
        r"terraingen\terrain_gen.py",
        "uimanagement\Character_creation.py",
        "uimanagement\client_ui.py",
        "uimanagement\death.py",
        "uimanagement\inventory.py",
        "uimanagement\logo.py",
        "uimanagement\MainMen.py",
        "uimanagement\server_ui.py",
    ]  # Add your script file names here

    # Output file where the combined script will be saved
    output_file = "combined_script.py"

    combine_scripts_with_dependencies(script_files, output_file)
    print(f"Combined scripts with dependencies into '{output_file}'")
