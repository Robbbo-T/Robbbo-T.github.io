# DMRL · Catálogo (CSV)

El catálogo DMRL se mantiene en formato CSV para facilitar la importación/exportación y el procesamiento automatizado.

## Acceso al Catálogo

El archivo maestro se encuentra en: `docs/_data/dmrl.csv`

### Campos del DMRL

| Campo | Descripción | Formato | Requerido |
|-------|-------------|---------|-----------|
| `dmrl_id` | Identificador único DMRL | DMRL-NNNN | ✅ |
| `dmc` | Data Module Code S1000D | DMC-... | ✅ |
| `title` | Título descriptivo | Texto libre | ✅ |
| `type` | Tipo de módulo | DES/PRC/FSC | ✅ |
| `status` | Estado actual | Ver estados | ✅ |
| `priority` | Prioridad | critical/high/medium/low | ✅ |
| `responsible_org` | Organización responsable | CAGE code | ✅ |
| `assigned_author` | Autor asignado | ID usuario | - |
| `due_date` | Fecha límite | YYYY-MM-DD | - |
| `created_date` | Fecha creación | YYYY-MM-DD | ✅ |
| `modified_date` | Última modificación | YYYY-MM-DD | ✅ |
| `tektok_ref` | Referencia TEKTOK | TEKTOK-... | - |
| `notes` | Notas adicionales | Texto libre | - |

## Catálogo Actual

<div style="max-height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px;">

```csv
dmrl_id,dmc,title,type,status,priority,responsible_org,assigned_author,due_date,created_date,modified_date,tektok_ref,notes
DMRL-0001,DMC-AQUA-A-00-00-00-00-000A-040A-A,Introducción al Sistema S1000D,DES,required,high,AQUA,system,2025-02-15,2025-01-16,2025-01-16,,Documento introductorio del sistema
DMRL-0002,DMC-AQUA-A-56-10-20-00-000A-040A-A,Descripción Sistema Propulsión,DES,in-progress,critical,AQUA,propulsion-team,2025-02-01,2025-01-16,2025-01-16,TEKTOK-ATA-56-propulsion-desc-0001,Sistema de propulsión principal
DMRL-0003,DMC-AQUA-A-56-10-20-00-001A-040A-A,Procedimiento Arranque Motor,PRC,required,high,AQUA,maintenance-team,2025-02-10,2025-01-16,2025-01-16,,Procedimientos de arranque y parada
DMRL-0004,DMC-AQUA-A-56-10-20-00-002A-040A-A,Diagnóstico Fallos Propulsión,FSC,required,medium,AQUA,diagnostics-team,2025-02-20,2025-01-16,2025-01-16,,Guía de diagnóstico y solución de problemas
DMRL-0005,DMC-AQUA-A-32-20-10-00-000A-040A-A,Descripción Tren de Aterrizaje,DES,complete,high,AQUA,landing-gear-team,2025-01-30,2025-01-10,2025-01-15,,Sistema de tren de aterrizaje principal
DMRL-0006,DMC-AQUA-A-32-20-10-00-001A-040A-A,Procedimiento Extensión Tren,PRC,in-progress,high,AQUA,operations-team,2025-02-05,2025-01-12,2025-01-16,,Procedimientos de operación del tren
DMRL-0007,DMC-AQUA-A-71-10-00-00-000A-040A-A,Descripción Sistema Motores,DES,required,critical,AQUA,engine-team,2025-01-25,2025-01-16,2025-01-16,TEKTOK-ATA-71-engine-system-0001,Motores principales de la aeronave
DMRL-0008,DMC-AQUA-A-28-10-00-00-000A-040A-A,Descripción Sistema Combustible,DES,required,critical,AQUA,fuel-systems,2025-02-08,2025-01-16,2025-01-16,,Sistema de combustible y distribución
DMRL-0009,DMC-AQUA-A-24-10-00-00-000A-040A-A,Descripción Sistema Eléctrico,DES,in-progress,high,AQUA,electrical-team,2025-02-12,2025-01-14,2025-01-16,TEKTOK-ATA-24-electrical-power-0001,Sistema eléctrico principal
DMRL-0010,DMC-AQUA-A-27-10-00-00-000A-040A-A,Descripción Controles de Vuelo,DES,required,critical,AQUA,flight-controls,2025-01-28,2025-01-16,2025-01-16,,Sistemas de control de vuelo primarios
```

</div>

## Análisis del Estado Actual

### Por Estado
- **Required**: 6 módulos (60%)
- **In-Progress**: 3 módulos (30%)
- **Complete**: 1 módulo (10%)
- **Approved**: 0 módulos (0%)

### Por Tipo
- **DES (Descriptivo)**: 7 módulos (70%)
- **PRC (Procedimiento)**: 2 módulos (20%)
- **FSC (Fallos)**: 1 módulo (10%)

### Por Prioridad
- **Critical**: 4 módulos (40%)
- **High**: 5 módulos (50%)
- **Medium**: 1 módulo (10%)

## Gestión del Catálogo

### Actualización Manual
El archivo CSV puede editarse directamente en cualquier editor de texto o hoja de cálculo.

### Validación Automática
```bash
# Validar consistencia DMRL
python tools/validate_dm_metadata.py

# Generar reporte de estado
python scripts/dmrl_report.py
```

### Integración con Git
Los cambios en el DMRL se rastrean automáticamente mediante git:

```bash
# Ver historial de cambios
git log --follow docs/_data/dmrl.csv

# Ver diferencias
git diff HEAD~1 docs/_data/dmrl.csv
```

## Workflow de Actualización

1. **Identificar** nuevo requisito de módulo
2. **Asignar** DMRL-ID único
3. **Generar** DMC siguiendo nomenclatura S1000D
4. **Completar** metadatos requeridos
5. **Actualizar** CSV maestro
6. **Validar** con script de verificación
7. **Commit** cambios con mensaje descriptivo

## Enlaces Relacionados

- [Esquema JSON para metadatos](../90-anexos/esquema-json-metadatos.md)
- [Nomenclatura DMC](../30-nomenclatura/data-module-code.md)
- [Ejemplos de módulos](../50-modulos/vista-general.md)