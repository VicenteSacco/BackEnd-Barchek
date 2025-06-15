# api/services.py
import openai
import base64
import os
import json

# Inicialización del Cliente de OpenAI (desde variables de entorno)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada.")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def calcular_volumenes(fraccion: float, capacidad_total_ml: float = 750.0) -> dict:
    """
    Calcula los volúmenes en ml y oz a partir de una fracción de la capacidad total.
    """
    if not (0.05 <= fraccion <= 0.95):
        raise ValueError("La fracción debe estar entre 0.05 y 0.95")
    volumen_ml = fraccion * capacidad_total_ml
    volumen_oz = volumen_ml / 29.5735
    return {
        "fraccion": round(fraccion, 2),
        "volumen_fl_oz": round(volumen_oz, 2),
        "volumen_ml": round(volumen_ml, 2)
    }

def process_image_for_liquid_estimation(base64_image_data: str, drink_id: int):
    """
    Procesa una imagen para estimar la fracción de líquido utilizando GPT-4o.
    Devuelve la fracción predicha y volúmenes calculados.

    Levanta excepciones para errores específicos.
    """
    try:
        # Asegúrate de que la cadena Base64 que recibes no tenga el prefijo
        if ',' in base64_image_data:
            base64_image_data = base64_image_data.split(',')[1]

        print(f"Enviando imagen a GPT-4o para análisis para drinkId: {drink_id}...")

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
                    - No incluyas explicaciones ni texto adicional fuera del JSON.
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
                                "detail": "low"
                            }
                        }
                    ]
                }
            ],
            temperature=0.2,
            max_tokens=40
        )

        respuesta_json = json.loads(response.choices[0].message.content)
        fraccion = float(respuesta_json.get("fraccion")) # Usar .get para evitar KeyError

        if fraccion is None or not (0.05 <= fraccion <= 0.95):
            raise ValueError("La fracción predicha es nula o está fuera del rango válido (0.05-0.95).")

        resultado_final = calcular_volumenes(fraccion)
        return resultado_final

    except openai.APIError as e:
        # Captura errores específicos de OpenAI y los relanza como un error más genérico
        raise Exception(f"Error de la API de OpenAI: {e.response.status_code} - {e.response.text}")
    except json.JSONDecodeError:
        raise Exception("No se pudo decodificar el JSON de la respuesta del modelo.")
    except ValueError as e:
        # Re-lanza los errores de validación de `calcular_volumenes` o la fracción
        raise e
    except Exception as e:
        # Captura cualquier otro error inesperado
        raise Exception(f"Error inesperado al procesar la imagen con IA: {e}")