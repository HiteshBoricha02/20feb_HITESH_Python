# Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            
            word_freq = {}
            
            
            for line in file:
                
                words = line.split()
                
                
                for word in words:
                    
                    word = word.strip(".,!?\"'()[]{}")
                    
                    
                    word = word.lower()
                    
                    
                    if word:
                        word_freq[word] = word_freq.get(word, 0) + 1
        
        return word_freq
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


file_path = 'example.txt'  


word_frequency = count_word_frequency(file_path)

# Print the result
print("Word Frequency:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
    
    
