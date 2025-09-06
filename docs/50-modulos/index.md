# 50 · Módulos de Datos

Plantillas y ejemplos de Data Modules siguiendo el estándar S1000D con metadatos UTCS-MI v5.0.

## Contenido de la Sección

- **[Vista general](vista-general.md)**: Introducción a los tipos de módulos
- **[DES · Descriptivo (ejemplo)](des-descriptivo-ejemplo.md)**: Ejemplo de módulo descriptivo
- **[PRC · Procedimiento (ejemplo)](prc-procedimiento-ejemplo.md)**: Ejemplo de procedimiento
- **[FSC · Fallos (ejemplo)](fsc-fallos-ejemplo.md)**: Ejemplo de diagnóstico

## Tipos de Módulos

### DES - Descriptivo
**Propósito**: Describir sistemas, componentes y su funcionamiento

**Contenido típico**:
- Introducción y propósito
- Especificaciones técnicas  
- Diagramas y esquemas
- Interfaces y conexiones
- Limitaciones operacionales

### PRC - Procedimiento  
**Propósito**: Instrucciones paso a paso para operaciones

**Contenido típico**:
- Precondiciones y advertencias
- Equipos requeridos
- Pasos numerados detallados
- Verificaciones y criterios de aceptación
- Acciones en caso de fallo

### FSC - Fault Schema Chart
**Propósito**: Diagnóstico y solución de problemas

**Contenido típico**:
- Síntomas y causas
- Árboles de diagnóstico
- Herramientas especializadas
- Procedimientos de reparación
- Repuestos críticos

## Front-matter Estándar

Todos los módulos incluyen:

```yaml
---
utcs_mi_v5_id: "campo1:campo2:...:campo13"
s1000d:
  schema_version: "5.0"
  dmc: "DMC-CAGE-TYPE-..."
  title: "Título del módulo"
  language: "es-ES"
  issue: "001"
  security: "01"
tektok_ref: "TEKTOK-XXX-..."  # Opcional
dmrl_entry:
  dmrl_id: "DMRL-NNNN"
  status: "in-progress"
metadata:
  created: "2025-01-16T10:00:00Z"
  authors: [...]
---
```

## Validación Automática

Todos los módulos pasan por:

1. **Schema validation**: Estructura JSON Schema
2. **S1000D compliance**: DMC y metadatos válidos
3. **UTCS-MI v5.0**: 13 campos correctos
4. **Business rules**: Reglas específicas del proyecto