import axios from 'axios'

const handler = async (req, res) => {
  const chaptersUrl = 'https://yt.lemnoslife.com/videos'

  const {
    data: { items },
  } = await axios.get(chaptersUrl, {
    params: {
      part: 'chapters',
      id: req.query.lectureId,
    },
  })
  const chapters = items ? items[0].chapters.chapters : []
  res.status(200).json({
    chapters,
  })
}

export default handler
