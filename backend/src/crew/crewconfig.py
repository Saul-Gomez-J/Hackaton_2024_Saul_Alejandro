from crewai import Agent, Task, Crew, Process
from src.tools.cafe_tool import SupabaseCafeTool
from src.tools.pedido_tool import SupabasePedidoTool
from src.tools.gpt4o_tool import GPT4oTool
from src.tools.claude_tool import ClaudeTool

# Crear instancias de las herramientas específicas de Supabase
cafe_tool = SupabaseCafeTool()         # Herramienta para recomendar cafés basada en preferencias
pedido_tool = SupabasePedidoTool()      # Herramienta para consultar el estado de pedidos

# Crear instancias de las herramientas de LLM (GPT-4o-mini y Claude Haiku)
gpt4o_tool = GPT4oTool()                # Herramienta para usar GPT-4o-mini
claude_tool = ClaudeTool()              # Herramienta para usar Claude Haiku

# Agente Experto en Cafés
experto_en_cafes = Agent(
    role="Experto en Cafés",
    goal="Recomendar cafés según las preferencias del cliente.",
    backstory="Especialista en cafés de la tienda, experto en perfiles de sabor y variedades.",
    tools=[cafe_tool, gpt4o_tool]  # Asignamos la herramienta de café y GPT-4o para recomendaciones
)

# Agente de Soporte de Pedidos
soporte_pedidos = Agent(
    role="Soporte de Pedidos",
    goal="Resolver dudas sobre el estado de pedidos realizados.",
    backstory="Especialista en seguimiento de pedidos y soporte al cliente.",
    tools=[pedido_tool, claude_tool]  # Asignamos la herramienta de pedidos y Claude para respuestas detalladas
)

# Tarea para la Crew de Dudas (Consultas de Cafés)
consulta_cafes_task = Task(
    description="Recomendar cafés basados en las preferencias del cliente.",
    expected_output="Lista de cafés recomendados con sus características.",
    agent=experto_en_cafes  # Asignamos el agente que maneja esta tarea
)

# Tarea para la Crew de SoportePedidos
consulta_pedidos_task = Task(
    description="Consultar y devolver el estado del pedido del cliente.",
    expected_output="Estado y detalles del pedido.",
    agent=soporte_pedidos  # Asignamos el agente que maneja esta tarea
)

# Definir la Crew para Dudas (Consultas de Cafés)
crew_cafes = Crew(
    agents=[experto_en_cafes],  # Agente(s) involucrado(s) en la crew
    tasks=[consulta_cafes_task],  # Tarea(s) específica(s) de la crew
    process=Process.sequential  # Tipo de proceso para ejecutar la tarea de forma secuencial
)

# Definir la Crew para Soporte de Pedidos
crew_pedidos = Crew(
    agents=[soporte_pedidos],  # Agente(s) involucrado(s) en la crew
    tasks=[consulta_pedidos_task],  # Tarea(s) específica(s) de la crew
    process=Process.sequential  # Tipo de proceso para ejecutar la tarea de forma secuencial
)

# Exportamos las crews para que puedan ser utilizadas en otros módulos (como la API)
