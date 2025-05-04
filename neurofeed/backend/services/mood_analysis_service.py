from transformers import pipeline

class MoodAnalysisService:
    def __init__(self):
        # Initialize the sentiment analysis pipeline
        self.classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)
    
    def analyze_mood_text(self, text):

        if not text:
            return None
        
        predictions = self.classifier(text)
        
        moods = []
        for mood in predictions[0]:
            if mood['score'] >= 0.2: 
                moods.append(mood)
        
        return moods


'''
# Test the functions
if __name__ == "__main__":
    # Example mood text input
    test_text = "b"
    
    # Initialize the MoodAnalysisService
    mood_analyzer = MoodAnalysisService()
    
    # Analyze the mood text
    result = mood_analyzer.analyze_mood_text(test_text)
    
    # Print the results
    print(result)
'''
