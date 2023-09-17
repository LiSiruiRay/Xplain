import {
  Flex,
  Box,
  TextInput,
  Loader,
  Button,
  Tooltip,
  Select,
} from '@mantine/core'
import {
  BotIcon,
  SendHorizonalIcon,
  EraserIcon,
  MailSearchIcon,
  FileTextIcon,
} from 'lucide-react'
import { useState } from 'react'
import { useForm } from '@mantine/form'
import { useMantineTheme } from '@mantine/core'
import axios from '@/utils/axios'
import { languages } from '@/utils/constants'
import prettyMilliseconds from 'pretty-ms'

const Chat = ({ getCurrentTimestamp, lectureId }) => {
  const [questions, setQuestions] = useState([])
  const [answers, setAnswers] = useState([])
  const [isWaiting, setIsWaiting] = useState(false)
  const [isSummaryLoading, setSummaryLoading] = useState(false)

  const theme = useMantineTheme()

  const chatForm = useForm({
    initialValues: {
      question: '',
    },
  })
  const sendMessage = (question) => {
    const timeStamp = getCurrentTimestamp()

    setQuestions((prev) => [...prev, question])

    setIsWaiting(true)
    axios
      .post('/api/question', {
        lectureId,
        timeStamp,
        question,
        historyData: {},
      })
      .then((res) => {
        setAnswers((prev) => [...prev, res.data.answer])
        setIsWaiting(false)
      })
    chatForm.reset()
  }
  return (
    <Flex
      sx={{
        borderRadius: 20,
        border: '1px solid #ccc',
        padding: '15px',
        height: '80vh',
        width: '25vw',
        justifyContent: 'space-between',
        overflow: 'scroll',
      }}
      direction='column'>
      {/* <Select label='Language' data={languages} defaultValue='en' /> */}
      {questions.length ? (
        <Flex direction='column' gap={10}>
          {questions.map((question, index) => {
            return (
              <Flex key={index} direction='column' gap={5}>
                <Box
                  sx={{
                    borderRadius: 20,
                    backgroundColor: '#FAA2C1',
                    padding: 10,
                    color: 'white',
                    alignSelf: 'end',
                    fontWeight: 'bold',
                    background: theme.fn.linearGradient(
                      35,
                      '#ed6ea0',
                      '#ec8c69'
                    ),
                  }}>
                  {question}
                </Box>

                {answers[index] && (
                  <Box
                    sx={{
                      borderRadius: 20,
                      backgroundColor: '#845EF7',
                      padding: 10,
                      color: 'white',
                      fontWeight: 'bold',
                      backgroundColor: theme.fn.darken('#00acee', 0.05),
                    }}>
                    {answers[index]}
                  </Box>
                )}
              </Flex>
            )
          })}
        </Flex>
      ) : (
        <Box my='35%' mx='35%'>
          <MailSearchIcon size='100px' color='#DB2777' opacity={0.4} />
        </Box>
      )}
      <form
        onSubmit={chatForm.onSubmit((values) => {
          if (values.question) {
            sendMessage(values.question)
          }
        })}>
        <Flex
          sx={{
            alignItems: 'end',
            gap: 10,
          }}>
          <Tooltip label='Clear history'>
            <EraserIcon
              style={{
                cursor: 'pointer',
              }}
              onClick={() => {
                chatForm.reset()
                setQuestions([])
                setAnswers([])
              }}
            />
          </Tooltip>
          <TextInput
            {...chatForm.getInputProps('question')}
            icon={<BotIcon size='1rem' />}
            placeholder='Your question'
            mt={15}
            rightSection={
              isWaiting ? (
                <Loader size='xs' />
              ) : (
                <SendHorizonalIcon
                  style={{
                    cursor: 'pointer',
                  }}
                  color='#364FC7'
                  onClick={() => {
                    const question = chatForm.values.question

                    if (question) {
                      sendMessage(question)
                    }
                  }}
                />
              )
            }
          />

          <Tooltip label='Generate Summary'>
            <Button
              onClick={() => {
                setSummaryLoading(true)

                const timeStamp = getCurrentTimestamp()

                axios
                  .post('/api/summary', {
                    timeStamp,
                    lectureId,
                  })
                  .then((res) => {
                    setQuestions((prev) => [
                      ...prev,
                      `Get a summary for ${prettyMilliseconds(
                        timeStamp * 1000
                      )} timestamp`,
                    ])
                    setAnswers((prev) => [...prev, res.data.answer])
                    setSummaryLoading(false)
                  })
              }}
              color='yellow'>
              {isSummaryLoading ? <Loader size='xs' /> : <FileTextIcon />}
            </Button>
          </Tooltip>
        </Flex>
      </form>
    </Flex>
  )
}

export default Chat
