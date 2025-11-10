#counts how many times a substring (like a letter) appears in a string

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    

    true_score = 0
    for letter in "true":
        true_score += combined_names.count(letter)
        
    love_score = 0
    for letter in "love":
        love_score += combined_names.count(letter)
    

    total_score = int(str(true_score) + str(love_score))
    
    print(total_score)
