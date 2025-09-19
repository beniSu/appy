import streamlit as st
import random

st.title("🌍 Interactive Fun Program")

fun_facts = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can be 15 cm taller during hot days.",
    "Some cats are allergic to humans!"
]

if 'history' not in st.session_state:
    st.session_state['history'] = []

with st.form("main_form"):
    world_spinning = st.radio("Is the world spinning?", ("Yes", "No"))
    likes_winter = st.radio("Do you like winter?", ("Yes", "No"))
    favorite_season = st.selectbox("What's your favorite season?", ("Spring", "Summer", "Autumn", "Winter", "None"))
    favorite_activity = st.text_input("What's your favorite activity?")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("---")
    if world_spinning == "Yes":
        st.warning("Be careful not to lose your brain!")
    else:
        st.info("Standing still, huh? Interesting!")
    st.info("Winter is very cold")
    st.info("It will try to replace the true intelligence")
    if likes_winter == "Yes":
        st.success("That's great! Winter has its charm.")
    else:
        st.error("That's understandable! Winter isn't for everyone.")
    st.write(f"**Favorite season:** {favorite_season}")
    st.write(f"**Favorite activity:** {favorite_activity}")
    st.info(f"Fun fact: {random.choice(fun_facts)}")
    # Save to history
    st.session_state['history'].append({
        'World spinning': world_spinning,
        'Likes winter': likes_winter,
        'Favorite season': favorite_season,
        'Favorite activity': favorite_activity
    })
    st.write("---")
    st.write("### Your previous answers:")
    for i, entry in enumerate(st.session_state['history'], 1):
        st.write(f"**Round {i}:**", entry)
