# Cambios y Versionado

## Esquema de Versionado

El sistema utiliza **Semantic Versioning** (SemVer) para el control de versiones:

```
MAJOR.MINOR.PATCH
```

### Incremento de Versiones

- **MAJOR**: Cambios incompatibles en API/estructura
- **MINOR**: Nuevas funcionalidades compatibles
- **PATCH**: Correcciones de bugs y mejoras menores

### Ejemplos
- `1.0.0` → `1.0.1`: Corrección de typos
- `1.0.1` → `1.1.0`: Nuevo tipo de Data Module
- `1.1.0` → `2.0.0`: Cambio en esquema UTCS-MI

## Control de Cambios en Data Modules

### Metadatos de Versión

Cada Data Module incluye:

```yaml
s1000d:
  issue: "001"          # Número de emisión S1000D
  inWork: "00"          # Trabajo en curso
metadata:
  version: "v1.2"       # Versión contenido
  created: "2025-01-16"
  modified: "2025-01-20"
```

### Historial de Cambios

Control mediante:
- **Git commits**: Cada cambio rastreado
- **PR descriptions**: Documentación del cambio
- **DMRL updates**: Estado sincronizado
- **Change log**: Resumen de modificaciones

## Workflow de Cambios

### 1. Solicitud de Cambio

```bash
# Crear feature branch
git checkout -b feat/update-propulsion-system

# Hacer cambios
# Validar localmente
python tools/validate_dm_metadata.py

# Commit con mensaje descriptivo
git commit -m "feat: Update propulsion system specifications

- Add hydrogen fuel cell efficiency metrics
- Update safety procedures
- Refresh diagram ICN-AQUA-56-0001-001-A

Refs: DMRL-0002"
```

### 2. Revisión y Aprobación

```bash
# Push branch
git push origin feat/update-propulsion-system

# Crear Pull Request
# - Descripción detallada del cambio
# - Links a DMRL entries afectados
# - Capturas de pantalla si hay cambios visuales
# - Checklist de verificación

# Review automatizada:
# - Validación S1000D
# - Build test
# - Link checker
```

### 3. Integración

```bash
# Tras aprobación
git checkout main
git merge feat/update-propulsion-system
git tag v1.2.0
git push origin main --tags
```

## Tipos de Commits

Siguiendo **Conventional Commits**:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `feat` | Nueva funcionalidad | `feat: Add FSC module for electrical system` |
| `fix` | Corrección de error | `fix: Correct DMC format in propulsion DES` |
| `docs` | Cambios documentación | `docs: Update installation instructions` |
| `style` | Formateo, espacios | `style: Fix markdown formatting` |
| `refactor` | Refactorización | `refactor: Reorganize navigation structure` |
| `test` | Añadir/modificar tests | `test: Add validation tests for UTCS-MI` |
| `chore` | Mantenimiento | `chore: Update dependencies` |

## Gestión de Releases

### Release Notes

Para cada release se genera:

```markdown
## Version 1.2.0 (2025-01-20)

### Added
- New FSC module for electrical system diagnosis
- Interactive diagrams with Mermaid
- DMRL status dashboard

### Changed  
- Updated propulsion system specifications
- Improved validation script performance
- Enhanced error messages

### Fixed
- Corrected DMC format validation
- Fixed broken links in navigation
- Resolved ICN metadata inconsistencies

### Removed
- Deprecated legacy validation script
```

### Deployment

```bash
# Tag release
git tag -a v1.2.0 -m "Release v1.2.0: Enhanced validation and new modules"

# Deploy to production
mkdocs gh-deploy --force

# Update DMRL status
python tools/update_dmrl_status.py --release v1.2.0
```

## Rollback Procedures

### Emergency Rollback

```bash
# Identificar último tag estable
git tag --sort=-version:refname | head -5

# Rollback a versión anterior
git checkout v1.1.0
mkdocs gh-deploy --force

# Notificar rollback
python tools/notify_rollback.py --version v1.1.0 --reason "Critical validation error"
```

### Rollback Selectivo

```bash
# Revertir commit específico
git revert <commit-hash>

# Rebuild y redeploy
mkdocs build --strict
mkdocs gh-deploy
```

## Auditoría y Compliance

### Registro de Cambios

- **Git log completo**: Todos los cambios rastreados
- **PR history**: Decisiones documentadas
- **DMRL updates**: Estado de módulos
- **Deployment logs**: Historial de publicaciones

### Informes de Compliance

```bash
# Generar informe mensual
python tools/generate_compliance_report.py --month 2025-01

# Verificar trazabilidad UTCS-MI
python tools/audit_utcs_traceability.py

# Validar conformidad S1000D
python tools/s1000d_compliance_check.py
```