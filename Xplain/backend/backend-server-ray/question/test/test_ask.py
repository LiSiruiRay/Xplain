# Author: ray
# Date: 9/16/23

import unittest

from question.ask import generate_prompt, ask


class MyTestCaseAsk(unittest.TestCase):
    def test_ask(self):
        file_name = "context_2.txt"
        file_path = f"../../resources/context/{file_name}"
        with open(file_path, 'r') as file:
            context = file.read()
        # print(f"checking context: {context}")
        answer = ask(context=context, q="What is additive relations")
        print(f"answer: {answer}")


if __name__ == '__main__':
    unittest.main()
