# Author: ray
# Date: 9/16/23
# Description:
from typing import Tuple

from llm.gpt import call_gpt


def generate_prompt(context: str, q: str) -> Tuple[str, str]:
    role_description = (
        "You are going to play a role as a tutor. A part of video transcript (context) will be provided, and there"
        " will be a specific problem between asked about that part of video transcript. Answer the question"
        " with simple langauge, highly related to the context, use an example if possible. But to provide student with most immersive "
        "experience do not mentioned 'transcript' in your answer, replace it with 'lecture', or 'video'. Also, "
        "let's go through everything step by step but also keep the answer clear and concise.")
    prompt = f"# Context: {context} \n# Question: {q}"

    return role_description, prompt


def ask(context: str, q: str) -> str:
    role_description, prompt = generate_prompt(context=context, q=q)
    answer = call_gpt(role_description, prompt)
    return answer
