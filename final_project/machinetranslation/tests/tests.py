import unittest, translator

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase): 
    def testenglishToFrench(self): 
        self.assertIsNotNone(englishToFrench)
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # test Hello input translated output is Bonjour.
        self.assertEqual(englishToFrench("The sky is blue"), "Le ciel est bleu") # test "The sky is blue" input, output "Le ciel est bleu".

    def testfrenchToEnglish(self): 
        self.assertIsNotNone(frenchToEnglish)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") # test Bonjour input translated output is Hello.
        self.assertEqual(frenchToEnglish("Le ciel est bleu"), "The sky is blue") # test "The sky is blue" translation is "Le ciel est bleu".
unittest.main()
    