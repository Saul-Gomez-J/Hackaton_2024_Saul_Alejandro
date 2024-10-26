from crewai import Agent, Task, Crew, Process
from src.tools.cafe_tool import SupabaseCafeTool
from src.tools.pedido_tool import SupabasePedidoTool
from src.tools.gpt4o_tool import GPT4oTool
from src.tools.claude_tool import ClaudeTool

# Crear instancias de las herramientas
cafe_tool = SupabaseCafeTool()
pedido_tool = SupabasePedidoTool()
gpt4o_tool = GPT4oTool()
claude_tool = ClaudeTool()

# Agente Experto en Cafés con memoria
experto_en_cafes = Agent(
    role="Experto en Cafés",
    goal="Recomendar cafés según las preferencias del cliente.",
    backstory="Especialista en cafés de la tienda, con conocimientos detallados en perfiles de sabor y variedades.",
    tools=[cafe_tool, gpt4o_tool]  # Herramientas asignadas
)


# Agente de Soporte de Pedidos
soporte_pedidos = Agent(
    role="Soporte de Pedidos",
    goal="Resolver dudas sobre el estado de pedidos realizados.",
    backstory="Especialista en seguimiento de pedidos y soporte al cliente.",
    tools=[pedido_tool, claude_tool]  # Herramientas asignadas para consultas de pedidos
)
