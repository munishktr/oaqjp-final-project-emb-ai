import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy emotion
        emotion_scores1 = emotion_detector('I am glad this happened')
        dominant_emotion1 = max(emotion_scores1, key=emotion_scores1.get)
        self.assertEqual(dominant_emotion1, 'joy')

        # Test case for anger emotion
        emotion_scores2 = emotion_detector('I am very angry right now')
        dominant_emotion2 = max(emotion_scores2, key=emotion_scores2.get)
        self.assertEqual(dominant_emotion2, 'anger')

        # Test case for disgust emotion
        emotion_scores3 = emotion_detector('I feel disgusted just hearing about this')
        dominant_emotion3 = max(emotion_scores3, key=emotion_scores3.get)
        self.assertEqual(dominant_emotion3, 'disgust')

        # Test case for sadness emotion
        emotion_scores4 = emotion_detector('I am so sad about this')
        dominant_emotion4 = max(emotion_scores4, key=emotion_scores4.get)
        self.assertEqual(dominant_emotion4, 'sadness')

        # Test case for fear emotion
        emotion_scores5 = emotion_detector('I am really afraid that this will happen')
        dominant_emotion5 = max(emotion_scores5, key=emotion_scores5.get)
        self.assertEqual(dominant_emotion5, 'fear')


if __name__ == '__main__':
    unittest.main()

        
