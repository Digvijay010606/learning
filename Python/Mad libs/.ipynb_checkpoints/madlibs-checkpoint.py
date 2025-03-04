def generate_mad_lib():
    # Get the input values from the entry widgets
    noun = input("enter noun: ")
    verb = input("enter verb: ")
    adjective = input("enter adjective: ")
    place = input("enter place: ")

    # Generate the Mad Libs story
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} in {place}."
    print(story)
    

generate_mad_lib()