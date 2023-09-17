from database.database import Transcripts, TranscriptDetails, db
from util.transcript import get_transcript_str, get_transcript_detail, get_summarized_transcript

def load_the_transcript(video_id: str):
    new_video = Transcripts(
        id=video_id,
        full_text=get_transcript_str(video_id),
        summary=get_summarized_transcript(video_id)["content"],
    )

    db.session.add(new_video)
    db.session.commit()

    for item in get_transcript_detail(video_id = video_id):
        transcript_detail = TranscriptDetails(
            transcript_id = video_id,
            start = item['start'],
            text = item['text'],
            duration = item['duration'],
            end = item['start'] +  item['duration'],
        )

        db.session.add(transcript_detail)
        db.session.commit()
