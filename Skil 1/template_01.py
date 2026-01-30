## 1: (Problem 1.7.3) Python Comprehensions: Function Composition
def my_function_composition(f, g):
    
    f: dict
    g: dict

    composition: dict = {}

    for _input in f:
        if _input in g:
            composition[_input] = g[input]

    return composition
        


## 2: Image of a function
def image(f, D):
    
    f: dict
    D: set

    images = []
    for _input, _output in f.values():
        if _input in D:
            images.append(_output)

    return set(images)
        
        


## 3: Image cardinality of a function
def image_cardinality(f, D):
    f: dict
    D: set

    images = []
    for _input, _output in f.values():
        if _input in D:
            images.append(_output)

    return len(set(images))


## 4: One-to-one functions
def is_one_to_one(f, D):
    
    f: dict
    D: set


    for _input in f:
        if _input not in D:
            return False
        
    return True
    


## 5: Onto functions
def is_onto(f, D, C):
    f: dict
    D: set
    C: set

    for _input, _output in f.items():
        if _input not in D or _output not in C:
            return False
    
    return True


## 6: Invertible functions
def is_invertible(f, D, C):
    
    f: dict
    D: set
    C: set

    if is_one_to_one(f, D) and is_onto(f, D, C):
        return True
    return False



## 7: Caesar Cipher Encoder
def encode(s):
    s: str
    encoded = ""

    for letter in s:
        number = ord(letter)
        encoded += chr()


## 8: Caesar Cipher Decoder
def decode(s):
    '''
    Input:
      -s: a string consisting only of capitalized letters from the english alphabet
    Output:
      -a string representing the Caesar cipher decoded version of the original string s, shifted by 3 places
    Examples:
      >>> decode("PDWULA")
      'MATRIX'

      >>> decode("ABC")
      'XYZ'
    '''
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
