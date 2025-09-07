# Estructura y Control

## Organización del Repositorio

```
Repository Root/
├── docs/                    # Documentación fuente
│   ├── XX-seccion/         # Agrupación por ATA chapter
│   │   ├── *.md           # Data Modules
│   │   └── index.md       # Índice de sección
│   ├── _data/             # Datos estructurados
│   │   └── dmrl.csv       # Lista maestra DMRL
│   └── _assets/           # Recursos multimedia
│       ├── images/        # Imágenes e ilustraciones
│       └── *.meta.json    # Metadatos ICN
├── tools/                  # Herramientas de validación
├── schemas/               # BREX y esquemas JSON
└── mkdocs.yml            # Configuración MkDocs
```

## Control de Versiones

### Estados de Documentos
- **Draft**: En desarrollo
- **Review**: Bajo revisión
- **Approved**: Aprobado para uso
- **Obsolete**: Fuera de uso

### Nomenclatura Git
- `feat/`: Nueva funcionalidad
- `fix/`: Corrección de errores
- `docs/`: Actualizaciones documentación
- `schema/`: Cambios en esquemas

## Gestión de Configuración

### Baseline Management
- Tags para releases estables
- Branches por configuración de producto
- Control de cambios documentado

### Trazabilidad
- Cada cambio vinculado a requisito
- Historial completo en git log
- Referencias cruzadas en DMRL