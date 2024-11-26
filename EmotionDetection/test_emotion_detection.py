from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I love this new technology')
        self.assertEqual(result_1['dominant'], 'joy')
    
    

unittest.main()