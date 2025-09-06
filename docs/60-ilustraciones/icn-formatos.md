# ICN y Formatos

## Information Control Number (ICN)

Sistema de identificación única para recursos multimedia siguiendo S1000D.

### Estructura ICN

```
ICN-CAGE-SYSTEM-FIGURE-ITEM-VARIANT
```

**Componentes**:
- **CAGE**: Código organización (2-5 caracteres)
- **SYSTEM**: Sistema ATA (2 dígitos)
- **FIGURE**: Número de figura (4 dígitos)
- **ITEM**: Ítem dentro de figura (3 dígitos)
- **VARIANT**: Variante (1 letra)

### Ejemplos por Sistema

#### Propulsión (ATA 56)
```
ICN-AQUA-56-0001-001-A  # Diagrama general
ICN-AQUA-56-0001-002-A  # Motor eléctrico
ICN-AQUA-56-0002-001-A  # Celdas combustible
```

#### Sistema Eléctrico (ATA 24)
```
ICN-AQUA-24-0001-001-A  # Esquema eléctrico principal
ICN-AQUA-24-0001-002-A  # Distribución energía
```

## Formatos Soportados

### Imágenes Estáticas

| Formato | Uso Principal | Características |
|---------|---------------|-----------------|
| **SVG** | Diagramas técnicos | Vectorial, escalable, editable |
| **PNG** | Capturas, iconos | Transparencia, sin pérdidas |
| **JPG** | Fotografías | Compresión eficiente |
| **WebP** | Web optimizado | Menor tamaño, calidad alta |

### Contenido Multimedia

| Formato | Uso Principal | Características |
|---------|---------------|-----------------|
| **MP4** | Videos instructivos | Amplia compatibilidad |
| **WebM** | Videos web | Código abierto, eficiente |
| **PDF** | Documentos técnicos | Multiplataforma, imprimible |

## Metadatos Estándar

Cada recurso incluye archivo `.meta.json`:

```json
{
  "icn": "ICN-AQUA-56-0001-001-A",
  "title": "Diagrama Sistema Propulsión Principal",
  "description": "Vista general del sistema de propulsión con componentes principales",
  "format": "SVG",
  "dimensions": "1920x1080",
  "file_size": "125.7 KB",
  "security": "01",
  "created": "2025-01-16T10:00:00Z",
  "modified": "2025-01-16T15:30:00Z",
  "author": "Design Team",
  "checksum": "sha256:abc123def456...",
  "linked_dmc": [
    "DMC-AQUA-A-56-10-20-00-000A-040A-A"
  ],
  "keywords": ["propulsión", "hidrógeno", "motor", "celdas"],
  "revision": "Rev-A"
}
```

## Organización de Archivos

```
docs/_assets/
├── images/
│   ├── ICN-AQUA-56-0001-001-A.svg
│   ├── ICN-AQUA-56-0001-001-A.meta.json
│   ├── ICN-AQUA-56-0001-002-A.svg
│   └── ICN-AQUA-56-0001-002-A.meta.json
├── videos/
│   ├── ICN-AQUA-56-0002-001-A.mp4
│   └── ICN-AQUA-56-0002-001-A.meta.json
└── documents/
    ├── ICN-AQUA-56-0003-001-A.pdf
    └── ICN-AQUA-56-0003-001-A.meta.json
```

## Referenciado en Markdown

```markdown
<!-- Imagen simple -->
![Diagrama Propulsión](../_assets/images/ICN-AQUA-56-0001-001-A.svg)

<!-- Con caption y referencia ICN -->
![Diagrama Sistema Propulsión](../_assets/images/ICN-AQUA-56-0001-001-A.svg)
*Figura 1: Sistema de propulsión principal (ICN-AQUA-56-0001-001-A)*

<!-- Video embebido -->
<video controls>
  <source src="../_assets/videos/ICN-AQUA-56-0002-001-A.mp4" type="video/mp4">
</video>
*Video 1: Procedimiento arranque motor (ICN-AQUA-56-0002-001-A)*
```

## Validación de ICN

```python
import re

def validate_icn(icn):
    pattern = r'^ICN-[A-Z0-9]{2,5}-[0-9]{2}-[0-9]{4}-[0-9]{3}-[A-Z]$'
    return re.match(pattern, icn) is not None

# Ejemplos
validate_icn("ICN-AQUA-56-0001-001-A")  # True
validate_icn("ICN-INVALID-FORMAT")       # False
```