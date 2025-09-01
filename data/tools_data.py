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
                description="Plataforma de acceso remoto ampliamente utilizada para asistencia técnica y colaboración en línea. Permite controlar computadoras y servidores a través de Internet de manera segura mediante ID y contraseña únicos. Se emplea mucho en soporte técnico y trabajo remoto, ofreciendo funciones como transferencia de archivos, chat, videollamadas y multisesión.",
                download_link="https://www.teamviewer.com/latam/download/windows/",
                info_link="https://www.teamviewer.com/latam/"
            ),
            Tool(
                name="AnyDesk", 
                description="Software de escritorio remoto similar a TeamViewer, pero enfocado en un rendimiento más liviano y rápido gracias a su protocolo DeskRT, que optimiza la compresión de datos y la latencia. Es muy usado en soporte remoto en empresas y en usuarios individuales que buscan un acceso remoto estable incluso en conexiones de baja velocidad.",
                download_link="https://anydesk.com/es/downloads/windows",
                info_link="https://anydesk.com/es"
            ),
            Tool(
                name="Chrome Remote Desktop",
                description="Extensión gratuita de Google que permite acceder de forma remota a una computadora desde el navegador Chrome o una app móvil. Su mayor ventaja es la simplicidad, ya que no requiere configuraciones complicadas ni software adicional más allá de Chrome. Se usa sobre todo en entornos domésticos o pequeñas empresas.",
                download_link="https://remotedesktop.google.com/",
                info_link="https://chromewebstore.google.com/detail/chrome-remote-desktop/inomeogfingihgjfjlpeplalcfajhgai?hl=es&pli=1"
            ),
            Tool(
                name="OpenSSH",
                description="Conjunto de utilidades de red basadas en el protocolo SSH (Secure Shell), utilizado para conectarse de manera segura a sistemas remotos a través de una terminal encriptada. Incluye herramientas como scp y sftp para transferir archivos de forma segura. Es un estándar en servidores Linux y Unix para administración remota.",
                download_link="https://www.openssh.com",
                info_link="https://www.openssh.com/manual.html"
            ),
            Tool(
                name="PuTTY",
                description="Cliente SSH y Telnet para Windows muy popular y liviano. Permite conectarse a servidores Linux/Unix desde Windows sin necesidad de instalar suites completas como OpenSSH. También soporta protocolos como serial, raw y rlogin. Suele usarse en redes pequeñas o en entornos educativos para prácticas de administración de sistemas.",
                download_link="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html",
                info_link="https://www.chiark.greenend.org.uk/~sgtatham/putty"
            ),
            Tool(
                name="WireGuard",
                description="Protocolo VPN moderno y minimalista que se caracteriza por su rapidez, simplicidad en la configuración y alto nivel de seguridad. Está integrado en el kernel de Linux y se considera más eficiente que opciones tradicionales como OpenVPN o IPSec. Ideal para proteger comunicaciones en redes corporativas y conexiones móviles.",
                download_link="https://www.wireguard.com/install",
                info_link="https://www.wireguard.com/"
            ),
            Tool(
                name="OpenVPN",
                description="Software VPN muy extendido que utiliza SSL/TLS para establecer túneles seguros entre dispositivos. Es altamente configurable, multiplataforma y soporta tanto acceso remoto como conexiones punto a punto o sitio a sitio. Es una de las soluciones más utilizadas por empresas para garantizar acceso seguro a redes internas desde Internet.",
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
                description="Aplicación multiplataforma para rastrear y proteger dispositivos en caso de robo o pérdida. Permite geolocalizar equipos, tomar capturas de pantalla, activar alarmas sonoras y bloquear el dispositivo de forma remota. Es usado tanto en entornos personales como empresariales para resguardar laptops y móviles.",
                download_link="https://preyproject.com/download",
                info_link="https://preyproject.com/resources"
            ),
        ]
    ),
    ToolCategory(
        category="Firewall",
        tools=[
            Tool(
                name="Windows Defender Firewall Placeholder",
                description="Firewall integrado en Windows que monitorea y controla el tráfico entrante y saliente en el sistema operativo. Funciona en conjunto con Microsoft Defender Antivirus y ofrece una protección básica contra accesos no autorizados y malware que intente comunicarse con Internet.",
                download_link="#",
                info_link="https://support.microsoft.com/es-es/windows/firewall-y-protección-de-red-en-la-aplicación-seguridad-de-windows-ec0844f7-aebd-0583-67fe-601ecf5d774f"
            ),
            Tool(
                name="ZoneAlarm",
                description="Firewall y suite de seguridad desarrollada por Check Point. Proporciona control detallado sobre el tráfico de red, protección contra intrusiones y funciones adicionales como protección de identidad y sandboxing de aplicaciones sospechosas. Fue uno de los firewalls personales más conocidos en entornos domésticos.",
                download_link="https://www.zonealarm.com/es/software/free-firewall",
                info_link="https://www.zonealarm.com/es/software/free-firewall"
            ),
            Tool(
                name="Comodo Firewall Placeholder",
                description="Parte de la suite de seguridad de Comodo, ofrece un firewall avanzado con características como prevención de intrusiones, modo default deny para bloquear aplicaciones desconocidas, y sandbox automático. Es muy usado por usuarios avanzados que buscan más control sobre el tráfico que el firewall de Windows.",
                download_link="https://www.comodo.com/antivirus-internet-security/#firewall",
                info_link="https://www.comodo.com"
            ),
            Tool(
                name="pfSense",
                description="Sistema operativo basado en FreeBSD que convierte una PC en un firewall/router avanzado. Se administra mediante interfaz web y soporta funciones como VPNs, balanceo de carga, detección de intrusiones y filtrado detallado. Es muy popular en redes corporativas y educativas por ser open source y muy robusto.",
                download_link="https://www.pfsense.org/download",
                info_link="https://www.pfsense.org"
            ),
            Tool(
                name="OPNsense",
                description="Derivado de pfSense, con una interfaz gráfica más moderna y actualizaciones frecuentes. Mantiene las funciones de firewall y router avanzado, con énfasis en usabilidad, plugins y seguridad. Se utiliza en entornos profesionales y domésticos que buscan una alternativa libre y confiable para proteger redes.",
                download_link="https://opnsense.org/download/",
                info_link="https://docs.opnsense.org"
            ),
            Tool(
                name="IPFire",
                description="Distribución Linux enfocada en seguridad de red, que funciona como firewall, proxy y sistema de detección de intrusiones. Destaca por su sistema modular de colores (zonas de red) que simplifica la gestión de reglas de seguridad. Es fácil de usar en redes pequeñas y medianas.", 
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
                description="Analizador de protocolos de red que permite capturar y examinar paquetes en tiempo real. Es una de las herramientas más usadas en auditorías de seguridad, resolución de problemas de red y aprendizaje de protocolos. Su interfaz gráfica permite filtrar y analizar tráfico de forma muy detallada.",
                download_link="https://www.wireshark.org/download.html",
                info_link="https://www.wireshark.org"
            ),
            Tool(
                name="Nmap",
                description="Herramienta de escaneo de red muy potente que identifica dispositivos, puertos abiertos, servicios y posibles vulnerabilidades. Es ampliamente utilizada por administradores de sistemas y especialistas en ciberseguridad para mapear redes y realizar auditorías de seguridad.",
                download_link="https://nmap.org/download.html",
                info_link="https://nmap.org"
            ),
            Tool(
                name="Zenmap",
                description="Interfaz gráfica oficial de Nmap. Facilita la creación y ejecución de escaneos para usuarios que prefieren evitar la línea de comandos. Incluye perfiles de escaneo preconfigurados y visualización gráfica de topologías de red.",
                download_link="https://nmap.org/zenmap",
                info_link="https://nmap.org"
            ),
            Tool(
                name="Kismet",
                description="Herramienta de monitoreo de redes inalámbricas. Detecta redes WiFi y dispositivos cercanos, incluso redes ocultas o no anunciadas. Es usada en auditorías de seguridad WiFi, wardriving y pruebas de penetración en redes inalámbricas.",
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
                description="Plataforma de análisis de vulnerabilidades open source que escanea sistemas en busca de configuraciones inseguras, software desactualizado y servicios vulnerables. Es una alternativa libre a soluciones comerciales como Nessus, usada en pruebas de seguridad en entornos corporativos.",
                download_link="https://github.com/greenbone",
                info_link="https://www.openvas.org"
            ),
            Tool(
                name="Nikto",
                description="Escáner web de código abierto que analiza servidores web en busca de vulnerabilidades comunes, configuraciones débiles y software obsoleto. Es útil en pruebas de penetración para detectar problemas iniciales en aplicaciones y servidores web.",
                download_link="https://cirt.net/Nikto2",
                info_link="https://cirt.net/Nikto2"
            ),
            Tool(
                name="Lynis",
                description="Herramienta de auditoría de seguridad para sistemas Linux y Unix. Revisa configuraciones, parches, permisos, servicios y aplicaciones instaladas para recomendar mejoras de seguridad y cumplimiento. Es utilizada en hardening de servidores.",
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
                description="Antivirus open source diseñado especialmente para servidores Linux y correo electrónico. Detecta malware, troyanos y archivos infectados en sistemas de producción. Suele usarse como motor de detección en gateways de correo electrónico y soluciones de seguridad personalizadas.",
                download_link="https://www.clamav.net/downloads",
                info_link="https://www.clamav.net"
            ),
            Tool(
                name="Malwarebytes",
                description="Malwarebytes es una herramienta de seguridad especializada en la detección y eliminación de malware avanzado, incluyendo virus, spyware, troyanos, rootkits, ransomware y adware. A diferencia de los antivirus tradicionales que dependen principalmente de firmas de virus, Malwarebytes utiliza un enfoque de análisis por comportamiento, lo que le permite identificar amenazas emergentes y software malicioso que aún no ha sido catalogado oficialmente.",
                download_link="https://www.malwarebytes.com/es/mwb-download/thankyou",
                info_link="https://www.malwarebytes.com/es/"
            ),
            Tool(
                name="Kaspersky Free Antivirus",
                description="Kaspersky es un conjunto de herramientas de seguridad integral que combina antivirus, protección contra malware, firewall y herramientas de seguridad en línea. Su motor antivirus está basado en firmas de malware actualizadas continuamente y técnicas de análisis heurístico, lo que le permite detectar tanto amenazas conocidas como nuevas variantes.",
                download_link="https://latam.kaspersky.com/downloads",
                info_link="https://latam.kaspersky.com/"
            )
        ]
    ),

    ToolCategory(
        category="Gestión de contraseñas",
        tools=[
            Tool(
                name="KeePassXC",
                description="Gestor de contraseñas local y open source, derivado de KeePass. Permite almacenar credenciales en una base de datos cifrada y acceder a ellas mediante una contraseña maestra o llave física. Es multiplataforma y soporta integración con navegadores.",
                download_link="https://keepassxc.org/download/",
                info_link="https://keepassxc.org"
            ),
            Tool(
                name="Bitwarden",
                description="Gestor de contraseñas multiplataforma con enfoque en la nube. Permite sincronizar credenciales entre dispositivos de manera segura, soporta 2FA, bóvedas compartidas y almacenamiento cifrado. Al ser open source, es muy utilizado por empresas y usuarios particulares como alternativa a LastPass o 1Password.",
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
                description="Herramienta de cifrado de disco open source, sucesora de TrueCrypt. Permite crear volúmenes cifrados dentro de archivos o cifrar particiones y discos completos, incluso el sistema operativo. Soporta algoritmos como AES, Serpent y Twofish, e incluso combinaciones en cascada. Es muy utilizada para proteger información sensible en laptops y discos externos frente a robos o accesos no autorizados.",
                download_link="https://www.veracrypt.fr/en/Downloads.html",
                info_link="https://www.veracrypt.fr"
            ),
            Tool(
                name="GnuPG (GPG)",
                description="Implementación libre del estándar OpenPGP. Sirve para cifrar, firmar digitalmente y autenticar archivos y correos electrónicos. Es ampliamente usado en comunicaciones seguras y en la validación de software distribuido por desarrolladores (firmas de paquetes). Funciona con claves públicas y privadas, garantizando confidencialidad e integridad de los datos.",
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
                description="Interfaz gráfica para la suite forense The Sleuth Kit (TSK). Facilita el análisis de discos, sistemas de archivos y dispositivos móviles. Permite examinar metadatos, recuperar archivos borrados, analizar registros de navegación web y detectar actividad sospechosa. Es muy utilizado por investigadores forenses y equipos de respuesta a incidentes.",
                download_link="https://www.autopsy.com/download/",
                info_link="https://www.autopsy.com"
            ),
            Tool(
                name="The Sleuth Kit (TSK)",
                description="Colección de herramientas de línea de comandos para el análisis forense de discos y sistemas de archivos. Puede recuperar información de particiones dañadas, analizar estructuras internas de sistemas como NTFS, FAT o EXT y extraer evidencia digital. Normalmente se utiliza en conjunto con Autopsy para una experiencia más amigable.",
                download_link="https://www.sleuthkit.org/sleuthkit/download.php",
                info_link="https://www.sleuthkit.org/sleuthkit"
            ),
            Tool(
                name="Volatility",
                description="Framework forense para el análisis de memoria RAM. Permite detectar procesos ocultos, conexiones de red, rootkits y actividad maliciosa en sistemas Windows, Linux y MacOS. Es muy usado en análisis post-mortem (después de un ataque) y en investigaciones de malware avanzado que opera en memoria.",
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
                description="Plataforma de monitoreo de infraestructura de TI. Supervisa disponibilidad de servidores, servicios, aplicaciones y dispositivos de red, generando alertas cuando se detectan problemas. Aunque su interfaz es más básica en comparación con otras herramientas modernas, sigue siendo muy utilizado en entornos corporativos por su flexibilidad y la gran cantidad de plugins disponibles.",
                download_link="https://www.nagios.org/downloads/",
                info_link="https://www.nagios.org"
            ),
            Tool(
                name="Zabbix",
                description="Plataforma de monitoreo empresarial que combina métricas en tiempo real, alertas y visualización gráfica. Permite recolectar datos de servidores, aplicaciones, bases de datos y redes, con agentes instalados en los equipos o mediante protocolos como SNMP. Es muy popular por su escalabilidad y facilidad de integración en grandes entornos de TI.",
                download_link="https://www.zabbix.com/download",
                info_link="https://www.zabbix.com"
            ),
            Tool(
                name="Prometheus",
                description="Sistema de monitoreo y alertas orientado a métricas y series temporales. Recoge datos en intervalos regulares a través de endpoints HTTP y los almacena en su base de datos propia, optimizada para consultas rápidas con su lenguaje PromQL. Es ampliamente usado en entornos de DevOps y microservicios junto con Kubernetes, Grafana y sistemas de observabilidad modernos.",
                download_link="https://prometheus.io/download/",
                info_link="https://prometheus.io"
            )
        ]
    )
]