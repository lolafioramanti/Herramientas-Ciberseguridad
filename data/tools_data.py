from dataclasses import dataclass
from typing import List

@dataclass
class Tool:
    name: str
    description: str
    download_link: str

@dataclass
class ToolCategory:
    category: str
    tools: List[Tool]

tools_data: List[ToolCategory] = [
    ToolCategory(
        category="Acceso Remoto",
        tools=[
            Tool(
                name="TeamViewer Placeholder",
                description="Herramienta para acceso remoto a equipos. Permite controlar computadoras desde cualquier ubicación.",
                download_link="#"
            ),
            Tool(
                name="AnyDesk Placeholder", 
                description="Software de escritorio remoto rápido y seguro para acceso a distancia.",
                download_link="#"
            ),
            Tool(
                name="Chrome Remote Desktop Placeholder",
                description="Acceso remoto gratuito a través del navegador Chrome.",
                download_link="#"
            )
        ]
    ),
    ToolCategory(
        category="Antirrobo",
        tools=[
            Tool(
                name="Prey Anti Theft Placeholder",
                description="Sistema de seguimiento y recuperación para dispositivos robados o perdidos.",
                download_link="#"
            ),
            Tool(
                name="LoJack Placeholder",
                description="Software de seguridad para protección contra robo de laptops y dispositivos.",
                download_link="#"
            ),
            Tool(
                name="Find My Device Placeholder",
                description="Herramienta nativa para localizar dispositivos perdidos o robados.",
                download_link="#"
            )
        ]
    ),
    ToolCategory(
        category="Firewall",
        tools=[
            Tool(
                name="Windows Defender Firewall Placeholder",
                description="Firewall integrado de Windows para protección de red básica.",
                download_link="#"
            ),
            Tool(
                name="ZoneAlarm Placeholder",
                description="Firewall avanzado con protección bidireccional y control de aplicaciones.",
                download_link="#"
            ),
            Tool(
                name="Comodo Firewall Placeholder",
                description="Firewall gratuito con tecnología de sandboxing y protección proactiva.",
                download_link="#"
            )
        ]
    ),
    ToolCategory(
        category="Análisis de Red",
        tools=[
            Tool(
                name="Wireshark Placeholder",
                description="Analizador de protocolos de red para captura y análisis de tráfico.",
                download_link="#"
            ),
            Tool(
                name="Nmap Placeholder",
                description="Escáner de red para descubrimiento de hosts y servicios.",
                download_link="#"
            ),
            Tool(
                name="Netstat Placeholder",
                description="Herramienta de línea de comandos para mostrar conexiones de red activas.",
                download_link="#"
            )
        ]
    ),
    ToolCategory(
        category="Seguridad",
        tools=[
            Tool(
                name="Malwarebytes Placeholder",
                description="Software anti-malware para detección y eliminación de amenazas.",
                download_link="#"
            ),
            Tool(
                name="Bitdefender Placeholder",
                description="Suite de seguridad completa con antivirus y protección en tiempo real.",
                download_link="#"
            ),
            Tool(
                name="KeePass Placeholder",
                description="Gestor de contraseñas seguro y gratuito para almacenar credenciales.",
                download_link="#"
            )
        ]
    ),
    ToolCategory(
        category="Monitoreo del Sistema",
        tools=[
            Tool(
                name="Process Monitor Placeholder",
                description="Herramienta avanzada para monitorear actividad del sistema de archivos y registro.",
                download_link="#"
            ),
            Tool(
                name="Task Manager Plus Placeholder",
                description="Administrador de tareas mejorado con información detallada de procesos.",
                download_link="#"
            ),
            Tool(
                name="System Information Placeholder",
                description="Utilidad para obtener información detallada del hardware y software del sistema.",
                download_link="#"
            )
        ]
    )
]
