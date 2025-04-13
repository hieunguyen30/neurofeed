import spacy

nlp = spacy.load("en_core_web_sm")

def classify_activity(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc]

    if any(word in tokens for word in ['meet', 'call', 'conference', 'discuss']):
        return 'Work/Meeting'
    elif any(word in tokens for word in ['run', 'gym', 'exercise', 'train']):
        return 'Workout'
    elif any(word in tokens for word in ['study', 'read', 'learn', 'class']):
        return 'Study'
    elif any(word in tokens for word in ['fly', 'travel', 'trip', 'airport']):
        return 'Travel'
    elif any(word in tokens for word in ['doctor', 'hospital', 'checkup', 'medicine']):
        return 'Health'
    elif any(word in tokens for word in ['party', 'celebrate', 'birthday', 'wedding']):
        return 'Social'
    else:
        return 'Other'
