
# • Write a Python program to copy the contents of a file to another file.

def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode 
        with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
            
            for line in src:
                dst.write(line)
        print(f"Contents of {source_file} have been copied to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"The file {source_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# path of two file 
source_file = 'example.txt'  
destination_file = 'data.txt' 


copy_file(source_file, destination_file)


