import streamlit as st
from data.tools_data import tools_data, ToolCategory, Tool

# Configuración de la página
st.set_page_config(
    page_title="Baúl de Herramientas",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Tarjetas */
    .tool-card {
        background-color: #243444; /* secondaryBackgroundColor */
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #246c7c; /* primaryColor */
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    .tool-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.4);
    }

    /* Títulos y texto */
    .tool-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #3abeb6; /* textColor */
        margin-bottom: 0.5rem;
    }
    .tool-description {
        color: #d1e3e2; /* texto secundario claro */
        margin-bottom: 1rem;
        line-height: 1.5;
    }

    /* Encabezado de categoría */
    .category-header {
        color: #3abeb6; /* textColor */
        border-bottom: 2px solid #246c7c; /* primaryColor */
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }

    /* Títulos principales */
    .main-title {
        text-align: center;
        color: #3abeb6; /* textColor */
        margin-bottom: 2rem;
    }
    .subtitle {
        text-align: center;
        color: #a8cfcf; /* tono más suave para contraste */
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #243444; /* secondaryBackgroundColor */
        border-radius: 8px;
        border: 1px solid #246c7c; /* primaryColor */
        color: #3abeb6; /* textColor */
        transition: all 0.2s ease-in-out;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #2f4c5c; /* un poco más claro que secondaryBackground */
        cursor: pointer;
    }
    .stTabs [aria-selected="true"] {
        background-color: #246c7c; /* primaryColor */
        color: #ffffff;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


def display_tool_card(tool: Tool):
    """Muestra una tarjeta individual de herramienta"""
    st.markdown(f"""
    <div class="tool-card">
        <div class="tool-title">{tool.name}</div>
        <div class="tool-description">{tool.description}</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if tool.download_link != "#":
            st.link_button("⬇️ Descargar", tool.download_link, use_container_width=True)
        else:
            st.button("⬇️ Descargar", key=f"download_{tool.name.replace(' ', '_')}", disabled=True, help="Placeholder - Agregar link real", use_container_width=True)
    
    with col2:
        st.button("ℹ️ Info", key=f"info_{tool.name.replace(' ', '_')}", help="Más información sobre esta herramienta", use_container_width=True)

def display_category_stats():
    """Muestra estadísticas generales del baúl de herramientas"""
    total_tools = sum(len(category.tools) for category in tools_data)
    total_categories = len(tools_data)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Herramientas", total_tools)
    with col2:
        st.metric("Categorías", total_categories)
    with col3:
        st.metric("Herramientas por Categoría", f"{total_tools/total_categories:.1f}")

def main():
    # Título principal
    st.markdown('<h1 class="main-title">🧰 Baúl de Herramientas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Colección organizada de herramientas de seguridad y administración de sistemas</p>', unsafe_allow_html=True)
    
    # Verificar si hay datos
    if not tools_data:
        st.error("❌ No hay herramientas disponibles.")
        st.info("💡 Agrega herramientas editando el archivo `data/tools_data.py`")
        return
    
    # Mostrar estadísticas
    display_category_stats()
    st.markdown("---")
    
    # Crear tabs para cada categoría
    category_names = [category.category for category in tools_data]
    tabs = st.tabs(category_names)
    
    for tab, category in zip(tabs, tools_data):
        with tab:
            st.markdown(f'<h2 class="category-header">📁 {category.category}</h2>', unsafe_allow_html=True)
            
            if not category.tools:
                st.warning(f"No hay herramientas disponibles en la categoría '{category.category}'")
                continue
            
            # Mostrar herramientas en columnas
            cols = st.columns(2)
            for j, tool in enumerate(category.tools):
                with cols[j % 2]:
                    display_tool_card(tool)
                    st.markdown("<br>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6c757d; padding: 1rem;'>
        <p>💡 <strong>Nota:</strong> Todas las herramientas mostradas son placeholders. 
        Edita el archivo <code>data/tools_data.py</code> para agregar herramientas reales.</p>
        <p>🔧 Para agregar una nueva herramienta, simplemente agrega un nuevo objeto <code>Tool</code> 
        a la categoría correspondiente con nombre, descripción y link de descarga.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
