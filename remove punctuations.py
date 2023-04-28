import string
def remove_punctuations(input_string):
    
    punctuations = set(string.punctuation)
    
    output_string = ''.join(char for char in input_string if char not in punctuations)
    
    return output_string

input_string = "Hello, Thribhu ! are u okay today?"
output_string = remove_punctuations(input_string)
print(output_string)
