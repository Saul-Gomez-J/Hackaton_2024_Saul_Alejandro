from src.utils import get_supabase_client  # Importamos el cliente de Supabase

class SupabaseCafeTool:
    def __init__(self):
        self.client = get_supabase_client()
        self.name = "SupabaseCafeTool"
        self.description = "Recomienda cafés basados en las preferencias proporcionadas por el cliente."
        self.model_fields = {
            "preferences": "Un diccionario que contiene las preferencias del cliente (tipo_cafe, nivel_tueste, sabor, etc.)."
        }

    def recommend_cafe(self, preferences: dict) -> str:
        """
        Recomienda cafés basados en las preferencias del cliente.
        
        :param preferences: Diccionario que contiene las preferencias del cliente, e.g.,
                            {"tipo_cafe": "Arábica", "nivel_tueste": "Medio"}
        :return: Una cadena con recomendaciones de cafés similares o alternativas.
        """
        # Inicializamos la consulta base en la tabla `cafes`
        query = self.client.from_("cafes").select("*")
        
        # Agregamos filtros por similitud según las preferencias proporcionadas
        for field, value in preferences.items():
            if value:  # Solo agregamos el filtro si el valor no es None o vacío
                query = query.like(field, f"%{value}%")

        # Ejecutamos la consulta principal
        response = query.execute()
        cafes = response.data or []

        # Si hay coincidencias exactas, devolvemos esas recomendaciones
        if cafes:
            recommendations = "\n\n".join(
                f"**{cafe.get('tipo_cafe', 'Tipo desconocido')}**:\n"
                f"- Descripción: {cafe.get('descripcion', 'Descripción no disponible')}\n"
                f"- Procedencia: {cafe.get('procedencia', 'Desconocida')}\n"
                f"- Sabor: {cafe.get('sabor', 'Desconocido')}\n"
                f"- Nivel de tueste: {cafe.get('nivel_tueste', 'Desconocido')}\n"
                f"- Cuerpo: {cafe.get('cuerpo', 'Desconocido')}\n"
                f"- Acidez: {cafe.get('acidez', 'Desconocido')}\n"
                f"- Recomendaciones de preparación: {cafe.get('recomendaciones_preparacion', 'No disponible')}"
                for cafe in cafes
            )
            return "Te recomiendo los siguientes cafés:\n\n" + recommendations

        # Si no hay coincidencias exactas, buscamos recomendaciones alternativas basadas en parámetros individuales
        else:
            individual_recommendations = []
            for field, value in preferences.items():
                if value:
                    # Intentamos encontrar cafés que coincidan con esta característica individual
                    sub_query = self.client.from_("cafes").select("*").like(field, f"%{value}%").limit(2)
                    sub_response = sub_query.execute()
                    sub_cafes = sub_response.data or []
                    
                    # Añadimos cada resultado individualmente si aún no está en las recomendaciones
                    for sub_cafe in sub_cafes:
                        if sub_cafe not in individual_recommendations:
                            individual_recommendations.append(sub_cafe)

            # Si encontramos recomendaciones alternativas, las formateamos y las presentamos
            if individual_recommendations:
                recommendations = "\n\n".join(
                    f"**{cafe.get('tipo_cafe', 'Tipo desconocido')}**:\n"
                    f"- Descripción: {cafe.get('descripcion', 'Descripción no disponible')}\n"
                    f"- Procedencia: {cafe.get('procedencia', 'Desconocida')}\n"
                    f"- Sabor: {cafe.get('sabor', 'Desconocido')}\n"
                    f"- Nivel de tueste: {cafe.get('nivel_tueste', 'Desconocido')}\n"
                    f"- Cuerpo: {cafe.get('cuerpo', 'Desconocido')}\n"
                    f"- Acidez: {cafe.get('acidez', 'Desconocido')}\n"
                    f"- Recomendaciones de preparación: {cafe.get('recomendaciones_preparacion', 'No disponible')}"
                    for cafe in individual_recommendations
                )
                return "No encontré cafés que cumplan con todas tus preferencias exactas, pero aquí tienes algunas alternativas basadas en tus parámetros individuales:\n\n" + recommendations
            else:
                return "Lo siento, no encontré recomendaciones basadas en esas preferencias."

