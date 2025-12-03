import re
from textblob import TextBlob

# Read the book text
with open("gone_with_the_wind.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chapters
chapters = re.split(r"CHAPTER [IVXLC]+", text)[1:]

print("="*60)
print("SUMMARY OF CHAPTERS 18-21")
print("="*60)

for chapter_num in range(18, 22):  # Chapters 18, 19, 20, 21
    chapter_index = chapter_num - 1  # Convert to 0-based index
    chapter_text = chapters[chapter_index]
    
    # Analyze sentiment
    blob = TextBlob(chapter_text)
    sentiment = blob.sentiment.polarity
    
    print(f"\nCHAPTER {chapter_num} (Sentiment: {sentiment:.3f})")
    print("-" * 40)
    
    # Get first 500 characters as preview
    preview = chapter_text[:500].replace('\n', ' ').strip()
    print(f"Preview: {preview}...")
    
    # Get word count
    word_count = len(chapter_text.split())
    print(f"Word count: {word_count}")
    
    # Extract key sentences (first few sentences)
    sentences = blob.sentences[:3] if len(blob.sentences) >= 3 else blob.sentences
    print("Key sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"  {i}. {str(sentence)[:100]}...")
