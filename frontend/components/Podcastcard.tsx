import { Podcast } from '@/app/page'
import Image from 'next/image'

type Props = {
  podcast: Podcast
  index: number
}

export default function PodcastCard({ podcast, index }: Props) {
  return (
    <a
      href={podcast.url}
      target="_blank"
      rel="noopener noreferrer"
      className="group flex gap-4 p-4 rounded-xl border border-[#1a1a1a] hover:border-[#2a2a2a] bg-[#0d0d12] hover:bg-[#111118] transition-all"
    >
      {/* Thumbnail */}
      <div className="w-14 h-14 rounded-lg overflow-hidden shrink-0 bg-[#1a1a1a]">
        {podcast.image ? (
          <Image
            src={podcast.image}
            alt={podcast.title}
            width={56}
            height={56}
            className="w-full h-full object-cover"
            unoptimized
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center text-[#333] text-lg font-mono">
            {index + 1}
          </div>
        )}
      </div>

      {/* Content */}
      <div className="flex-1 min-w-0">
        <p className="text-sm font-medium text-[#f0ede8] group-hover:text-white transition-colors truncate mb-1">
          {podcast.title}
        </p>
        <p className="text-xs text-[#555] line-clamp-2 leading-relaxed">
          {podcast.description || 'No description available.'}
        </p>
      </div>

      {/* Arrow */}
      <div className="text-[#333] group-hover:text-[#666] transition-colors text-sm shrink-0 self-center">
        →
      </div>
    </a>
  )
}