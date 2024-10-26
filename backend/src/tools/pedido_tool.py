from datetime import datetime
from src.utils import get_supabase_client  # Importamos el cliente de Supabase

class SupabasePedidoTool:
    def __init__(self):
        # Inicializamos el cliente de Supabase usando nuestra función de utils
        self.client = get_supabase_client()

    def check_order_status(self) -> str:
        """
        Consulta el estado del pedido con id=1 en la base de datos.
        
        :return: Una cadena con el estado del pedido y detalles adicionales.
        """
        # Realizamos una consulta en la base de datos para buscar el pedido con id=1
        response = self.client.from_("pedidos").select("*").eq("id", 1).execute()
        
        # Extraemos los datos de la respuesta (lista de pedidos)
        pedidos = response.data or []

        if not pedidos:
            return "Lo siento, no pude encontrar información sobre tu pedido en este momento."

        # Formateamos la respuesta con los detalles del pedido
        pedido = pedidos[0]
        cliente = pedido.get("cliente", "Cliente desconocido")
        cafe = pedido.get("cafe", "Café no especificado")
        cantidad = pedido.get("cantidad", "Cantidad no especificada")
        fecha_pedido = pedido.get("fecha_pedido", "Fecha desconocida")
        direccion_envio = pedido.get("direccion_envio", "Dirección no especificada")
        estado = pedido.get("estado", "Estado desconocido")
        localizador = pedido.get("localizador", "Localización no disponible")

        # Calcular los días desde la fecha del pedido
        try:
            fecha_pedido_dt = datetime.strptime(fecha_pedido, "%Y-%m-%d")
            dias_desde_pedido = (datetime.now() - fecha_pedido_dt).days
        except (ValueError, TypeError):
            dias_desde_pedido = None  # Si la fecha es inválida, no mostramos los días

        # Respuesta basada en la información disponible
        if estado.lower() == "en camino":
            return (
                f"Hola {cliente}, tu pedido de {cantidad} unidad(es) de café {cafe} está en camino. "
                f"Actualmente se encuentra en: {localizador}."
            )
        elif dias_desde_pedido is not None and dias_desde_pedido < 3:
            return (
                f"Hola {cliente}, tu pedido de {cantidad} unidad(es) de café {cafe} fue realizado hace "
                f"{dias_desde_pedido} día(s). Está en proceso de preparación y se enviará pronto a: {direccion_envio}."
            )
        else:
            return (
                f"Hola {cliente}, tu pedido de {cantidad} unidad(es) de café {cafe} está en estado: {estado}. "
                f"Para más detalles, la última actualización de ubicación fue: {localizador}."
            )
