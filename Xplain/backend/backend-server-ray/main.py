# Author: ray
# Date: 9/17/23
# Description:

from flask import Blueprint, request, jsonify, Flask

from question.ask import ask
from util.transcript import get_transcript_detail, get_context_by_ts, get_summarized_transcript

app = Flask(__name__)


@app.route('/hhh', methods=['GET'])
def hello():
    return "hello"


@app.route('/questions', methods=['POST'])
def post_question():
    data = request.get_json()

    if not data:
        return jsonify({
            "Error": "API Invalid Input"
        })

    transcript_id = data.get('transcript_id')
    time_stamp = data.get('time_stamp')
    history_data = data.get('history_data')
    question_text = data.get('question_text')

    # exist = len(Transcripts.query.filter(Transcripts.id == transcript_id).all()) > 0
    # if not exist:
    #     load_the_transcript(transcript_id)
    #
    # results = TranscriptDetails.query.filter(and_(TranscriptDetails.transcript_id == transcript_id,
    #                                               and_(TranscriptDetails.start > time_stamp - int(INTERVAL_RANGE),
    #                                                    TranscriptDetails.end < time_stamp + int(INTERVAL_RANGE)))).all()
    # context = "".join([transcript.text for transcript in results]).replace('\n', " ")
    # print(context)
    raw_trans = get_transcript_detail(video_id=transcript_id)

    context = get_context_by_ts(ts=int(time_stamp),
                                raw_trans=raw_trans,
                                interval=500)
    return jsonify({
        "answer": ask(context, question_text)
    })


@app.route('/get_summary', methods=['POST'])
def post_summary():
    data = request.get_json()

    if not data:
        return jsonify({
            "Error": "API Invalid Input"
        })

    video_id = data.get('video_id')

    # exist = Transcripts.query.filter(Transcripts.id == video_id).first()
    # print(exist)
    summ = get_summarized_transcript(video_id=video_id)

    return jsonify({
        "answer": summ
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
