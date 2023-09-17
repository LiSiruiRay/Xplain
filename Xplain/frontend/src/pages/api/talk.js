import axios from 'axios'

const handler = async (req, res) => {
  const talkResponse = await fetch('http://127.0.0.1:5000/translate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: {},
  })

  return talkResponse
}
