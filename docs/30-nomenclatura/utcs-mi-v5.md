# UTCS‑MI v5.0

Universal Technical Classification System - Metadata Identification v5.0

## Estructura de 13 Campos

El UTCS-MI v5.0 utiliza exactamente 13 campos separados por dos puntos `:`:

```
Campo1:Campo2:Campo3:Campo4:Campo5:Campo6:Campo7:Campo8:Campo9:Campo10:Campo11:Campo12:Campo13
```

## Definición de Campos

| # | Campo | Descripción | Ejemplo |
|---|-------|-------------|---------|
| 1 | **Estándar** | Identificador del estándar | `EstándarUniversal` |
| 2 | **Tipo** | Tipo de documento | `Documento`, `Procedimiento` |
| 3 | **Dominio** | Dominio técnico | `Genesis-S1000D` |
| 4 | **Versión Esquema** | Versión del esquema | `5.0` |
| 5 | **Categoría Info** | Categoría de información | `DescripcionSistema` |
| 6 | **Secuencial** | Número secuencial | `0001`, `0002` |
| 7 | **Versión Contenido** | Versión del contenido | `v1.0`, `v2.1` |
| 8 | **Proyecto** | Nombre del proyecto | `TekniaTokens` |
| 9 | **Generación** | Tipo de generación | `GeneracionHumana` |
| 10 | **Clasificación** | Nivel de acceso | `CROSS`, `RESTRICTED` |
| 11 | **Organización** | Organización responsable | `AquaTechnologies` |
| 12 | **Hash** | Hash corto (8 chars) | `d34db33f` |
| 13 | **Ciclo Vida** | Estado del ciclo de vida | `RestoDeVidaUtil` |

## Ejemplos Completos

### Data Module Descriptivo
```
EstándarUniversal:Documento:Genesis-S1000D:5.0:DescripcionSistema:0002:v1.0:TekniaTokens:GeneracionHumana:CROSS:AquaTechnologies:d34db33f:RestoDeVidaUtil
```

### Procedimiento Operacional
```  
EstándarUniversal:Procedimiento:Genesis-S1000D:5.0:ProcedimientoOperacion:0003:v1.0:TekniaTokens:GeneracionHumana:CROSS:AquaTechnologies:e45ab67c:RestoDeVidaUtil
```

## Validación

```python
def validate_utcs_mi_v5(utcs_id):
    fields = utcs_id.split(':')
    if len(fields) != 13:
        return False, f"Expected 13 fields, got {len(fields)}"
    return True, None
```

## Integración con S1000D

El UTCS-MI v5.0 complementa el DMC S1000D proporcionando:

- **Trazabilidad completa**: Desde requisito hasta implementación
- **Metadatos extendidos**: Información no cubierta por S1000D
- **Versionado granular**: Control de cambios detallado
- **Clasificación flexible**: Adaptable a diferentes contextos