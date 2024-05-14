from textblob import TextBlob


class EmotionAccumulator:
    def __init__(self):
        # Initialize
        self.set_cumulative_positive(0.0)
        self.set_cumulative_negative(0.0)

    def analyze_emotion(self, text):
        # calculate emotion
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            self.set_cumulative_positive(self.get_cumulative_positive() + polarity)
        elif polarity < 0:
            self.set_cumulative_negative(self.get_cumulative_negative() + abs(polarity))

        total = self.get_cumulative_positive() + self.get_cumulative_negative()
        if total == 0:
            return {'positive': 50.0, 'negative': 50.0}

        # Normalize
        normalized_positive = (self.get_cumulative_positive() / total) * 100
        normalized_negative = (self.get_cumulative_negative() / total) * 100

        return {'positive': normalized_positive, 'negative': normalized_negative}

    #Getter and Setter
    def set_cumulative_positive(self, value):
        if value >= 0:
            self.__cumulative_positive = value
        else:
            raise ValueError("Cumulative positive score cannot be negative.")

    def get_cumulative_positive(self):
        return self.__cumulative_positive

    def set_cumulative_negative(self, value):
        if value >= 0:
            self.__cumulative_negative = value
        else:
            raise ValueError("Cumulative negative score cannot be negative.")

    def get_cumulative_negative(self):
        return self.__cumulative_negative
