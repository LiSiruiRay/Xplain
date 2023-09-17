import useSWR from 'swr'
import axios from '@/utils/axios'
const useLectures = (playlistId) => {
  const fetcher = (url) => axios.get(url).then((res) => res.data)

  const { data, error, isLoading } = useSWR(`/api/lectures`, fetcher)

  return {
    data,
    isLoading,
    isError: error,
  }
}

export default useLectures
