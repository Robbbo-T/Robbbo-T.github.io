# Esquema JSON (metadatos DM)

Documentación del esquema JSON para validación de metadatos de Data Modules S1000D.

## Ubicación del Esquema

```
docs/90-anexos/esquemas/s1000d_dm_meta.schema.json
```

## Estructura Principal

El esquema define la validación para el front-matter YAML de cada Data Module:

### Campos Obligatorios

```json
{
  "required": ["utcs_mi_v5_id", "s1000d"],
  "properties": {
    "utcs_mi_v5_id": {
      "type": "string",
      "pattern": "^[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+:[^:]+$",
      "description": "13-field UTCS-MI v5.0 identifier separated by colons"
    }
  }
}
```

### Sección S1000D

Metadatos core del estándar S1000D:

```json
{
  "s1000d": {
    "type": "object",
    "required": ["schema_version", "dmc", "language", "issue", "security"],
    "properties": {
      "schema_version": {
        "type": "string",
        "enum": ["5.0", "4.2", "4.1", "4.0"]
      },
      "dmc": {
        "type": "string",
        "pattern": "^DMC-[A-Z0-9]{2,5}-[A-Z]-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{3}[A-Z]-[0-9]{3}[A-Z]-[A-Z]$"
      }
    }
  }
}
```

## Validaciones Específicas

### UTCS-MI v5.0

- **Formato**: 13 campos separados por `:` 
- **Pattern**: Regex para verificar estructura
- **Campos no vacíos**: Todos los campos deben tener contenido

### Data Module Code (DMC)

- **Formato S1000D**: Cumple estructura estándar
- **CAGE Code**: 2-5 caracteres alfanuméricos
- **Campos numéricos**: Formato específico por sección

### Metadatos Opcionales

```json
{
  "tektok_ref": {
    "type": "string",
    "pattern": "^TEKTOK-[A-Z]{3}-[a-z0-9-]+-[0-9]{4}$"
  },
  "dmrl_entry": {
    "type": "object",
    "properties": {
      "status": {
        "enum": ["required", "in-progress", "complete", "approved", "rejected"]
      }
    }
  }
}
```

## Uso del Esquema

### Validación Automática

```python
import json
import jsonschema

# Cargar esquema
with open('docs/90-anexos/esquemas/s1000d_dm_meta.schema.json') as f:
    schema = json.load(f)

# Validar front-matter
jsonschema.validate(frontmatter_data, schema)
```

### Integración con Tools

El esquema es utilizado por:

- `tools/validate_dm_metadata.py`: Validador principal
- CI/CD pipeline: Validación automática
- IDE extensions: Validación en tiempo real
- Documentation generators: Verificación de consistencia

## Extensiones del Esquema

### Campos Personalizados

Para añadir validaciones específicas del proyecto:

```json
{
  "custom_fields": {
    "type": "object",
    "properties": {
      "project_specific": {
        "type": "string",
        "pattern": "^PROJ-[0-9]{4}$"
      }
    }
  }
}
```

### Validaciones de Negocio

Reglas adicionales implementadas en el validador:

- Consistencia entre UTCS-MI y S1000D
- Referencias válidas a DMRL
- Formatos de fecha ISO 8601
- Códigos de seguridad válidos

## Mantenimiento del Esquema

### Versionado

El esquema sigue versionado semántico:
- **Major**: Cambios incompatibles
- **Minor**: Nuevos campos opcionales  
- **Patch**: Correcciones y mejoras

### Testing

```bash
# Test del esquema
python -m pytest tests/test_schema_validation.py

# Validación con datos de ejemplo
python tools/test_schema_examples.py
```

### Documentación

- **JSON Schema**: Definición formal
- **Markdown docs**: Explicación y ejemplos
- **Code comments**: Implementación detallada
- **Test cases**: Casos de uso cubiertos