# Flujo de Trabajo

## Ciclo de Vida del Data Module

### 1. Planificación
- Identificar necesidad en DMRL
- Asignar autor y revisor
- Establecer fecha límite

### 2. Desarrollo
```bash
# Crear nuevo módulo desde plantilla
cp templates/des-template.md docs/XX-seccion/nuevo-modulo.md

# Completar metadatos y contenido
# Validar localmente
python tools/validate_dm_metadata.py --file docs/XX-seccion/nuevo-modulo.md
```

### 3. Validación
- Verificación automática con scripts
- Revisión de conformidad S1000D
- Pruebas de build MkDocs

### 4. Revisión
- Peer review técnica
- Aprobación de stakeholders
- Registro en DMRL

### 5. Publicación
- Merge a rama principal
- Actualización automática de site
- Notificación a usuarios

## Roles y Responsabilidades

| Rol | Responsabilidades |
|-----|------------------|
| **Autor** | Crear y mantener Data Modules |
| **Revisor** | Verificar contenido y conformidad |
| **Administrador** | Gestionar CSDB y herramientas |
| **Publicador** | Deploy y distribución |

## Herramientas de Workflow

- **Git**: Control de versiones
- **GitHub Actions**: CI/CD automático  
- **Scripts validación**: Verificación calidad
- **MkDocs**: Generación de publicación