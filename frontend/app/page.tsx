'use client'
 
import { useState } from 'react'
import MoodInput from '@/components/MoodInput' 
import PodcastResults from '@/components/Podcastresults'
import MoodBadge from '@/components/Moodbadge'
 
export type Podcast = {
  title: string
  description: string
  image: string
  url: string
}
 
export type RecommendResult = {
  history_id: string
  mood: string
  reason: string
  podcasts: Podcast[]
}
 
export default function Home() {
  const [result, setResult] = useState<RecommendResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
 
  async function handleSubmit(userInput: string) {
    setLoading(true)
    setError(null)
    setResult(null)
 
    try {
      const res = await fetch('http://127.0.0.1:8000/api/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_input: userInput }),
      })
 
      if (!res.ok) throw new Error('Something went wrong')
      const data: RecommendResult = await res.json()
      setResult(data)
    } catch (err) {
      setError('Could not connect to backend. Make sure it is running.')
    } finally {
      setLoading(false)
    }
  }
 
  return (
    <main className="min-h-screen bg-[#0a0a0f] text-white">
      <div className="max-w-2xl mx-auto px-6 py-16">
 
        {/* Header */}
        <div className="mb-14">
          <p className="text-xs tracking-[0.2em] uppercase text-[#666] mb-3 font-mono">
            neurofeed
          </p>
          <h1 className="text-4xl font-light leading-tight text-[#f0ede8] mb-3">
            How are you feeling<br />right now?
          </h1>
          <p className="text-[#555] text-sm">
            Tell us what's on your mind — we'll find the right podcast for your headspace.
          </p>
        </div>
 
        {/* Input */}
        <MoodInput onSubmit={handleSubmit} loading={loading} />
 
        {/* Error */}
        {error && (
          <p className="mt-4 text-sm text-red-400">{error}</p>
        )}
 
        {/* Results */}
        {result && (
          <div className="mt-12">
            <div className="flex items-center gap-3 mb-8">
              <MoodBadge mood={result.mood} />
              <p className="text-sm text-[#666]">{result.reason}</p>
            </div>
            <PodcastResults podcasts={result.podcasts} />
          </div>
        )}
      </div>
    </main>
  )
}