def read_and_modify_file():
    try:
        # Ask the user for a filename
        input_filename = input("Enter the filename to read from: ")

        # Try opening and reading the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Generate new filename
        output_filename = "modified_" + input_filename

        # Write modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
