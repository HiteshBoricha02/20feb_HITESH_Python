
# • Write a Python program to copy the contents of a file to another file.

def copy_file(s_file, d_file):
    
       
        with open(s_file, 'r') as src, open(d_file, 'w') as dst:
            
            for line in src:
                dst.write(line)
        print(f"Contents of {s_file} have been copied to {d_file} successfully.")
   
s_file = 'example.txt'  
d_file = 'data.txt' 


copy_file(s_file, d_file)


