#!/bin/bash

# Set the name of your main Python script
MAIN_SCRIPT="SquarePixel.py"

# Output directory
OUTPUT_DIR="modules"

# Output C++ source file
OUTPUT_CPP="$OUTPUT_DIR/embedded_python.cpp"

# List of dependencies
DEPENDENCIES=(
    "SquarePixels/eastereggs/credits_Easteregg.py"
    "SquarePixels/enemymanagement/enemy_manager.py"
    "SquarePixels/enemymanagement/enemy.py"
    "SquarePixels/game/game.py"
    "SquarePixels/multiplayer/client.py"
    "SquarePixels/multiplayer/clientr.py"
    "SquarePixels/multiplayer/server.py"
    "SquarePixels/player/player.py"
    "SquarePixels/render/render.py"
    "SquarePixels/render/Lighting.py"
    "SquarePixels/soundmanagement/music.py"
    "SquarePixels/soundmanagement/MusicManager.py"
    "SquarePixels/terraingen/terrain_gen.py"
    "SquarePixels/uimanagement/Character_creation.py"
    "SquarePixels/uimanagement/client_ui.py"
    "SquarePixels/uimanagement/death.py"
    "SquarePixels/uimanagement/inventory.py"
    "SquarePixels/uimanagement/logo.py"
    "SquarePixels/uimanagement/store.py"
    "SquarePixels/uimanagement/transition.py"
    "SquarePixels/uimanagement/EllipsesWarning.py"
    "SquarePixels/uimanagement/MainMen.py"
    "SquarePixels/uimanagement/server_ui.py"
    "SquarePixels/uimanagement/elements/button.py"
    "SquarePixels/uimanagement/elements/input_feild.py"
    "SquarePixels/uimanagement/elements/slider.py"
    "SquarePixels/uimanagement/elements/numeric_input.py"
    "SquarePixels/uimanagement/clouds.py"
    "SquarePixels/uimanagement/friends.py"
    "SquarePixels/uimanagement/elements/TextElement.py"
    "SquarePixels/uimanagement/easy_ui_maker.py"
    "SquarePixels/uimanagement/elements/Checkbox.py"
    "SquarePixels/uimanagement/elements/Image.py"
    "SquarePixels/uimanagement/elements/unfinished/Nodes.py"
    "SquarePixels/uimanagement/elements/unfinished/musicmaker.py"
    "SquarePixels/uimanagement/UIpanel.py"
    "SquarePixels/uimanagement/get_user_avatar.py"
    "SquarePixels/uimanagement/elements/color.py"
)

# Create the output directory
mkdir -p $OUTPUT_DIR

# Convert the main Python script to a C array
xxd -i $MAIN_SCRIPT > $OUTPUT_DIR/$MAIN_SCRIPT.h

# Create the C++ source file
echo -e "#include <Python.h>\n" > $OUTPUT_CPP
for DEPENDENCY in "${DEPENDENCIES[@]}"; do
    HEADER_NAME="${DEPENDENCY//\//_}.h"
    echo -e "#include \"$OUTPUT_DIR/$HEADER_NAME\"" >> $OUTPUT_CPP
done
echo -e "\nint main() {" >> $OUTPUT_CPP
echo -e "\tPy_Initialize();\n" >> $OUTPUT_CPP

# Include the main Python script header
echo -e "\tPyRun_SimpleString(${MAIN_SCRIPT/_/});\n" >> $OUTPUT_CPP

# Iterate over dependencies and convert them to C arrays
for DEPENDENCY in "${DEPENDENCIES[@]}"; do
    PYTHON_SCRIPT="$DEPENDENCY"
    HEADER_NAME="${DEPENDENCY//\//_}.h"
    xxd -i $PYTHON_SCRIPT > $OUTPUT_DIR/$HEADER_NAME

    # Include the dependency Python script header in the main program
    SCRIPT_NAME=$(basename $PYTHON_SCRIPT)
    echo -e "\tPyRun_SimpleString(${SCRIPT_NAME//./_});" >> $OUTPUT_CPP
done

# Finalize the C++ source file
echo -e "\n\tPy_Finalize();\n\n\treturn 0;\n}" >> $OUTPUT_CPP

echo "C++ source file and headers saved to $OUTPUT_DIR"
