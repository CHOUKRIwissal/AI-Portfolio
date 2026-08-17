"""
Data Analysis Functions
Statistical calculations for data analysis
"""

def calculate_mean(data):
    """Calculate the mean (average) of data"""
    if not data:
        return 0
    return sum(data) / len(data)
    

def calculate_median(data):
    """Calculate the median of data"""
    if not data:
        return 0
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
        

def calculate_std(data):
    """Calculate standard deviation of data"""
    if not data or len(data) < 2:
        return 0
    
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5
    

def summarize_data(data):
    """Return dictionary of all statistics"""
    if not data:
        return {}
    
    return {
        "mean": calculate_mean(data),
        "median": calculate_median(data),
        "std": calculate_std(data),
        "min": min(data),
        "max": max(data),
        "count": len(data),
        "sum": sum(data)
    }

# Test the functions
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    summary = summarize_data(data)
    print("Data Analysis:")
    print(f"Mean: {summary['mean']:.2f}")
    print(f"Median: {summary['median']:.2f}")
    print(f"Std Dev: {summary['std']:.2f}")
    print(f"Min: {summary['min']}")
    print(f"Max: {summary['max']}")
    print(f"Count: {summary['count']}")
    print(f"Sum: {summary['sum']}")   

"""count_vowels(text) → returns number of vowels"""
def count_vowels(text):
    count = 0

    for letter in text:
        if letter in "aeiouAEIOU":
            count += 1

    return count

"""count_words(text) → returns number of words """

def count_words(text):
    words = text.split()
    count = 0

    for word in words:
        count += 1

    return count

"""is_palindrome(text) → returns True if palindrome """
def is_word_palindrome(word):
    """Check if a single word is a palindrome"""
    word = word.lower()
    return word == word[::-1]


def is_text_palindrome(text):
    """Check if a text is a palindrome, ignoring spaces and punctuation"""
    text = ''.join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]



def find_most_common(text):
    """Find the most common word in text"""
    import re
    # Split into words using regex
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    
    # Count frequency
    from collections import Counter
    counter = Counter(words)
    return counter.most_common(1)[0]

def text_analysis(text):
    """Perform comprehensive text analysis"""
    return {
        "length": len(text),
        "vowels": count_vowels(text),
        "words": count_words(text),
        "is_palindrome": is_text_palindrome(text),
        "most_common": find_most_common(text)
    }

# Test the functions
if __name__ == "__main__":
    word="layali"
    
    print("Word Analysis:")
    print(f"Word: {word}")
    print(f"Length: {len(word)}")
    print(f"Vowels: {count_vowels(word)}")
    print(f"Is Palindrome: {is_word_palindrome(word)}")



    text = "A man, a plan, a canal, Panama!"
    analysis= text_analysis(text)
    print("Text Analysis:")
    print(f"Text: {text}")
    print(f"Length: {analysis['length']}")
    print(f"Vowels: {analysis['vowels']}")
    print(f"Words: {analysis['words']}")
    print(f"Is Palindrome: {analysis['is_palindrome']}")
    print(f"Most Common: {analysis['most_common']}")


