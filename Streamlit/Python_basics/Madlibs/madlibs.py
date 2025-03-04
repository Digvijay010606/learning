import streamlit as st

st.set_page_config(
    page_title="MadLibs",
    page_icon="icon.jpeg"
    )


st.title("Welcome to")
st.image("MadLibs/logo.png")


noun = st.text_input("Noun",placeholder="Ex:-girl")
verb = st.text_input("Verb",placeholder="Ex:-visit")
adjective = st.text_input("Adjective",placeholder="beautiful")
place = st.text_input("Place",placeholder="boston")


story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} in {place}"
print(story)
    
container = st.container(border=True)
if st.button("Generate",type="secondary"):
    container.success(story)
else:
    container.write("The MadLib will display here")
    
st.button("Reset",type="primary")

