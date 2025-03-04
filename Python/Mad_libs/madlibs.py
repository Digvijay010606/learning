# defining function for the madlibs
def generate_mad_lib():

    # Get the input values from the user for the madlibs
    noun = input("enter noun: ")
    verb = input("enter verb: ")
    adjective = input("enter adjective: ")
    place = input("enter place: ")

    # story of the madlibs
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} in {place}."
    # printing the story
    print(story)
    
# calling the madlibs function
generate_mad_lib()