# Author: ray
# Date: 9/16/23

import unittest

from util.transcript import get_transcript_detail, transcript_to_str, get_transcript_str, get_summarized_transcript, get_context_by_ts_range


class MyTestCaseTranscript(unittest.TestCase):
    def test_transcript_getter(self):
        video_id = "78vN4sO7FVU"
        result = get_transcript_detail(video_id=video_id)
        print(f"type: {result}")

    def test_transcript_to_str(self):
        video_id = "78vN4sO7FVU"
        str_trans = get_transcript_str(video_id=video_id)
        print(str_trans)

    def test_get_summarized_transcript(self):
        video_id = "78vN4sO7FVU"
        summ = get_summarized_transcript(video_id=video_id)
        print(summ)

    def test_get_ts_range(self):
        video_id = "78vN4sO7FVU"
        summ = get_context_by_ts_range(video_id=video_id)
        print(summ)

if __name__ == '__main__':
    unittest.main()
