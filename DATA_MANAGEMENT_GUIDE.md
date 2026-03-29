# Data Management Guide - LinkedIn Post Generator

This guide shows you how to use each feature of the new data management system with real examples.

---

## 📊 **Feature 1: Upload CSV File**

### What it does:
Upload a CSV file with your LinkedIn posts to use as examples for generation.

### CSV Format:
Your CSV file MUST have these 3 columns:
- `text` – The post content
- `tags` – Topics (comma-separated)
- `language` – Either "English" or "Hinglish"

### Example CSV Content:

```
text,tags,language
"Just completed my AI course! Excited to apply these skills. 🚀","Career,Learning,Tech","English"
"Failure is a stepping stone. Every setback taught me something valuable. 💪","Motivation,Success","English"
"नई technology सीखना डराता है, पर हर दिन कुछ सीखने से confidence बढ़ता है। 📚","Learning,Tech","Hinglish"
```

### How to use:
1. Open the app
2. Go to sidebar → **📊 Data Management** → **Upload** tab
3. Click "Upload CSV or JSON file"
4. Select your `example_posts.csv` file
5. Click **"Use this data"** button

✅ **Result:** Your posts are now loaded and available for generation!

---

## 📁 **Feature 2: Upload JSON File**

### What it does:
Upload a JSON file with posts (alternative to CSV).

### JSON Format:
Must be an array of objects with these fields:
```json
[
  {
    "text": "Your post content here",
    "tags": ["Tag1", "Tag2"],
    "language": "English",
    "line_count": 3
  }
]
```

### Example JSON:

```json
[
  {
    "text": "Today I launched my first project! 🎉",
    "tags": ["Career", "Entrepreneurship"],
    "language": "English",
    "line_count": 2
  },
  {
    "text": "Network > NetWorth. Great conversation today! 💬",
    "tags": ["Networking", "Growth"],
    "language": "English",
    "line_count": 2
  },
  {
    "text": "Machine Learning exciting है! Fundamentals पर focus करो। 🤖",
    "tags": ["Tech", "Learning"],
    "language": "Hinglish",
    "line_count": 2
  }
]
```

### How to use:
1. Go to sidebar → **📊 Data Management** → **Upload** tab
2. Click "Upload CSV or JSON file"
3. Select your `example_posts.json` file
4. Click **"Use this data"** button

---

## 📝 **Feature 3: Add Manual Post**

### What it does:
Add posts directly in the app without uploading files.

### Example:

**User Input:**
- Post content: 
  ```
  Just finished a successful project launch! 
  Grateful for my amazing team. 
  Success is a team effort. 🎯
  ```
- Tags: `Career,Achievement,Leadership`
- Language: `English`

### How to use:
1. Go to sidebar → **📊 Data Management** → **Add Manual** tab
2. Fill in the form:
   - **Post content:** Paste your post text
   - **Tags:** Enter tags separated by commas (e.g., `Career,Tech,Motivation`)
   - **Language:** Select `English` or `Hinglish`
3. Click **➕ Add Post** button

✅ **Result:** Post is saved and immediately available for generation!

---

## 👁️ **Feature 4: View Data**

### What it does:
See how many posts you have loaded from all sources.

### Example Info:
```
📁 Default posts: 5 (from processed_posts.json)
📝 Custom posts: 3 (posts you added manually)
📊 Total: 8 posts
```

### How to use:
1. Go to sidebar → **📊 Data Management** → **View Data** tab
2. You'll see a breakdown of all posts in the system

---

## 🎯 **Feature 5: Generate Post**

### What it does:
Generate a new post using the AI and your uploaded/added posts as examples.

### Step-by-step Example:

**Input:**
- Topic: `Career`
- Length: `Medium` (6-10 lines)
- Language: `English`

**Process:**
- App finds 2-3 example posts with "Career" tag
- Uses them as writing style reference
- AI generates a new unique post

**Output:**
```
Excited to announce that I've just completed an advanced Python certification! 🎓

This journey taught me the importance of continuous learning in tech. 
The road wasn't easy, but every challenge strengthened my problem-solving skills.

Now I'm ready to apply these skills to exciting new projects. 
Special thanks to my mentors who guided me throughout this journey.

What's your latest learning achievement? 💡
```

### How to use:
1. Make sure you've uploaded data (Step 1-4 above)
2. In the main app, select:
   - **Topic** (from available tags)
   - **Length** (Short/Medium/Long)
   - **Language** (English/Hinglish)
3. Click **✨ Generate Post**
4. Copy or download your post

---

## 📋 **Feature 6: Copy & Download**

### Copy to Clipboard:
1. Click **📋 Copy to Clipboard** button
2. It displays the post in a code block
3. Use `Ctrl+A` then `Ctrl+C` to copy

### Download as TXT:
1. Click **📥 Download as TXT** button
2. File is saved as `linkedin_post.txt`

---

## 🚀 **Complete Workflow Example**

### Scenario: You want to generate career-focused posts

**Step 1: Prepare your data**
- Download example files from `resources/` folder
- Use `example_posts.csv` or `example_posts.json`

**Step 2: Upload to app**
- Open app (http://localhost:8501)
- Go to sidebar → Upload tab
- Upload `example_posts.csv`
- Click "Use this data"

**Step 3: Add custom posts** (optional)
- Go to Add Manual tab
- Add your favorite posts (2-3 examples)
- This helps AI understand your writing style better

**Step 4: View available data**
- Go to View Data tab
- Confirm you have 8+ posts loaded

**Step 5: Generate posts**
- Select Topic: `Career`
- Select Length: `Medium`
- Select Language: `English`
- Click **✨ Generate Post**

**Step 6: Use the post**
- Review generated post
- Click **📥 Download as TXT** to save
- Share on LinkedIn! 🚀

---

## ❓ **Troubleshooting**

### "No posts available" warning
- **Fix:** Upload CSV/JSON or add posts manually

### "Tags missing" error
- **Fix:** Ensure your CSV/JSON has proper format with tags column

### Error reading file
- **Fix:** 
  - Check file is CSV or JSON only
  - Check column names match: `text`, `tags`, `language`
  - Use commas to separate tags

### No topics in dropdown
- **Fix:** Ensure at least one post is loaded with proper tags

---

## 📂 **File Locations**

- Example CSV: `resources/example_posts.csv`
- Example JSON: `resources/example_posts.json`
- Uploaded data: Auto-saved in session
- Custom posts: `data/custom_posts.json`
- Default posts: `data/processed_posts.json`

---

Happy generating! 🎉
