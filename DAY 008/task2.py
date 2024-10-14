#multiple input function

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in  {location}?")


greet_with("Chinmayee", "Nashik")   # Position arguments

greet_with(location="Nashik", name="Chinmayee") # Keyword Arguments