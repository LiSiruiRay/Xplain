import useSWR from 'swr'
import axios from '@/utils/axios'
const useChapters = (lectureId) => {
  const fetcher = (url) => axios.get(url).then((res) => res.data)
    
  const { data, error, isLoading } = useSWR(
    `/api/chapters?lectureId=${lectureId}`,
    fetcher
  )

  return {
    data,
    isLoading,
    isError: error,
  }
}

export default useChapters
