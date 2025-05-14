import obspython as obs
from datetime import datetime

# Nombre de la fuente de texto en OBS
source_name = "hora"

# Intervalo de actualización (en milisegundos)
update_interval = 1000  # 1 segundo

def update_text():
    # Obtener la hora y fecha actuales
    now = datetime.now()
    hora_actual = now.strftime("%H:%M:%S")
    fecha_actual = now.strftime("%d/%m/%Y")
    texto = f"{hora_actual} - {fecha_actual}"

    # Buscar la fuente y actualizar el texto
    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", texto)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)

def script_update(settings):
    # Reinicia el temporizador en cada cambio
    obs.timer_remove(update_text)
    obs.timer_add(update_text, update_interval)

def script_load(settings):
    # Al cargar el script, comienza a actualizar
    obs.timer_add(update_text, update_interval)
