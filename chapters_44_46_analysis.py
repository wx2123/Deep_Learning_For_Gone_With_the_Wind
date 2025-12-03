import re
from textblob import TextBlob

# Read the book text
with open("gone_with_the_wind.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chapters
chapters = re.split(r"CHAPTER [IVXLC]+", text)[1:]

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

print("="*80)
print("ANALYSIS OF CHAPTERS 44-46")
print("="*80)

for chapter_num in range(44, 47):  # Chapters 44, 45, 46
    chapter_index = chapter_num - 1
    chapter_text = chapters[chapter_index]
    sentiment = analyze_sentiment(chapter_text)
    
    print(f"\nCHAPTER {chapter_num} (Sentiment: {sentiment:.3f})")
    print("-" * 50)
    
    # Get first 500 characters as preview
    preview = chapter_text[:500].replace('\n', ' ').strip()
    print(f"Preview: {preview}...")
    
    # Get word count
    word_count = len(chapter_text.split())
    print(f"Word count: {word_count}")
    
    # Extract key sentences (first few sentences)
    blob = TextBlob(chapter_text)
    sentences = blob.sentences[:3] if len(blob.sentences) >= 3 else blob.sentences
    print("Key sentences:")
    for i, sentence in enumerate(sentences, 1):
        sentence_str = str(sentence).replace('\n', ' ').strip()
        print(f"  {i}. {sentence_str[:100]}...")

# Compare with surrounding chapters
print("\n" + "="*80)
print("CONTEXT - SURROUNDING CHAPTERS")
print("="*80)

surrounding_chapters = [42, 43, 44, 45, 46, 47, 48]
for chapter_num in surrounding_chapters:
    chapter_index = chapter_num - 1
    chapter_text = chapters[chapter_index]
    sentiment = analyze_sentiment(chapter_text)
    print(f"Chapter {chapter_num}: {sentiment:.3f}")
