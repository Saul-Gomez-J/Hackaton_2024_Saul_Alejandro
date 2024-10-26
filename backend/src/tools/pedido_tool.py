from src.utils import get_supabase_client  # Importamos el cliente de Supabase

class SupabasePedidoTool:
    def __init__(self):
        self.client = get_supabase_client()
        self.name = "SupabasePedidoTool"
        self.description = "Consulta el estado de un pedido específico en la base de datos."
        self.model_fields = {
            "order_id": "ID del pedido que se desea consultar (en este caso, siempre será 1)."
        }

    def check_order_status(self) -> str:
        # Resto del código...

        response = self.client.from_("pedidos").select("*").eq("id", 1).execute()
        pedidos = response.data or []

        if not pedidos:
            return "Lo siento, no pude encontrar información sobre tu pedido en este momento."

        pedido = pedidos[0]
        cliente = pedido.get("cliente", "Cliente desconocido")
        cafe = pedido.get("cafe", "Café no especificado")
        cantidad = pedido.get("cantidad", "Cantidad no especificada")
        fecha_pedido = pedido.get("fecha_pedido", "Fecha desconocida")
        direccion_envio = pedido.get("direccion_envio", "Dirección no especificada")
        estado = pedido.get("estado", "Estado desconocido")
        localizador = pedido.get("localizador", "Localización no disponible")

        return (
            f"Hola {cliente}, tu pedido de {cantidad} unidad(es) de café {cafe} está en estado: {estado}. "
            f"Para más detalles, la última actualización de ubicación fue: {localizador}."
        )
