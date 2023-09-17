# Author: ray
# Date: 9/16/23
# Description:
from typing import Tuple

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


def get_summarized_transcript(video_id: str, token_size: int = 2600) -> str:
    trans_str = get_transcript_str(video_id=video_id)
    spl_trans_str = trans_str.split()
    appro_l = len(spl_trans_str)
    # token_size = 3000
    sum_round = appro_l // token_size
    answer = ""
    for i in range(0, sum_round, token_size):
        text = ''.join(spl_trans_str[i: i + token_size])
        answer_dict = call_gpt(
            role_description="you are a good learning assistant, but to provide student with most immersive "
                             "experience do not mentioned 'transcript' in your answer, replace it with 'lecture', "
                             "or 'video'."
            ,
            prompt=f"Summarize the following video (from transcript): \n{text}")
        answer += answer_dict["content"]

    polished_summary = call_gpt(role_description="you are a good assistant",
                                prompt=f"Polish the following summary of a video, make it less "
                                       f"repetitive but do not reduce the information."
                                       f"The summary: '{answer}")
    return polished_summary


def get_context(time_stamp: float, raw_trans: list):
    index = binary_search_index(time_stamp=time_stamp, raw_trans=raw_trans)
    pass


def binary_search_index(time_stamp: float, raw_trans: list) -> int:
    l, r = 0, len(raw_trans) - 1
    while l <= r:
        m = (l + r) // 2
        if raw_trans[m]["start"] > time_stamp:
            r = m - 1
        elif raw_trans[m]["start"] < time_stamp:
            l = m + 1
        else:
            return m
    return min(l, r)


def get_time_stamp_range(interval: int, time_stamp: float, raw_trans: list) -> Tuple[int, int]:
    target_index = binary_search_index(time_stamp=time_stamp, raw_trans=raw_trans)
    start_ts = max(0, time_stamp - interval)
    end_ts = min(raw_trans[-1]["start"], time_stamp + interval)
    start_index = binary_search_index(time_stamp=start_ts, raw_trans=raw_trans)
    end_ts = binary_search_index(time_stamp=end_ts, raw_trans=raw_trans)
    return start_index, end_ts


def get_context_by_ts(ts: float, raw_trans: list, interval: int):
    start_index, end_ts = get_time_stamp_range(time_stamp=ts,
                                               interval=interval,
                                               raw_trans=raw_trans)
    context_str = ""
    for i in range(start_index, end_ts + 1):
        curr_sec = raw_trans[i]
        context_str += curr_sec["text"].replace("\n", " ") + " "

    return context_str
