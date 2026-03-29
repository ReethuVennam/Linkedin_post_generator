import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📱", layout="wide")
    
    st.title("🚀 LinkedIn Post Generator")
    st.markdown("""
    Generate engaging LinkedIn posts tailored to your topic, length, and language preferences.
    Powered by AI for professional content creation.
    """)

    # Sidebar for additional info
    with st.sidebar:
        st.header("ℹ️ About")
        st.write("This app uses AI to create LinkedIn posts based on examples.")
        st.write("Select your preferences and click Generate!")
        st.markdown("---")
        st.write("**Features:**")
        st.write("- Topic-based generation")
        st.write("- Adjustable length")
        st.write("- Bilingual support")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        st.subheader("📌 Topic")
        selected_tag = st.selectbox("Choose a topic", options=tags, label_visibility="collapsed")

    with col2:
        st.subheader("📏 Length")
        selected_length = st.selectbox("Select length", options=length_options, label_visibility="collapsed")

    with col3:
        st.subheader("🌐 Language")
        selected_language = st.selectbox("Choose language", options=language_options, label_visibility="collapsed")

    # Generate Button
    st.markdown("---")
    if st.button("✨ Generate Post", type="primary", use_container_width=True):
        with st.spinner("Generating your post..."):
            post = generate_post(selected_length, selected_language, selected_tag)
        
        st.success("Post generated successfully!")
        st.text_area("Generated Post", value=post, height=200, label_visibility="collapsed")
        
        # Copy button
        if st.button("📋 Copy to Clipboard"):
            st.code(post, language=None)
            st.info("Post copied! (Use Ctrl+A, Ctrl+C to copy)")


# Run the app
if __name__ == "__main__":
    main()
