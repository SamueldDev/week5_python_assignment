# file_handling_assignment.py

# File creation and writing
try:
    # Create a new file and open it in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Write three lines of text, including strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("12345 is a number.\n")
        file.write("This is the third line with some text.\n")
    print("File 'my_file.txt' created and written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while creating the file: {e}")

# Reading and displaying the file content
try:
    # Open the file in read mode ('r')
    with open("my_file.txt", 'r') as file:
        print("\nReading the contents of 'my_file.txt':")
        # Read and print the content
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to read 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Appending additional lines
try:
    # Open the file in append mode ('a')
    with open("my_file.txt", 'a') as file:
        # Append three new lines
        file.write("This is an appended line.\n")
        file.write("Appended number: 67890.\n")
        file.write("Another appended text line.\n")
    print("\nThree new lines appended to 'my_file.txt'.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while appending to the file: {e}")

# Read the file again to display the updated content
try:
    with open("my_file.txt", 'r') as file:
        print("\nReading the updated contents of 'my_file.txt':")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to read 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("\nFile handling operations complete.")
