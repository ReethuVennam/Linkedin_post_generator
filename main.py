import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from data_manager import DataManager
import pandas as pd


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Custom CSS for better styling
def load_custom_css():
    st.markdown("""
    <style>
    /* Main title styling */
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    /* Card-like styling for sections */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-left: 4px solid #667eea;
        padding: 16px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9ff 0%, #f0f0ff 100%);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border: 2px solid #e0e0ff;
        border-radius: 8px;
        font-size: 0.95rem;
    }
    
    /* Select box styling */
    .stSelectbox select {
        border: 2px solid #e0e0ff;
        border-radius: 8px;
    }
    
    .stSelectbox label {
        font-weight: 600;
        color: #333;
    }
    
    /* Column styling */
    .column-header {
        font-weight: 700;
        color: #667eea;
        font-size: 0.95rem;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


# Main app layout
def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="📱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    load_custom_css()
    
    st.title("🚀 LinkedIn Post Generator")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
                padding: 20px; border-radius: 10px; border-left: 4px solid #667eea;'>
    <p style='font-size: 1.1rem; color: #333; margin: 0;'>
    ✨ <b>Generate engaging LinkedIn posts</b> tailored to your topic, length, and language preferences.<br>
    Powered by AI for professional content creation.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Sidebar for additional info and data management
    with st.sidebar:
        st.markdown("## 📊 Data Management")
        
        data_tab1, data_tab2, data_tab3 = st.tabs(["📤 Upload", "✍️ Add", "👁️ View"])
        
        with data_tab1:
            st.markdown("### Upload Posts")
            st.markdown("*Upload CSV or JSON file with your posts*")
            
            uploaded_file = st.file_uploader(
                "Choose file",
                type=["csv", "json"],
                help="Required columns: text, tags, language"
            )
            
            if uploaded_file:
                df, error = DataManager.load_from_upload(uploaded_file)
                if error:
                    st.error(f"❌ {error}")
                else:
                    st.success(f"✅ Loaded {len(df)} posts!")
                    st.markdown(f"**Preview:** {df.shape[0]} rows × {df.shape[1]} columns")
                    
                    if st.button("🚀 Use this data", key="use_upload"):
                        st.session_state.uploaded_df = df
                        st.success("Data loaded! Refresh to see new topics.")
        
        with data_tab2:
            st.markdown("### Add Post Manually")
            st.markdown("*Create posts directly in the app*")
            
            with st.form("manual_post_form"):
                post_text = st.text_area(
                    "Post content",
                    height=120,
                    placeholder="Write your LinkedIn post here..."
                )
                
                post_tags = st.text_input(
                    "Tags (comma-separated)",
                    placeholder="e.g., Career, Motivation, Tech"
                )
                
                post_language = st.selectbox(
                    "Language",
                    ["English", "Hinglish"],
                    key="manual_lang_form"
                )
                
                submit = st.form_submit_button("➕ Add Post", use_container_width=True)
                
                if submit:
                    if post_text and post_tags:
                        success, msg = DataManager.add_manual_post(post_text, post_tags, post_language)
                        if success:
                            st.success("✅ " + msg)
                        else:
                            st.error("❌ " + msg)
                    else:
                        st.warning("⚠️ Please fill in all fields")
        
        with data_tab3:
            st.markdown("### Data Overview")
            
            default_df, _ = DataManager.load_default_data()
            custom_df, _ = DataManager.load_custom_data()
            
            col1, col2 = st.columns(2)
            
            default_count = len(default_df) if default_df is not None else 0
            custom_count = len(custom_df) if custom_df is not None else 0
            
            with col1:
                st.metric("📁 Default", default_count)
            
            with col2:
                st.metric("📝 Custom", custom_count)
            
            st.markdown("---")
            st.metric("📊 Total Posts", default_count + custom_count)
            
            if default_count + custom_count > 0:
                st.success(f"✅ Ready to generate!")
            else:
                st.warning(f"⚠️ Upload or add posts first")
    
    # Initialize session state for uploaded data
    if 'uploaded_df' not in st.session_state:
        st.session_state.uploaded_df = None
    
    # Load posts with dynamic data
    fs = FewShotPosts(custom_df=st.session_state.uploaded_df)
    tags = fs.get_tags()
    
    if not tags:
        st.markdown("""
        <div style='background: #fff3cd; padding: 20px; border-radius: 8px; border-left: 4px solid #ffc107;'>
        <p style='margin: 0; font-size: 1.1rem; color: #856404;'>
        ⚠️ <b>No posts available yet!</b><br>
        Please upload data or add posts manually using the sidebar.
        </p>
        </div>
        """, unsafe_allow_html=True)
        return

    # Main generation section
    st.markdown("## ✨ Generate Your Post")
    
    # Create three columns for selections
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='column-header'>📌 Select Topic</div>", unsafe_allow_html=True)
        selected_tag = st.selectbox(
            "Topic",
            options=sorted(tags),
            label_visibility="collapsed",
            key="topic_select"
        )

    with col2:
        st.markdown("<div class='column-header'>📏 Select Length</div>", unsafe_allow_html=True)
        selected_length = st.selectbox(
            "Length",
            options=length_options,
            label_visibility="collapsed",
            key="length_select"
        )

    with col3:
        st.markdown("<div class='column-header'>🌐 Select Language</div>", unsafe_allow_html=True)
        selected_language = st.selectbox(
            "Language",
            options=language_options,
            label_visibility="collapsed",
            key="lang_select"
        )

    # Generate Button
    st.markdown("---")
    
    if st.button("✨ Generate Post", type="primary", use_container_width=True, key="gen_btn"):
        with st.spinner("🤖 Creating your post..."):
            try:
                post = generate_post(selected_length, selected_language, selected_tag)
                
                st.success("✅ Post generated successfully!")
                
                # Display generated post in a nice container
                st.markdown("""
                <div style='background: #f0f4ff; padding: 20px; border-radius: 10px; 
                            border-left: 4px solid #667eea; margin: 20px 0;'>
                """, unsafe_allow_html=True)
                
                st.text_area(
                    "Your Generated Post",
                    value=post,
                    height=200,
                    disabled=True,
                    label_visibility="collapsed"
                )
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Action buttons
                st.markdown("---")
                col_copy, col_down = st.columns(2)
                
                with col_copy:
                    st.info("💡 **Tip:** Select all text (Ctrl+A) and copy (Ctrl+C) to clipboard")
                
                with col_down:
                    st.download_button(
                        label="📥 Download as TXT",
                        data=post,
                        file_name="linkedin_post.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                # Social sharing info
                st.markdown("---")
                st.markdown("""
                <div style='text-align: center; color: #666; font-size: 0.9rem; padding: 10px;'>
                🚀 Ready to share? Copy and paste your post on LinkedIn!
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Error generating post: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #999; font-size: 0.85rem; padding: 20px;'>
   
    </div>
    """, unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()
