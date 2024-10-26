import * as React from 'react'
import Textarea from 'react-textarea-autosize'
import { UseChatHelpers } from 'ai/react'
import { useEnterSubmit } from '@/lib/hooks/use-enter-submit'
import { Button } from '@/components/ui/button'
import { IconArrowElbow } from '@/components/ui/icons'

export interface PromptProps
  extends Pick<UseChatHelpers, 'input' | 'setInput'> {
  onSubmit: (value: string) => Promise<void>
  isLoading: boolean
}

export function PromptForm({
  onSubmit,
  input,
  setInput,
  isLoading
}: PromptProps) {
  const { formRef, onKeyDown } = useEnterSubmit()
  const inputRef = React.useRef<HTMLTextAreaElement>(null)

  React.useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus()
    }
  }, [])

  return (
    <form
      onSubmit={async e => {
        e.preventDefault()
        if (!input?.trim()) {
          return
        }
        setInput('')
        await onSubmit(input)
      }}
      ref={formRef}
      className="fixed bottom-4 left-1/2 transform -translate-x-1/2 flex items-center gap-3 bg-white shadow-md rounded-full px-6 py-3 w-10/12 max-w-lg"
    >
      <Textarea
        ref={inputRef}
        tabIndex={0}
        onKeyDown={onKeyDown}
        rows={1}
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Escribe aquí tu consulta..."
        spellCheck={false}
        className="flex-grow resize-none bg-transparent px-2 py-2 text-sm outline-none focus:outline-none"
      />

      <Button
        type="submit"
        size="icon"
        disabled={isLoading || input === ''}
        className="p-3 h-10 w-10"
      >
        <IconArrowElbow className="h-6 w-6" />
        <span className="sr-only">Enviar mensaje</span>
      </Button>
    </form>
  )
}
