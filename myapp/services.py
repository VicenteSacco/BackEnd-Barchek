import openai
import base64
import os
import json

# --- Excepción Personalizada ---
# Crear una excepción personalizada hace que el manejo de errores sea más específico.
class OpenAI_APIError(Exception):
    """Excepción personalizada para errores relacionados con la API de OpenAI."""
    pass

# --- CONFIGURACIÓN IMPORTANTE ---
# Asegúrate de haber configurado tu clave de API de OpenAI como una variable de entorno.
# En tu terminal, antes de iniciar Django, puedes usar:
# export OPENAI_API_KEY='tu_clave_secreta_aqui' (en Linux/Mac)
# set OPENAI_API_KEY=tu_clave_secreta_aqui (en Windows)
try:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except openai.OpenAIError as e:
    raise ValueError("La clave de API de OpenAI no está configurada o es inválida. Asegúrate de exportar la variable de entorno OPENAI_API_KEY.")

def calcular_volumenes(fraccion: float, capacidad_total_ml: float = 750.0) -> dict:
    """
    Calcula los volúmenes en ml y oz a partir de una fracción de la capacidad total.
    """
    if not (0.05 <= fraccion <= 0.95):
        raise ValueError(f"La fracción '{fraccion}' está fuera del rango válido (0.05-0.95).")
    
    volumen_ml = fraccion * capacidad_total_ml
    volumen_oz = volumen_ml / 29.5735
    return {
        "fraccion": round(fraccion, 2),
        "volumen_fl_oz": round(volumen_oz, 2),
        "volumen_ml": round(volumen_ml, 2)
    }

def process_image_for_liquid_estimation(base64_image_data: str, drink_id: int | None = None) -> dict:
    """
    Procesa una imagen en base64 para estimar la fracción de líquido restante usando GPT-4o.
    ``drink_id`` se incluye por compatibilidad con el frontend aunque no se utilice
    actualmente.  Devuelve la fracción predicha y los volúmenes calculados.
    """
    try:
        # Algunas librerías añaden un prefijo al dato base64 (por ejemplo
        # ``data:image/jpeg;base64,``). Si está presente lo removemos para
        # evitar errores.
        if ',' in base64_image_data:
            base64_image_data = base64_image_data.split(',')[1]

        # Validamos que realmente sea una cadena en Base64
        try:
            base64.b64decode(base64_image_data, validate=True)
        except Exception:
            raise ValueError("La imagen enviada no es una cadena Base64 válida.")

        # Envía la solicitud a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": """
                    Eres un analizador visual experto en botellas de licor. Tu tarea es estimar visualmente la fracción de líquido que contiene una botella en una imagen.
                    - Tu estimación debe ser un número decimal entre 0.05 y 0.95.
                    - Devuelve exclusivamente un objeto JSON con el formato: {"fraccion": 0.XX}
                    - No incluyas explicaciones ni texto adicional fuera del JSON. Si no puedes determinar la fracción, devuelve {"fraccion": 0.0}.
                    """
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analiza la imagen de esta botella y estima la fracción de líquido restante."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image_data}",
                                "detail": "low" # Usamos 'low' para un análisis más rápido y económico
                            }
                        }
                    ]
                }
            ],
            temperature=0.1, # Usamos baja temperatura para respuestas más consistentes
            max_tokens=50
        )

        # Procesa la respuesta de la IA
        respuesta_json = json.loads(response.choices[0].message.content)
        fraccion = float(respuesta_json.get("fraccion", 0.0))

        if fraccion == 0.0:
             raise ValueError("El modelo no pudo determinar la fracción de la botella.")

        # Calcula los volúmenes y devuelve el resultado final
        return calcular_volumenes(fraccion)

    except openai.APIError as e:
        # Usamos la excepción personalizada para dar más contexto al error.
        raise OpenAI_APIError(f"Error de la API de OpenAI: {e.code} - {e.message}")
    except (json.JSONDecodeError, KeyError):
        # Maneja el caso en que la IA devuelve un formato de JSON incorrecto
        raise Exception("La respuesta del modelo de IA no tuvo el formato JSON esperado.")
    except ValueError as e:
        # Re-lanza los errores de validación de `calcular_volumenes`
        raise e
    except Exception as e:
        # Captura cualquier otro error inesperado
        raise Exception(f"Error inesperado al procesar la imagen con IA: {e}")
