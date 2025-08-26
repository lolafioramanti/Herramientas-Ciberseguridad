from dataclasses import dataclass
from typing import List

@dataclass
class Tool:
    name: str
    description: str
    download_link: str
    info_link: str = ""

@dataclass
class ToolCategory:
    category: str
    tools: List[Tool]

tools_data: List[ToolCategory] = [
    ToolCategory(
        category="Acceso Remoto",
        tools=[
            Tool(
                name="TeamViewer",
                description="Herramienta para acceso remoto a equipos. Permite controlar computadoras desde cualquier ubicación.",
                download_link="https://www.teamviewer.com/latam/download/windows/",
                info_link="https://www.teamviewer.com/latam/"
            ),
            Tool(
                name="AnyDesk", 
                description="Software de escritorio remoto rápido y seguro para acceso a distancia.",
                download_link="https://anydesk.com/es/downloads/windows",
                info_link="https://anydesk.com/es"
            ),
            Tool(
                name="Chrome Remote Desktop",
                description="Acceso remoto gratuito a través del navegador Chrome.",
                download_link="https://remotedesktop.google.com/",
                info_link="https://chromewebstore.google.com/detail/chrome-remote-desktop/inomeogfingihgjfjlpeplalcfajhgai?hl=es&pli=1"
            ),
            Tool(
                name="OpenSSH",
                description="Paquete de herramientas para acceso remoto mediante SSH. Cifra todo el tráfico para evitar escuchas y secuestros de sesión.",
                download_link="https://www.openssh.com",
                info_link="https://www.openssh.com/manual.html"
            ),
            Tool(
                name="PuTTY",
                description="Cliente SSH y telnet para conexiones remotas seguras.",
                download_link="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html",
                info_link="https://www.chiark.greenend.org.uk/~sgtatham/putty"
            ),
            Tool(
                name="WireGuard",
                description="VPN moderno de código abierto, extremadamente simple y rápido, basado en criptografía avanzada. Está diseñado para ser más eficiente y liviano que IPsec u OpenVPN, y es multiplataforma (Windows, Linux, macOS, BSD, iOS, Android)",
                download_link="https://www.wireguard.com/install",
                info_link="https://www.wireguard.com/"
            ),
            Tool(
                name="OpenVPN",
                description="solución VPN libre que permite crear redes privadas virtuales seguras. Ofrece conectividad punto a punto cifrada con SSL/TLS y autenticación de usuarios/hosts.",
                download_link="https://openvpn.net/client",
                info_link="https://openvpn.net/"
            )
        ]
    ),
    ToolCategory(
        category="Antirrobo",
        tools=[
            Tool(
                name="Prey Anti Theft",
                description="Sistema de seguimiento y recuperación para dispositivos robados o perdidos.",
                download_link="https://preyproject.com/download",
                info_link="https://preyproject.com/resources"
            )
        ]
    ),
    ToolCategory(
        category="Firewall",
        tools=[
            Tool(
                name="Windows Defender Firewall Placeholder",
                description="Firewall integrado de Windows para protección de red básica.",
                download_link="#",
                info_link="https://support.microsoft.com/es-es/windows/firewall-y-protección-de-red-en-la-aplicación-seguridad-de-windows-ec0844f7-aebd-0583-67fe-601ecf5d774f"
            ),
            Tool(
                name="ZoneAlarm",
                description="Firewall avanzado con protección bidireccional y control de aplicaciones.",
                download_link="https://www.zonealarm.com/es/software/free-firewall",
                info_link="https://www.zonealarm.com/es/software/free-firewall"
            ),
            Tool(
                name="Comodo Firewall Placeholder",
                description="Firewall gratuito con tecnología de sandboxing y protección proactiva.",
                download_link="https://www.comodo.com/antivirus-internet-security/#firewall",
                info_link="https://www.comodo.com"
            ),
            Tool(
                name="pfSense",
                description="Firewall/router de código abierto basado en FreeBSD. Ofrece funcionalidades avanzadas (firewall stateful, VPN IPsec/OpenVPN, balanceo de carga, UTM, IDS/IPS, portal cautivo, etc.) con interfaz web amigable",
                download_link="https://www.pfsense.org/download",
                info_link="https://www.pfsense.org"
            ),
            Tool(
                name="OPNsense",
                description="Firewall y plataforma de enrutamiento de código abierto basada en FreeBSD. Ofrece características avanzadas como firewall stateful, VPN IPsec/OpenVPN, balanceo de carga, UTM, IDS/IPS, portal cautivo, y más, todo accesible a través de una interfaz web intuitiva.",
                download_link="https://opnsense.org/download/",
                info_link="https://docs.opnsense.org"
            ),
            Tool(
                name="IPFire",
                description="Distribución Linux especializada en firewall de código abierto. Ofrece inspección de paquetes, gestión por consola web fácil de usar, y soporte para VPN, proxy, y antivirus integrado", 
                download_link="https://www.ipfire.org/downloads/ipfire-2.29-core196",
                info_link="https://www.ipfire.org"
            )
        ]
    ),
    ToolCategory(
        category="Análisis de red",
        tools=[
            Tool(
                name="Wireshark",
                description="Analizador de protocolos de red open source. Captura paquetes y permite examinar en detalle el tráfico de red, ideal para diagnóstico y seguridad (requiere interfaz gráfica).",
                download_link="https://www.wireshark.org/download.html",
                info_link="https://www.wireshark.org"
            ),
            Tool(
                name="Nmap",
                description="Escáner de redes y auditoría de seguridad de código abierto. Permite descubrir hosts, servicios activos, identificar sistemas operativos y vulnerabilidades básicas. Incluye la GUI Zenmap.",
                download_link="https://nmap.org/download.html",
                info_link="https://nmap.org"
            ),
            Tool(
                name="Zenmap",
                description="Interfaz gráfica oficial de Nmap, gratuita y open source. Facilita la ejecución de escaneos, permite guardar resultados y crear perfiles de análisis.",
                download_link="https://nmap.org/zenmap",
                info_link="https://nmap.org"
            ),
            Tool(
                name="Kismet",
                description="Detector y sniffer inalámbrico open source. Soporta Wi-Fi, Bluetooth, Zigbee y RF, usado en auditorías y mapeo de redes inalámbricas.",
                download_link="https://www.kismetwireless.net/download",
                info_link="https://www.kismetwireless.net"
            )
        ]
    ),
    ToolCategory(
        category="Escáneres de vulnerabilidades",
        tools=[
            Tool(
                name="OpenVAS (Greenbone)",
                description="Escáner de vulnerabilidades de red open source. Realiza pruebas autenticadas y no autenticadas a gran escala, con actualizaciones diarias de su base de datos.",
                download_link="https://github.com/greenbone",
                info_link="https://www.openvas.org"
            ),
            Tool(
                name="Nikto",
                description="Escáner de vulnerabilidades para servidores web. Busca archivos sensibles, configuraciones erróneas, scripts vulnerables y software desactualizado.",
                download_link="https://cirt.net/Nikto2",
                info_link="https://cirt.net/Nikto2"
            ),
            Tool(
                name="Lynis",
                description="Herramienta de auditoría de seguridad para sistemas *nix. Escanea configuraciones débiles, parches faltantes y cumplimiento de buenas prácticas.",
                download_link="https://cisofy.com/download/lynis/",
                info_link="https://cisofy.com/lynis/"
            )
        ]
    ),
    ToolCategory(
        category="Antivirus",
        tools=[
            Tool(
                name="ClamAV",
                description="Antivirus open source multiplataforma. Utiliza detección por firmas actualizadas diariamente, ideal para servidores, correo y análisis forense.",
                download_link="https://www.clamav.net/downloads",
                info_link="https://www.clamav.net"
            )
        ]
    ),

    ToolCategory(
        category="Gestión de contraseñas",
        tools=[
            Tool(
                name="KeePassXC",
                description="Gestor de contraseñas multiplataforma open source. Almacena credenciales cifradas en un archivo local, con generador de contraseñas y autocompletado.",
                download_link="https://keepassxc.org/download/",
                info_link="https://keepassxc.org"
            ),
            Tool(
                name="Bitwarden",
                description="Gestor de contraseñas de código abierto con almacenamiento cifrado en la nube. Permite sincronizar dispositivos, autenticación 2FA y funciones colaborativas.",
                download_link="https://bitwarden.com/download/",
                info_link="https://bitwarden.com"
            )
        ]
    ),

    ToolCategory(
        category="Cifrado de archivos",
        tools=[
            Tool(
                name="VeraCrypt",
                description="Software de cifrado gratuito y open source. Permite cifrar discos completos, particiones o crear contenedores cifrados con algoritmos robustos.",
                download_link="https://www.veracrypt.fr/en/Downloads.html",
                info_link="https://www.veracrypt.fr"
            ),
            Tool(
                name="GnuPG (GPG)",
                description="Implementación libre del estándar OpenPGP. Permite cifrar y firmar archivos y comunicaciones de forma segura, disponible en CLI y frontends.",
                download_link="https://gnupg.org/download/",
                info_link="https://gnupg.org"
            )
        ]
    ),
    ToolCategory(
        category="Herramientas forenses",
        tools=[
            Tool(
                name="Autopsy",
                description="Plataforma forense digital con GUI. Permite analizar discos duros y recuperar evidencias como archivos borrados, emails e índices.",
                download_link="https://www.autopsy.com/download/",
                info_link="https://www.autopsy.com"
            ),
            Tool(
                name="The Sleuth Kit (TSK)",
                description="Librería y utilidades CLI para análisis forense de sistemas de archivos. Permite examinar discos e imágenes de disco y recuperar metadatos.",
                download_link="https://www.sleuthkit.org/sleuthkit/download.php",
                info_link="https://www.sleuthkit.org/sleuthkit"
            ),
            Tool(
                name="Volatility",
                description="Framework de análisis forense de memoria RAM. Detecta procesos, conexiones, ventanas y artefactos en dumps de memoria.",
                download_link="https://www.volatilityfoundation.org/releases",
                info_link="https://www.volatilityfoundation.org"
            )
        ]
    ),
    ToolCategory(
        category="Monitoreo de sistemas",
        tools=[
            Tool(
                name="Nagios Core",
                description="Plataforma clásica de monitoreo de infraestructura IT open source. Vigila servidores, aplicaciones y redes con alertas configurables.",
                download_link="https://www.nagios.org/downloads/",
                info_link="https://www.nagios.org"
            ),
            Tool(
                name="Zabbix",
                description="Plataforma empresarial de monitoreo de red y sistemas. Escalable, de bajo consumo y con alertas en tiempo real, todo open source.",
                download_link="https://www.zabbix.com/download",
                info_link="https://www.zabbix.com"
            ),
            Tool(
                name="Prometheus",
                description="Sistema open source de monitoreo de métricas y base de datos de series temporales. Ideal para entornos cloud y contenedores.",
                download_link="https://prometheus.io/download/",
                info_link="https://prometheus.io"
            )
        ]
    )
]