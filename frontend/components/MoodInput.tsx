'use client'

import { useState, KeyboardEvent } from 'react'

type Props = {
  onSubmit: (input: string) => void
  loading: boolean
}

export default function MoodInput({ onSubmit, loading }: Props) {
  const [value, setValue] = useState('')

  function handleSubmit() {
    if (!value.trim() || loading) return
    onSubmit(value.trim())
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit()
    }
  }

  const prompts = [
    "I'm feeling anxious about everything",
    "Need to focus and get work done",
    "Totally exhausted after a long week",
    "Stressed about school deadlines",
  ]

  return (
    <div>
      <div className="relative">
        <textarea
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="e.g. I'm stressed and can't focus..."
          rows={3}
          className="w-full bg-[#111118] border border-[#222] rounded-xl px-4 py-3 text-[#f0ede8] placeholder-[#444] text-sm resize-none focus:outline-none focus:border-[#444] transition-colors"
        />
        <button
          onClick={handleSubmit}
          disabled={!value.trim() || loading}
          className="absolute bottom-3 right-3 bg-[#f0ede8] text-[#0a0a0f] text-xs font-medium px-4 py-1.5 rounded-lg disabled:opacity-30 hover:bg-white transition-all"
        >
          {loading ? (
            <span className="flex items-center gap-1.5">
              <span className="w-3 h-3 border border-[#0a0a0f] border-t-transparent rounded-full animate-spin inline-block" />
              thinking
            </span>
          ) : 'find podcasts'}
        </button>
      </div>

      {/* Quick prompts */}
      <div className="mt-3 flex flex-wrap gap-2">
        {prompts.map((p) => (
          <button
            key={p}
            onClick={() => setValue(p)}
            className="text-xs text-[#555] border border-[#1e1e1e] rounded-full px-3 py-1 hover:border-[#333] hover:text-[#888] transition-all"
          >
            {p}
          </button>
        ))}
      </div>
    </div>
  )
}