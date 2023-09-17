import axios from 'axios'

const handler = async (req, res) => {
  try {
    const videosUrl = 'https://www.googleapis.com/youtube/v3/playlistItems'

    const playlistUrl = 'https://www.googleapis.com/youtube/v3/playlists'
    const {
      data: { items },
    } = await axios.get(videosUrl, {
      params: {
        part: 'snippet',
        playlistId: 'PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY',
        key: process.env.YOUTUBE_KEY,
        maxResults: 50,
      },
    })

    const { data: playlistData } = await axios.get(playlistUrl, {
      params: {
        part: 'snippet',
        id: 'PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY',
        key: process.env.YOUTUBE_KEY,
        maxResults: 50,
      },
    })

    const courseName = playlistData.items[0].snippet.title

    res.status(200).json({
      playlist: {
        courseName,
      },
      items,
    })
  } catch (error) {
    console.error('Error fetching playlist videos:', error.message)

    res.status(500).json({
      status: 500,
      message: 'Server error occured',
    })
  }
}

export default handler
