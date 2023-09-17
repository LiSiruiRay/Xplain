import YouTube from 'react-youtube'

const YoutubePlayer = ({ videoId, ...props }) => {
  return <YouTube videoId={videoId} {...props} />
}

export default YoutubePlayer
