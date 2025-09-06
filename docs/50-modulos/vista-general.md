# Vista General

## Tipos de Data Modules

El sistema soporta tres tipos principales de Data Modules según el estándar S1000D:

### DES - Descriptive Data Module

**Código de información**: 000A

**Propósito**: Proporcionar información descriptiva sobre:
- Sistemas y subsistemas
- Componentes y partes
- Funcionamiento y características técnicas
- Especificaciones y limitaciones

**Estructura típica**:
1. Introducción y propósito
2. Descripción general del sistema
3. Componentes principales
4. Especificaciones técnicas
5. Interfaces y conexiones
6. Limitaciones operacionales
7. Referencias

### PRC - Procedural Data Module

**Código de información**: 001A

**Propósito**: Proporcionar procedimientos paso a paso para:
- Operaciones normales
- Procedimientos de mantenimiento
- Pruebas y verificaciones
- Procedimientos de emergencia

**Estructura típica**:
1. Alcance del procedimiento
2. Precondiciones y advertencias
3. Equipos y herramientas requeridos
4. Pasos detallados del procedimiento
5. Verificaciones y criterios de aceptación
6. Acciones en caso de fallo
7. Documentación post-procedimiento

### FSC - Fault Schema Chart

**Código de información**: 002A

**Propósito**: Proporcionar guías de diagnóstico para:
- Identificación de fallos
- Aislamiento de problemas
- Procedimientos de reparación
- Códigos de error del sistema

**Estructura típica**:
1. Síntomas y descripción del problema
2. Posibles causas
3. Árboles de diagnóstico
4. Herramientas especializadas
5. Procedimientos de verificación
6. Acciones correctivas
7. Repuestos críticos

## Metadatos Comunes

Todos los Data Modules incluyen:

### UTCS-MI v5.0
Identificador de 13 campos para trazabilidad:
```
EstándarUniversal:TipoDocumento:Genesis-S1000D:5.0:Categoria:Secuencial:Version:TekniaTokens:GeneracionHumana:CROSS:AquaTechnologies:hash:RestoDeVidaUtil
```

### S1000D Core
- **DMC**: Data Module Code único
- **Title**: Título descriptivo
- **Language**: Código de idioma
- **Issue**: Número de emisión
- **Security**: Clasificación de seguridad

## Plantillas Disponibles

| Tipo | Plantilla | Ejemplo |
|------|-----------|---------|
| **DES** | `templates/des-template.md` | [Ver ejemplo](des-descriptivo-ejemplo.md) |
| **PRC** | `templates/prc-template.md` | [Ver ejemplo](prc-procedimiento-ejemplo.md) |
| **FSC** | `templates/fsc-template.md` | [Ver ejemplo](fsc-fallos-ejemplo.md) |

## Workflow de Creación

1. **Seleccionar** tipo de módulo (DES/PRC/FSC)
2. **Copiar** plantilla correspondiente
3. **Generar** DMC siguiendo nomenclatura
4. **Completar** UTCS-MI v5.0 ID
5. **Escribir** contenido específico
6. **Validar** con scripts automáticos
7. **Registrar** en DMRL
8. **Revisar** y aprobar