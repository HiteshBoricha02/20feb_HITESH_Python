# Write a python program to find the longest words.


text = "Tops Technologies From Rajkot"
    
words = text.split()

    
longest_words = []
max_length = 0

    
for word in words:
        
    length = len(word)
        
        
    if length > max_length:
            
        max_length = length
            
        longest_words = [word]
        
    elif length == max_length:
            
        longest_words.append(word)

        
print("Longest word(s):", longest_words)
