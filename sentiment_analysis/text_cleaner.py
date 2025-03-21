import re

# Profanity list (safe to keep here if not public-facing)
PROFANITY_LIST = [
    'suck',
    'stupid',
    'pimp',
    'dumb',
    'slut',
    'damn',
    'rape',
    'poop',
    'cock',
    'crap',
    'sex',
    'nazi',
    'neo-nazi',
    'fuck',
    'bitch',
    'pussy',
    'penis',
    'vagina',
    'whore',
    'shit',
    'nigger',
    'nigga',
    'cocksucker',
    'assrape',
    'motherfucker',
    'wanker',
    'cunt',
    'faggot',
    'fags',
    'asshole',
    'piss',
    'cum'
]

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = text.lower()

    for word in PROFANITY_LIST:
        text = text.replace(word, "*" * len(word))
    
    return text