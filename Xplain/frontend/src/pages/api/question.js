import axios from 'axios'

const handler = async (req, res) => {
  try {
    const { data } = await axios.post(process.env.GPT_URL + '/questions', {
      transcript_id: req.body.lectureId,
      time_stamp: req.body.timeStamp,
      question_text: req.body.question,
      history_data: req.body.historyData,
    })

    res.status(200).json({
      answer: data.answer.content,
    })
  } catch (error) {
    console.error('Error fetching question:', error.message)

    res.status(500).json({
      status: 500,
      message: 'Server error occured',
    })
  }
}

export default handler
