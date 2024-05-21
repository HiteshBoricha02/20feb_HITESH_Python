# Write a Python program to count the frequency of words in a file.

def count_word(path):
    
        # Open the file in read mode
        with open(path, 'r') as file:
            
            word = {}
            
            
            for line in file:
                
                words = line.split()
                
                
                for word in words:
                    
                    word = word.strip(".,!?\"'()[]{}")
                    
                    
                    word = word.lower()
                    
                    
                    if word:
                        word[word] = word.get(word, 0) + 1
        
        return word
    
    

file_path = 'example.txt'  


word_frequency = count_word(file_path)

# Print the result
print("Word Frequency:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
    
    
