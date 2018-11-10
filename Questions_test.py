import unittest
from Questions import Questions # from Questions file, import Questions class
 
class test_Questions(unittest.TestCase):

    # the tests are tested based the name of the test in alphabetical order

    def test_getSpecficQuestion(self):
        test_question = Questions()

        test_question.getSpecificQuestion(3)

        # test class variable question
        self.assertEqual(test_question.question, "A poke bowl is a diced raw fish?\n \
a. True\n b. False\n") # added \n at end of string from fixNewLine
        self.assertNotEqual(test_question.question, "A poke bowl is a diced raw fish?\n \
a. True\n b. False")

        # test class variable solution
        self.assertEqual(test_question.solution, "a")
        self.assertNotEqual(test_question.solution, "b")

        # test class variable pointvalue
        self.assertEqual(test_question.pointvalue, 5)
        self.assertNotEqual(test_question.pointvalue, "5")
        self.assertNotEqual(test_question.pointvalue, 10)

        # test another question (question 5)
        test_question.getSpecificQuestion(9)
        
        # test class variable question
        self.assertEqual(test_question.question, "In the game of pool, what is the \
standard color for one ball?\n Type in answer:\n")
        self.assertNotEqual(test_question.question, "In the game of pool, what is the \
standard color for one ball?\n Type in answer:")

        # test class variable solution
        self.assertEqual(test_question.solution, "yellow")
        self.assertNotEqual(test_question.solution, "blue")

        # test class variable pointvalue
        self.assertEqual(test_question.pointvalue, 20)
        self.assertNotEqual(test_question.pointvalue, "20")
        self.assertNotEqual(test_question.pointvalue, 5)
        
    # The next two tests aren't really needed, since they depend on getSpecficQuestion
    # which was tested above. The tests below test the calls
    
    def test_getQuestion(self):
        test_question = Questions() # creates/initializes object from Questions class named test question

        test_question.getSpecificQuestion(1)
        self.assertEqual(test_question.getQuestion(), "In which Asian country \
is the city of Chiang Mai located?\n a. China\n b. Thailand\n c. Cambodia\n d. Japan\n")
        # test to see if fixNewLine adds new \n characters
        self.assertNotEqual(test_question.getQuestion(), "In which Asian country \
is the city of Chiang Mai located?\n a. China\n b. Thailand\n c. Cambodia\n d. Japan")

    def test_PointValue(self):
        test_question = Questions()

        test_question.getSpecificQuestion(1) # question 1 is worth 10 pts
        self.assertEqual(test_question.getPointValue(), 10)
        self.assertNotEqual(test_question. getPointValue(), 20)

        test_question.getSpecificQuestion(4) # question 4 is worth 20 pts
        self.assertEqual(test_question.getPointValue(), 20)
        self.assertNotEqual(test_question. getPointValue(), 10)

    def test_solution(self):
        test_question = Questions()

        test_question.getSpecificQuestion(1) # question is question 1 from csv
        self.assertTrue(test_question.trySolution("b"))
        self.assertFalse(test_question.trySolution("a"))
        # check_input in the main file will lower the input text, so passing in upper-case text will not occur
        #self.assertTrue(test_question.trySolution("B")) # test if uppercase is okay
        
        test_question.getSpecificQuestion(2) # question is question 2 from csv
        self.assertTrue(test_question.trySolution("c"))
        self.assertFalse(test_question.trySolution("d"))

if __name__ == '__main__':
    unittest.main()
