import json
from pathlib import Path
from data_manager import DataManager

# Post to add
post = {
    "text": "Investing in your career is one of the most valuable investments you can make. It not only boosts your professional growth but also enhances your personal development. #CareerGrowth #ProfessionalDevelopment",
    "tags": ["Career", "Professional Development", "Growth"],
    "language": "English",
    "line_count": 3
}

# Add to custom posts
success, message = DataManager.add_manual_post(
    text=post["text"],
    tags_str=", ".join(post["tags"]),
    language=post["language"]
)

print(f"✅ {message}" if success else f"❌ {message}")

# Verify it was added
custom_df, _ = DataManager.load_custom_data()
if custom_df is not None:
    print(f"\n📊 Custom posts loaded: {len(custom_df)}")
    print(f"\n📝 Last added post:")
    last_post = custom_df.iloc[-1]
    print(f"   Text: {last_post['text'][:80]}...")
    print(f"   Tags: {last_post['tags']}")
    print(f"   Language: {last_post['language']}")
