import unittest

from EmotionDetection import emotion_detection


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result1=emotion_detection.emotion_detection("I am glad this happened")
        self.assertEqual(result1['emotion'],'joy')

        result2=emotion_detection.emotion_detector("I am really mad about this.")
        self.assertEqual(result2['emotion'], 'anger')

        result3=emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['emotion'], 'disgust')

        result4=emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(result4['emotion'], 'sadness')

        result5=emotion_detection.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['emotion'], 'fear')