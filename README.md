# Baúl de Herramientas de Ciberseguridad

Una aplicación Streamlit para organizar herramientas de seguridad y administración de sistemas por categorías.

## Características

- **Organización por categorías**: Herramientas organizadas en pestañas por tipo (Acceso Remoto, Antirrobo, Firewall, etc.)
- **Documentación y links de descarga**: Acceso a documentación pública de herramientas y fácil obtención de las mismas.
- **Estadísticas**: Vista general del número de herramientas y categorías.

## Personalización

### Agregar nuevas herramientas

1. **Edita el archivo `data/tools_data.py`**
2. **Para agregar una herramienta a una categoría existente:**
   ```python
   Tool(
       name="Nombre de la Herramienta",
       description="Descripción detallada de qué hace la herramienta.",
       download_link="https://ejemplo.com/descarga"
   )
   ```

3. **Para crear una nueva categoría:**
   ```python
   ToolCategory(
       category="Nueva Categoría",
       tools=[
           Tool(
               name="Primera Herramienta",
               description="Descripción de la herramienta.",
               download_link="https://ejemplo.com/descarga"
           )
       ]
   )
   ```

### Categorías iniciales

- **Acceso Remoto**: TeamViewer, AnyDesk, Chrome Remote Desktop
- **Antirrobo**: Prey Anti Theft, LoJack, Find My Device
- **Firewall**: Windows Defender, ZoneAlarm, Comodo Firewall
- **Análisis de Red**: Wireshark, Nmap, Netstat
- **Seguridad**: Malwarebytes, Bitdefender, KeePass
- **Monitoreo del Sistema**: Process Monitor, Task Manager Plus, System Information



