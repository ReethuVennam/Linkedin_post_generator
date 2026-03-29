import json
import csv
import pandas as pd
import streamlit as st
from pathlib import Path


class DataManager:
    """Manages loading posts from various sources: JSON, CSV, and user uploads."""
    
    REQUIRED_FIELDS = ['text', 'tags', 'language']
    DATA_DIR = Path("data")
    DEFAULT_FILE = DATA_DIR / "processed_posts.json"
    CUSTOM_DATA_FILE = DATA_DIR / "custom_posts.json"
    
    @staticmethod
    def load_csv(uploaded_file):
        """Load posts from uploaded CSV file."""
        try:
            df = pd.read_csv(uploaded_file)
            # Validate required fields
            missing_fields = [field for field in DataManager.REQUIRED_FIELDS if field not in df.columns]
            if missing_fields:
                return None, f"CSV missing required fields: {', '.join(missing_fields)}"
            
            # Ensure tags is a list
            if 'tags' in df.columns and isinstance(df['tags'].iloc[0] if len(df) > 0 else None, str):
                df['tags'] = df['tags'].apply(lambda x: [t.strip() for t in str(x).split(',')])
            
            return df, None
        except Exception as e:
            return None, f"Error reading CSV: {str(e)}"
    
    @staticmethod
    def load_json(uploaded_file):
        """Load posts from uploaded JSON file."""
        try:
            data = json.load(uploaded_file)
            if not isinstance(data, list):
                return None, "JSON must be an array of posts"
            
            df = pd.json_normalize(data)
            
            # Validate required fields
            missing_fields = [field for field in DataManager.REQUIRED_FIELDS if field not in df.columns]
            if missing_fields:
                return None, f"JSON missing required fields: {', '.join(missing_fields)}"
            
            return df, None
        except Exception as e:
            return None, f"Error reading JSON: {str(e)}"
    
    @staticmethod
    def load_from_upload(uploaded_file):
        """Load posts from uploaded file (CSV or JSON)."""
        file_ext = uploaded_file.name.split('.')[-1].lower()
        
        if file_ext == 'csv':
            return DataManager.load_csv(uploaded_file)
        elif file_ext == 'json':
            return DataManager.load_json(uploaded_file)
        else:
            return None, "Unsupported file format. Please upload CSV or JSON."
    
    @staticmethod
    def load_default_data():
        """Load default processed posts from data folder."""
        try:
            if DataManager.DEFAULT_FILE.exists():
                with open(DataManager.DEFAULT_FILE, encoding='utf-8') as f:
                    posts = json.load(f)
                    df = pd.json_normalize(posts)
                    return df, None
            return None, "Default data file not found"
        except Exception as e:
            return None, f"Error loading default data: {str(e)}"
    
    @staticmethod
    def add_manual_post(text, tags_str, language):
        """Add a manually entered post to custom data."""
        try:
            DataManager.DATA_DIR.mkdir(exist_ok=True)
            
            # Parse tags
            tags = [t.strip() for t in tags_str.split(',') if t.strip()]
            
            if not text or not tags or not language:
                return False, "All fields are required"
            
            # Load existing custom posts
            existing_posts = []
            if DataManager.CUSTOM_DATA_FILE.exists():
                with open(DataManager.CUSTOM_DATA_FILE, encoding='utf-8') as f:
                    existing_posts = json.load(f)
            
            # Add new post
            new_post = {
                'text': text,
                'tags': tags,
                'language': language,
                'line_count': len(text.split('\n'))
            }
            existing_posts.append(new_post)
            
            # Save to file
            with open(DataManager.CUSTOM_DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(existing_posts, f, indent=4, ensure_ascii=False)
            
            return True, "Post added successfully!"
        except Exception as e:
            return False, f"Error adding post: {str(e)}"
    
    @staticmethod
    def load_custom_data():
        """Load manually added posts."""
        try:
            if DataManager.CUSTOM_DATA_FILE.exists():
                with open(DataManager.CUSTOM_DATA_FILE, encoding='utf-8') as f:
                    posts = json.load(f)
                    df = pd.json_normalize(posts)
                    return df, None
            return None, None
        except Exception as e:
            return None, f"Error loading custom data: {str(e)}"
    
    @staticmethod
    def merge_dataframes(dfs):
        """Merge multiple dataframes and remove duplicates."""
        if not dfs:
            return None
        
        merged = pd.concat(dfs, ignore_index=True)
        # Remove exact duplicates based on 'text' column
        merged = merged.drop_duplicates(subset=['text'], keep='first')
        return merged
    
    @staticmethod
    def export_posts_to_json(df):
        """Export dataframe to JSON format."""
        try:
            posts = df.to_dict(orient='records')
            return json.dumps(posts, indent=4, ensure_ascii=False)
        except Exception as e:
            return None


if __name__ == "__main__":
    # Test: Load default data
    df, error = DataManager.load_default_data()
    if error:
        print(f"Error: {error}")
    else:
        print(f"Loaded {len(df)} posts")
        print(df.head())
