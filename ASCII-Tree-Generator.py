import os
import pyperclip

def generate_directory_tree(root_path, padding=""):
    tree_structure = os.path.basename(root_path)

    try:
        entries = os.listdir(root_path)
        entries.sort()  # Sort entries for consistent order
        last_entry_index = len(entries) - 1

        for i, entry in enumerate(entries):
            entry_path = os.path.join(root_path, entry)
            is_last_entry = i == last_entry_index

            if os.path.isdir(entry_path):
                subtree = generate_directory_tree(entry_path, padding + ("│   " if not is_last_entry else "    "))
                tree_structure += "\n" + padding + ("├── " if not is_last_entry else "└── ") + subtree
            else:
                tree_structure += "\n" + padding + ("├── " if not is_last_entry else "└── ") + entry

    except PermissionError:
        pass

    return tree_structure

if __name__ == "__main__":
    current_directory = os.getcwd()
    directory_tree = generate_directory_tree(current_directory)

    print("\nDirectory Tree:")
    print(directory_tree)
    pyperclip.copy(directory_tree)
    
