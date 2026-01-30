## 1: (Problem 1.7.3) Python Comprehensions: Function Composition
def my_function_composition(f: dict, g: dict) -> dict:

    composition: dict = {}

    for _input, _output in f.items():
        
        if _output in g:
            composition[_input] = g[_output]

    return composition
        

## 2: Image of a function
def image(f: dict, D: set) -> set:

    images: set = set()

    for _input, _output in f.items():
        if _input in D:
            images.add(_output)

    return images
        
        
## 3: Image cardinality of a function
def image_cardinality(f: dict, D: set) -> int:

    images: set = set()

    for _input, _output in f.items():
        if _input in D:
            images.add(_output)

    return len(images)


## 4: One-to-one functions
def is_one_to_one(f: dict, D: set) -> bool:
    
    return len(list(f.values())) == len(set(f.values()))    


## 5: Onto functions
def is_onto(f: dict, D: set, C: set) -> bool:

    new = set()

    for _input, _output in f.items():
        if _input in D:
            new.add(_output)

    return new == C

## 6: Invertible functions
def is_invertible(f: dict, D: set, C: set) -> bool:

    return is_one_to_one(f, D) and is_onto(f, D, C)


## 7: Caesar Cipher Encoder
def encode(s: str) -> str:
    
    encoded: str = ""

    for letter in s:
        num: int = ord(letter)
        num += 3

        if num > 90:
            num -= 26

        encoded += chr(num)

    return encoded        


## 8: Caesar Cipher Decoder
def decode(s: str) -> str:
    
    decoded: str = ""

    for letter in s:
        num: int = ord(letter)
        num -= 3

        if num < 65:
            num += 26

        decoded += chr(num)

    return decoded



if __name__ == "__main__":
    import doctest
    doctest.testmod()


