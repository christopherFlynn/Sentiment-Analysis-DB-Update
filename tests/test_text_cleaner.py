from sentiment_analysis.text_cleaner import clean_text

def test_clean_text_removes_url():
    text = "Check this out http://example.com"
    assert "http" not in clean_text(text)

def test_clean_text_masks_profanity():
    text = "This is fuck"
    cleaned = clean_text(text)
    assert "fuck" not in cleaned
    assert "*" * len("fuck") in cleaned
