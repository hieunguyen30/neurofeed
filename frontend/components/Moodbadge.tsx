type Props = {
    mood: string
  }
  
  const MOOD_STYLES: Record<string, { bg: string; text: string; dot: string }> = {
    stressed:  { bg: 'bg-orange-950/50',  text: 'text-orange-300',  dot: 'bg-orange-400' },
    anxious:   { bg: 'bg-yellow-950/50',  text: 'text-yellow-300',  dot: 'bg-yellow-400' },
    tired:     { bg: 'bg-blue-950/50',    text: 'text-blue-300',    dot: 'bg-blue-400' },
    focused:   { bg: 'bg-teal-950/50',    text: 'text-teal-300',    dot: 'bg-teal-400' },
    energetic: { bg: 'bg-green-950/50',   text: 'text-green-300',   dot: 'bg-green-400' },
    happy:     { bg: 'bg-yellow-950/50',  text: 'text-yellow-300',  dot: 'bg-yellow-400' },
    sad:       { bg: 'bg-indigo-950/50',  text: 'text-indigo-300',  dot: 'bg-indigo-400' },
  }
  
  const DEFAULT = { bg: 'bg-[#1a1a1a]', text: 'text-[#888]', dot: 'bg-[#666]' }
  
  export default function MoodBadge({ mood }: Props) {
    const style = MOOD_STYLES[mood.toLowerCase()] ?? DEFAULT
  
    return (
      <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono shrink-0 ${style.bg} ${style.text}`}>
        <span className={`w-1.5 h-1.5 rounded-full ${style.dot}`} />
        {mood}
      </span>
    )
  }