# Guía de Conformidad

## Pasos para Cumplimiento S1000D

### 1. Estructura del Data Module

Cada Data Module debe seguir esta estructura:

```markdown
---
# Front-matter YAML con metadatos S1000D
utcs_mi_v5_id: "campo1:campo2:...:campo13"
s1000d:
  schema_version: "5.0"
  dmc: "DMC-CAGE-TYPE-SYSTEM-..."
  # ... otros campos requeridos
---

# Contenido del módulo en Markdown
```

### 2. Metadatos Obligatorios

#### UTCS-MI v5.0
- 13 campos separados por `:`
- Formato: `Estándar:Tipo:Dominio:Versión:Categoría:Secuencial:Contenido:Proyecto:Generación:Clasificación:Organización:Hash:CicloVida`

#### S1000D Core
- `schema_version`: Versión del esquema S1000D
- `dmc`: Data Module Code válido
- `language`: Código de idioma (ISO 639-1)
- `issue`: Número de emisión
- `security`: Clasificación de seguridad

### 3. Data Module Code (DMC)

Estructura: `DMC-CAGE-TYPE-SYSTEM-SUBSYSTEM-ASSEMBLY-SUBASSEMBLY-INFO-LOCATION-VARIANT`

Ejemplo: `DMC-AQUA-A-56-10-20-00-000A-040A-A`

### 4. Validación

```bash
# Ejecutar validador
python tools/validate_dm_metadata.py

# Verificar conformidad de archivo específico
python tools/validate_dm_metadata.py --file docs/50-modulos/ejemplo.md
```

## Checklist de Conformidad

- [ ] Front-matter YAML presente
- [ ] UTCS-MI v5.0 con 13 campos
- [ ] DMC válido según patrón S1000D
- [ ] Metadatos obligatorios completos
- [ ] Referencia DMRL (si aplicable)
- [ ] Validación automática sin errores