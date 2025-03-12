import unittest

from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    # Helper Function
    def check_text_for_dominance(self, text, expected):
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected)

    def test_joy(self):
        self.check_text_for_dominance("I am glad this happened", "joy")

    def test_anger(self):
        self.check_text_for_dominance("I am really mad about this", "anger")

    def test_disgust(self):
        self.check_text_for_dominance("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self.check_text_for_dominance("I am so sad about this", "sadness")

    def test_fear(self):
        self.check_text_for_dominance("I am really afraid this will happen", "fear")

if __name__ == '__main__':
    unittest.main()
