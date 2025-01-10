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
    </style>
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
        st.audio("output.wav", start_time=0, autoplay=True)


