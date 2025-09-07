# S1000D · Data Module Code (DMC)

El Data Module Code es el identificador único de cada módulo en el estándar S1000D.

## Estructura del DMC

```
DMC-CAGE-TYPE-SYSTEM-SUBSYSTEM-ASSEMBLY-SUBASSEMBLY-INFO-LOCATION-VARIANT
```

## Componentes del DMC

### Model Identification Code
- **CAGE**: Código de identificación comercial (2-5 caracteres)
- **TYPE**: Tipo de información (A=General, B=Crew)

### System Breakdown
- **SYSTEM**: Código ATA del sistema (2 dígitos)
- **SUBSYSTEM**: Código del subsistema (2 dígitos)  
- **ASSEMBLY**: Código del conjunto (2 dígitos)
- **SUBASSEMBLY**: Código del subconjunto (2 dígitos)

### Information Code
- **INFO**: Tipo de información + número (3 caracteres + 1 letra)
- **LOCATION**: Código de ubicación (3 dígitos + 1 letra)  
- **VARIANT**: Variante del módulo (1 letra)

## Tipos de Información Comunes

| Código | Descripción | Uso |
|--------|-------------|-----|
| **000A** | Descripción general | Módulos DES |
| **001A** | Procedimiento operacional | Módulos PRC |
| **002A** | Diagnóstico de fallos | Módulos FSC |
| **003A** | Procedimiento de mantenimiento | Mantenimiento |
| **040A** | Descripción de sistema | Sistemas específicos |

## Ejemplos de DMC

### Sistema de Propulsión (ATA 56)
```
DMC-AQUA-A-56-10-20-00-000A-040A-A
│   │    │ │  │  │  │  │    │    │
│   │    │ │  │  │  │  │    │    └─ Variante A
│   │    │ │  │  │  │  │    └────── Ubicación 040A  
│   │    │ │  │  │  │  └─────────── Info 000A (Descripción)
│   │    │ │  │  │  └────────────── Subassembly 00
│   │    │ │  │  └───────────────── Assembly 20
│   │    │ │  └──────────────────── Subsystem 10
│   │    │ └─────────────────────── System 56 (Propulsión)
│   │    └───────────────────────── Type A (General)
│   └────────────────────────────── CAGE AQUA
└─────────────────────────────────── Prefijo DMC
```

### Sistema Eléctrico (ATA 24)
```
DMC-AQUA-A-24-10-00-00-000A-040A-A  # Descripción sistema eléctrico
DMC-AQUA-A-24-10-00-00-001A-040A-A  # Procedimiento operación
DMC-AQUA-A-24-10-00-00-002A-040A-A  # Diagnóstico fallos
```

## Generación Automática

```python
def generate_dmc(cage, system, subsystem, assembly, info_type, info_num):
    return f"DMC-{cage}-A-{system:02d}-{subsystem:02d}-{assembly:02d}-00-{info_type}{info_num:03d}A-040A-A"

# Ejemplo
dmc = generate_dmc("AQUA", 56, 10, 20, "000", 1)
# Resultado: DMC-AQUA-A-56-10-20-00-000A-001A-A
```

## Validación

El patrón regex para validar DMC:
```regex
^DMC-[A-Z0-9]{2,5}-[A-Z]-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{3}[A-Z]-[0-9]{3}[A-Z]-[A-Z]$
```