import useLectures from '@/data/use-lectures'
import { Flex, Box, Title, NavLink, Loader, Center } from '@mantine/core'
import { useEffect, useRef, useState } from 'react'
import Chat from '@/components/Chat'
import YoutubePlayer from '@/components/YoutubePlayer'
import useChapters from '@/data/use-chapters'
import Image from 'next/image'

const Course = () => {
  const { data: lecturesData, isLoading } = useLectures('')

  const [activeLecture, setActiveLecture] = useState(0)
  const [activeChapter, setActiveChapter] = useState(1)

  const { data: chaptersData, isLoading: isChaptersLoading } = useChapters(
    lecturesData?.items[activeLecture]?.snippet?.resourceId?.videoId
  )

  const playerRef = useRef(null)

  const getCurrentTimestamp = () => {
    if (playerRef.current) {
      return playerRef.current.getCurrentTime()
    }
  }

  useEffect(() => {
    const intervalId = setInterval(() => {
      const currentTimeStamp = Math.floor(getCurrentTimestamp())
      if (
        !isChaptersLoading &&
        currentTimeStamp > chaptersData.chapters[activeChapter].time
      ) {
        setActiveChapter((prev) => prev + 1)
      }
    }, 1000)

    // Clear the interval when the component unmounts to prevent memory leaks
    return () => clearInterval(intervalId)
  }, [])

  return (
    <>
      <Image src='/logo.svg' width={200} height={50} />

      {isLoading ? (
        <Center my='25%'>
          <Loader size='xl' />
        </Center>
      ) : (
        <Flex direction='column'>
          <Title order={1} p={20}>
            {lecturesData.playlist.courseName}
          </Title>
          <Flex justify='space-around'>
            <Box w={240}>
              {lecturesData.items.map((item, index) => {
                return (
                  <NavLink
                    key={item.id}
                    label={item.snippet.title}
                    active={activeLecture == index}
                    onClick={() => {
                      setActiveLecture(index)
                    }}
                  />
                )
              })}
            </Box>

            <YoutubePlayer
              videoId={
                lecturesData.items[activeLecture].snippet.resourceId.videoId
              }
              onReady={(event) => {
                playerRef.current = event.target
              }}
            />

            <Chat
              getCurrentTimestamp={getCurrentTimestamp}
              lectureId={
                lecturesData.items[activeLecture].snippet.resourceId.videoId
              }
            />
          </Flex>
        </Flex>
      )}
    </>
  )
}

export default Course
