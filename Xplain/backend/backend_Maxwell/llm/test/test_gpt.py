# Author: ray
# Date: 9/16/23

import unittest

from llm.gpt import call_gpt


class MyTestGPT(unittest.TestCase):
    def test_gpt_calling(self):
        answer = call_gpt("You are a primary school teacher who answer kids from 5 to 10 years old questions",
                                "Why sky is blue?")
        print(f"answer : {answer}")
        # print(f"hello")

if __name__ == '__main__':
    unittest.main()
