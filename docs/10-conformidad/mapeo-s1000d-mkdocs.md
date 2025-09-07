# Mapeo Rápido (S1000D → MkDocs)

## Correspondencias de Elementos

| Elemento S1000D | Implementación MkDocs | Ubicación |
|------------------|----------------------|-----------|
| **Data Module** | Archivo Markdown | `docs/XX-seccion/archivo.md` |
| **DMC** | Campo `s1000d.dmc` | Front-matter YAML |
| **Title** | Título H1 + `s1000d.title` | Primer heading + metadatos |
| **Security** | Campo `s1000d.security` | Front-matter |
| **Language** | Campo `s1000d.language` | Front-matter |
| **Issue** | Campo `s1000d.issue` | Front-matter |
| **ICN** | Referencias en `_assets/` | Enlaces en contenido |
| **DMRL** | Archivo CSV | `docs/_data/dmrl.csv` |
| **BREX** | JSON Schema | `docs/90-anexos/esquemas/` |

## Mapeo de Tipos de Módulos

### DES (Descriptive)
```yaml
s1000d:
  dmc: "DMC-CAGE-A-XX-XX-XX-XX-000A-040A-A"
```
- **Propósito**: Describir sistemas, componentes, operación
- **Contenido**: Especificaciones, diagramas, características

### PRC (Procedural)
```yaml
s1000d:
  dmc: "DMC-CAGE-A-XX-XX-XX-XX-001A-040A-A"
```
- **Propósito**: Procedimientos paso a paso
- **Contenido**: Listas numeradas, precauciones, herramientas

### FSC (Fault Schema Chart)
```yaml
s1000d:
  dmc: "DMC-CAGE-A-XX-XX-XX-XX-002A-040A-A"
```
- **Propósito**: Diagnóstico y solución de problemas
- **Contenido**: Árboles de decisión, síntomas, causas

## Estructura de Archivos

```
docs/
├── XX-seccion/           # Agrupación por ATA chapter
│   ├── index.md         # Índice de sección
│   ├── des-*.md         # Módulos descriptivos
│   ├── prc-*.md         # Módulos de procedimiento
│   └── fsc-*.md         # Módulos de fallos
├── _data/
│   └── dmrl.csv         # Lista maestra DMRL
├── _assets/
│   ├── images/          # ICN multimedia
│   └── *.meta.json      # Metadatos ICN
└── 90-anexos/
    └── esquemas/        # BREX/schemas
```

## Flujo de Trabajo

1. **Crear** estructura de carpetas por ATA chapter
2. **Generar** DMC siguiendo nomenclatura
3. **Completar** front-matter con metadatos S1000D
4. **Escribir** contenido siguiendo plantillas
5. **Validar** con script automático
6. **Registrar** en DMRL
7. **Revisar** y aprobar según workflow

## Herramientas de Mapeo

- **Generador DMC**: Script para crear códigos válidos
- **Plantillas**: Templates por tipo de módulo
- **Validador**: Verificación automática de conformidad
- **Conversor**: Migración desde otros formatos