# Author: ray
# Date: 9/16/23
# Description:

from youtube_transcript_api import YouTubeTranscriptApi

from llm.gpt import call_gpt


def get_transcript_detail(video_id: str) -> list:
    return YouTubeTranscriptApi.get_transcript(video_id)


def get_transcript_str(video_id: str) -> str:
    trans_list = get_transcript_detail(video_id=video_id)
    trans_str = transcript_to_str(transcript=trans_list)
    return trans_str


def transcript_to_str(transcript: list) -> str:
    str_trans = ""
    for i in transcript:
        str_trans += i["text"].replace("\n", " ") + " "
    return str_trans


def get_summarized_transcript(video_id: str, token_size: int = 3000) -> str:
    trans_str = get_transcript_str(video_id=video_id)
    spl_trans_str = trans_str.split()
    appro_l = len(spl_trans_str)
    # token_size = 3000
    sum_round = appro_l // token_size
    answer = ""
    for i in range(0, sum_round, token_size):
        text = ''.join(spl_trans_str[i: i + token_size])
        answer_dict = call_gpt(role_description="you are a good assistant",
                               prompt=f"Summarize the following passage: \n{text}")
        answer += answer_dict["content"]

    polished_summary = call_gpt(role_description="you are a good assistant",
                                prompt=f"Polish the following summary of a video, make it less "
                                       f"repetitive but do not reduce and inofrmation."
                                       f"The summary: {answer}")
    return polished_summary

def get_context_by_ts_range(video_id: str, start_ts: float, end_ts: float) -> str:
    detailed_context = get_transcript_detail(video_id)
    context_str_by_ts_range = str()
    for item in detailed_context:
        if (item["start"] > start_ts) and (item["start"] + item["duration"] < end_ts):
            context_str_by_ts_range = context_str_by_ts_range + item['text'].replace('\n', ' ') + ' '
    return context_str_by_ts_range