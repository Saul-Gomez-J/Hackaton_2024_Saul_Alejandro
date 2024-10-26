from src.utils import get_supabase_client  # Importamos el cliente de Supabase

class SupabaseCafeTool:
    def __init__(self):
        # Inicializamos el cliente de Supabase usando nuestra función de utils
        self.client = get_supabase_client()

    def recommend_cafe(self, preferences: dict) -> str:
        """
        Recomienda cafés basados en las preferencias del cliente.
        
        :param preferences: Diccionario que contiene las preferencias del cliente, e.g.,
                            {"tipo_cafe": "Arábica", "nivel_tueste": "Medio"}
        :return: Una cadena con recomendaciones de cafés similares.
        """
        # Inicializamos la consulta base en la tabla `cafes`
        query = self.client.from_("cafes").select("*")
        
        # Agregamos filtros por similitud según las preferencias proporcionadas
        for field, value in preferences.items():
            if value:  # Solo agregamos el filtro si el valor no es None o vacío
                query = query.like(field, f"%{value}%")
        
        # Ejecutamos la consulta
        response = query.execute()
        cafes = response.data or []

        # Si no hay resultados para todas las preferencias, buscar cafés individualmente para cada preferencia
        if not cafes:
            individual_recommendations = []
            for field, value in preferences.items():
                if value:
                    # Intentamos encontrar cafés que coincidan con esta característica
                    sub_query = self.client.from_("cafes").select("*").like(field, f"%{value}%").limit(1)
                    sub_response = sub_query.execute()
                    sub_cafe = sub_response.data
                    if sub_cafe:
                        individual_recommendations.append(sub_cafe[0])  # Tomamos el primer resultado de cada subconsulta
            
            # Si encontramos recomendaciones individuales, las usamos
            if individual_recommendations:
                recommendations = [
                    f"{cafe.get('tipo_cafe', 'Tipo desconocido')} - {cafe.get('descripcion', 'Descripción no disponible')} "
                    f"(Procedencia: {cafe.get('procedencia', 'Desconocida')}, "
                    f"Sabor: {cafe.get('sabor', 'Desconocido')}, Nivel de tueste: {cafe.get('nivel_tueste', 'Desconocido')})"
                    for cafe in individual_recommendations
                ]
                return "No encontré cafés que cumplan con todas tus preferencias, pero aquí tienes algunas recomendaciones individuales: " + ", ".join(recommendations)
            else:
                return "Lo siento, no encontré recomendaciones basadas en esas preferencias."

        # Si encontramos cafés que cumplan con todas las preferencias, los usamos
        recommendations = [
            f"{cafe.get('tipo_cafe', 'Tipo desconocido')} - {cafe.get('descripcion', 'Descripción no disponible')} "
            f"(Procedencia: {cafe.get('procedencia', 'Desconocida')}, "
            f"Sabor: {cafe.get('sabor', 'Desconocido')}, Nivel de tueste: {cafe.get('nivel_tueste', 'Desconocido')})"
            for cafe in cafes
        ]
        return "Te recomiendo los siguientes cafés: " + ", ".join(recommendations)
