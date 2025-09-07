# 10 · Conformidad S1000D

Esta sección proporciona las guías y herramientas necesarias para asegurar el cumplimiento del estándar S1000D en el sistema de documentación Teknia Tokens.

## Contenido de la Sección

- **[Guía de conformidad](guia-conformidad.md)**: Pasos específicos para cumplir con S1000D
- **[Mapeo rápido (S1000D → MkDocs)](mapeo-s1000d-mkdocs.md)**: Correspondencias entre elementos S1000D y MkDocs

## Objetivos de Conformidad

La conformidad S1000D busca asegurar que:

- ✅ **Estructura**: Los módulos siguen la estructura estándar S1000D
- ✅ **Metadatos**: Todos los campos requeridos están presentes
- ✅ **Nomenclatura**: DMC e ICN siguen las convenciones
- ✅ **Validación**: Scripts automáticos verifican cumplimiento
- ✅ **Trazabilidad**: UTCS-MI v5.0 proporciona seguimiento completo

## Niveles de Conformidad

| Nivel | Descripción | Validación |
|-------|-------------|------------|
| **Básico** | Estructura mínima S1000D | Schema JSON |
| **Intermedio** | Metadatos completos + DMC válido | Script validación |
| **Avanzado** | UTCS-MI v5.0 + TEKTOK links | Validación completa |

## Herramientas de Conformidad

- **JSON Schema**: Validación automática de front-matter
- **Script validador**: `tools/validate_dm_metadata.py`
- **Plantillas**: Ejemplos DES/PRC/FSC conformes
- **DMRL**: Lista maestra con seguimiento de estado