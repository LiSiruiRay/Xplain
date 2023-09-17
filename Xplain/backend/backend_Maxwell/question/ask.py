# Author: ray
# Date: 9/16/23
# Description:
from typing import Tuple

from llm.gpt import call_gpt


def generate_prompt(context: str, q: str) -> Tuple[str, str]:
    role_description = (
        "You are going to play a role as a tutor. A part of video transcript will be provided, and there"
        " will be a specific problem between asked about that part of video transcript. Answer the question"
        " with simple langauge and provide an example if possible.")
    prompt = f"# Context: {context} \n# Question: {q}"

    return role_description, prompt

def generate_question(context: str) -> Tuple[str, str]:
    role_description = (
        "You’re a professor who just said the following ideas in your lecture, "
        "you need to provide a question to examine students’ understanding to the"
        "material you just presented. The question should be challenging but still"
        "helpful for students who learn the material first time"
    )

    prompt = f"# Context: {context} \n"
    answer = call_gpt(role_description, prompt)
    return answer

def generate_answer(question: str) -> Tuple[str, str]:
    role_description = (
        "You’re a professor who just said the following ideas in your lecture, "
        "you just asked the question to your students"
        "Provide a detailed answer to your students"
    )

    prompt = f"# Question: {question} \n"
    answer = call_gpt(role_description, prompt)
    return answer

def ask(context: str, q: str) -> str:
    role_description, prompt = generate_prompt(context=context, q=q)
    answer = call_gpt(role_description, prompt)
    return answer
