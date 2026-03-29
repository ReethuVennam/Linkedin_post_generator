import pandas as pd
import json
from data_manager import DataManager


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json", custom_df=None):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path, custom_df)

    def load_posts(self, file_path, custom_df=None):
        """Load posts from default file and/or custom dataframe."""
        dfs_to_merge = []
        
        # Load default posts
        default_df, _ = DataManager.load_default_data()
        if default_df is not None:
            dfs_to_merge.append(default_df)
        
        # Load custom manually added posts
        custom_uploaded_df, _ = DataManager.load_custom_data()
        if custom_uploaded_df is not None:
            dfs_to_merge.append(custom_uploaded_df)
        
        # Load user-provided dataframe (from upload)
        if custom_df is not None:
            dfs_to_merge.append(custom_df)
        
        # Merge all dataframes
        if dfs_to_merge:
            self.df = DataManager.merge_dataframes(dfs_to_merge)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            
            # Collect unique tags
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))
        else:
            self.df = pd.DataFrame()
            self.unique_tags = []

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  # Tags contain 'Influencer'
            (self.df['language'] == language) &  # Language is 'English'
            (self.df['length'] == length)  # Line count is less than 5
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    # print(fs.get_tags())
    posts = fs.get_filtered_posts("Medium","Hinglish","Job Search")
    print(posts)