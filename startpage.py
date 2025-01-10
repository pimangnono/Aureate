import streamlit as st
import os
from PIL import Image
import time

st.set_page_config(
    page_title="Aureate",
    page_icon="🎶",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS to style the tabs and the file uploader text
st.markdown(
    """
    <style>
    .stTabs [role="tablist"] {
        display: flex;
        justify-content: space-between;
    }
    .stTabs [role="tab"] {
        flex-grow: 1;
        text-align: center;
    }
    .file-uploader-text {
        font-size: 20px;
        margin-bottom: 0px;
    }
    """,
    unsafe_allow_html=True,
)

st.image("resources/logo.png", width=200)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎹 Play", "🔖 User Guide", "🎼 Find Music", "🛒 Shop", "📞 Contact"])

with tab1:
    st.markdown('<p class="file-uploader-text">Upload your music piece</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the uploaded file as an image
        image = Image.open(uploaded_file)

        # Convert the image to RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Save the image to the specified directory
        save_path = os.path.join('resources/samples', uploaded_file.name)
        image.save(save_path, format='JPEG')

        # Store the name of the file in a text file
        with open('resources/samples/last_uploaded_file.txt', 'w') as f:
            f.write(save_path)

        # Show rendering for 5 seconds
        placeholder = st.empty()
        with placeholder.container():
            placeholder.progress(0, "Wait for it...")
            time.sleep(1)
            placeholder.progress(20, "Wait for it...")
            time.sleep(1)
            placeholder.progress(40, "Wait for it...")
            time.sleep(1)
            placeholder.progress(60, "Wait for it...")
            time.sleep(1)
            placeholder.progress(80, "Almost there!")
            time.sleep(1)
            placeholder.progress(100, "Ready!")
            time.sleep(1)
        placeholder.empty()
        
        # Display the output.mp4 video in the middle of the page and start it automatically
        st.video("output.mp4", start_time=0, autoplay=True, muted=True)

        time.sleep(1)

        # need to close the file and reupload the file to play the audio
        st.audio("output.wav", start_time=0, autoplay=True, loop=False)

# need to mute the computer b4 changing the tab 
with tab2:
    st.markdown("Coming soon...")

# need to mute the computer b4 changing the tab
with tab3:
    row1 = st.columns(3)
    row2 = st.columns(3)

    row1[0].container(height=120).image("resources/samples/hbd.jpg", use_container_width=True)
    row1[1].container(height=120).image("resources/samples/fire.jpg", use_container_width=True)
    row1[2].container(height=120).image("resources/samples/lost.jpg", use_container_width=True)
    row2[0].container(height=120).image("resources/samples/races.png", use_container_width=True)
    row2[1].container(height=120).image("resources/samples/sheet.jpg", use_container_width=True)
    row2[2].container(height=120).image("resources/samples/twinkle.jpg", use_container_width=True)

# need to mute the computer b4 changing the tab
with tab4:
    st.image("resources/shop1.png", use_container_width=True)
    st.image("resources/shop2.png", use_container_width=True)

with tab5:
    st.markdown("Coming soon...")