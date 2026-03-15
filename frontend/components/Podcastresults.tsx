import { Podcast } from '@/app/page'
import PodcastCard from './Podcastcard'

type Props = {
  podcasts: Podcast[]
}

export default function PodcastResults({ podcasts }: Props) {
  if (podcasts.length === 0) {
    return (
      <p className="text-sm text-[#555]">
        No podcasts found for this mood. Try describing how you feel differently.
      </p>
    )
  }

  return (
    <div>
      <p className="text-xs tracking-[0.15em] uppercase text-[#444] font-mono mb-5">
        {podcasts.length} suggestion{podcasts.length !== 1 ? 's' : ''}
      </p>
      <div className="flex flex-col gap-3">
        {podcasts.map((podcast, i) => (
          <PodcastCard key={i} podcast={podcast} index={i} />
        ))}
      </div>
    </div>
  )
}