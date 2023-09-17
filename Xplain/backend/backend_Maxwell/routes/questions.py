from flask import Blueprint, request, jsonify
from sqlalchemy import and_

import sys
sys.path.append('..')
from database.database import db, Transcripts, TranscriptDetails
from question.ask import ask
from status_code.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_200_OK
from util.transcript import get_context_by_ts_range
from question.ask import generate_question, generate_answer
from import_data import load_the_transcript

from dotenv import load_dotenv
import os

load_dotenv()
INTERVAL_RANGE = os.getenv("INTERVAL_RANGE")

questions = Blueprint('questions', __name__)

@questions.route('/questions', methods = ['POST'])
def post_question():
    data = request.get_json()

    if not data:
        return jsonify({
            "Error": "API Invalid Input"
        }), HTTP_400_BAD_REQUEST

    transcript_id = data.get('transcript_id')
    time_stamp = data.get('time_stamp')
    history_data = data.get('history_data')
    question_text = data.get('question_text')

    exist = len(Transcripts.query.filter(Transcripts.id == transcript_id).all()) > 0
    if not exist:
        load_the_transcript(transcript_id)

    results = TranscriptDetails.query.filter(and_(TranscriptDetails.transcript_id == transcript_id,and_(TranscriptDetails.start > time_stamp - int(INTERVAL_RANGE), TranscriptDetails.end < time_stamp + int(INTERVAL_RANGE)))).all()
    context = "".join([transcript.text for transcript in results]).replace('\n', " ")
    print(context)

    return jsonify({
        "answer": ask(context, question_text)
    }), HTTP_200_OK

@questions.route('/get_summary', methods = ['POST'])
def post_summary():
    data = request.get_json()

    if not data:
        return jsonify({
            "Error": "API Invalid Input"
        }), HTTP_400_BAD_REQUEST

    video_id = data.get('video_id')

    exist = Transcripts.query.filter(Transcripts.id == video_id).first()
    print(exist)

    return jsonify({
        "answer": exist.summary
    }), HTTP_200_OK

@questions.route('/get_quiz_question', methods = ['POST'])
def get_quiz_question():
    data = request.get_json()

    video_id = data.get('video_id')
    time_stamp_start = data.get('time_stamp_start')
    time_stamp_end = data.get('time_stamp_end')

    context_by_ts_range = get_context_by_ts_range(video_id = video_id, start_ts = time_stamp_start, end_ts = time_stamp_end)
    question = generate_question(context = context_by_ts_range)

    return jsonify({
        "question": question["content"],
    }), HTTP_200_OK

@questions.route('/get_quiz_answer', methods = ['POST'])
def get_quiz_answer():
    data = request.get_json()
    question = data.get('question')

    answer = generate_answer(question = question)

    return jsonify({
        "answer": answer["content"],
    }), HTTP_200_OK
