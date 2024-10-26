import { UseChatHelpers } from 'ai/react'

import { Button } from '@/components/ui/button'
import { ExternalLink } from '@/components/external-link'
import { IconArrowRight } from '@/components/ui/icons'

const exampleMessages = [
  {
    heading: 'Mi pedido no ha llegado',
    message: `¡Hola! Parece que mi café decidió tomarse un descanso antes de llegar a mi casa. ¿Podrían ayudarme a encontrarlo?`
  },
  {
    heading: 'Recibí el café equivocado',
    message: 'Pedí un cappuccino y recibí un latte. No es que no me guste el latte, pero mi cappuccino y yo teníamos planes. ¿Podrían ayudarme con esto?'
  },
  {
    heading: 'Necesito modificar mi dirección de entrega',
    message: `Intenté cambiar mi dirección de entrega, pero creo que mi café se fue a una aventura distinta. ¿Podemos redirigirlo antes de que se pierda?`
  }
]

export function EmptyScreen({ setInput }: Pick<UseChatHelpers, 'setInput'>) {
  return (
    <div className="mx-auto max-w-2xl px-4">
      <div className="rounded-lg border bg-background p-8">
        <h1 className="mb-2 text-lg font-semibold">
          Sistema de Tickets - Soluciones al Grano
        </h1>
        <p className="mb-2 leading-normal text-muted-foreground">
        ¿Problemas con tu pedido de café? Nuestra IA está aquí para ayudarte a resolver cualquier 'descafeinamiento' en el proceso. 
        </p>
        <p className="leading-normal text-muted-foreground">
        Cuéntanos tu consulta y dejemos que la tecnología y el café hagan su magia!
        </p>
        <div className="mt-4 flex flex-col items-start space-y-2">
          {exampleMessages.map((message, index) => (
            <Button
              key={index}
              variant="link"
              className="h-auto p-0 text-base"
              onClick={() => setInput(message.message)}
            >
              <IconArrowRight className="mr-2 text-muted-foreground" />
              {message.heading}
            </Button>
          ))}
        </div>
      </div>
    </div>
  )
}
