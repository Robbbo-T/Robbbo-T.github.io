---
utcs_mi_v5_id: "EstándarUniversal:Procedimiento:Genesis-S1000D:5.0:ProcedimientoOperacion:0003:v1.0:TekniaTokens:GeneracionHumana:CROSS:AquaTechnologies:e45ab67c:RestoDeVidaUtil"
s1000d:
  schema_version: "5.0"
  dmc: "DMC-AQUA-A-56-10-20-00-001A-040A-A"
  title: "Procedimiento Arranque Motor"
  language: "es-ES"
  issue: "001"
  security: "01"
  responsiblePartnerCompany: "AQUA"
  originator: "AQUA"
  applicability:
    assert: ["Q100-0001", "BWB-H2"]
  brexDmRef:
    dmRef:
      dmRefIdent:
        dmCode: "DMC-AQUA-A-00-00-00-00-001A-040A-A"
dmrl_entry:
  dmrl_id: "DMRL-0003"
  status: "required"
  priority: "high"
metadata:
  created: "2025-01-16T10:00:00Z"
  modified: "2025-01-16T15:30:00Z"
  authors:
    - name: "Maintenance Team"
      id: "maintenance@aquatech.com"
      role: "procedure-author"
  reviewers:
    - name: "Operations Manager"
      id: "ops-mgr@aquatech.com"
      status: "pending"
---

# Procedimiento Arranque Motor

## Alcance

Este procedimiento describe los pasos para el arranque seguro del sistema de propulsión de hidrógeno en la aeronave Q100-0001.

## Precondiciones

Antes de iniciar este procedimiento, verificar:

- [ ] Aeronave en tierra y asegurada
- [ ] Chequeos pre-vuelo completados
- [ ] Personal autorizado únicamente
- [ ] Área despejada de personal no autorizado
- [ ] Sistemas de emergencia operativos

## Advertencias y Precauciones

!!! danger "PELIGRO - Hidrógeno Inflamable"
    El hidrógeno es altamente inflamable. Mantener todas las fuentes de ignición alejadas del área de operación.

!!! warning "PRECAUCIÓN - Alta Presión"
    El sistema opera a 700 bar. Usar únicamente herramientas y equipos certificados.

!!! note "NOTA"
    Este procedimiento debe realizarse por personal certificado en sistemas de hidrógeno.

## Equipos Requeridos

| Equipo | Parte/Modelo | Cantidad |
|--------|--------------|----------|
| Detector de fugas H₂ | HD-2000Pro | 1 |
| Multímetro | Fluke-87V | 1 |
| Tablet diagnóstico | Surface Pro 9 | 1 |
| EPP completo | - | 1 set |

## Procedimiento de Arranque

### Fase 1: Verificaciones Pre-Arranque

#### Paso 1: Inspección Visual
1. **Inspeccionar** visualmente el compartimento del motor:
   - Verificar ausencia de fugas
   - Comprobar conexiones seguras
   - Revisar estado de paneles de acceso

2. **Verificar** indicadores de estado:
   - LED verde en controlador principal
   - Presión H₂ > 50 bar en tanques
   - Temperatura ambiente dentro de límites

#### Paso 2: Verificación de Sistemas
1. **Encender** sistemas auxiliares:
   ```
   SWITCH BATERÍAS → ON
   SWITCH AVIÓNICOS → ON  
   SWITCH FADEC → ON
   ```

2. **Verificar** parámetros iniciales:
   - Voltaje baterías: 24-28V DC
   - Presión tanques H₂: > 50 bar
   - Temperatura celdas: < 30°C

#### Paso 3: Test de Fugas
1. **Conectar** detector de fugas H₂
2. **Verificar** todas las conexiones:
   - Válvulas de tanque
   - Líneas de alimentación  
   - Conexiones de celdas de combustible
3. **Confirmar** lectura < 0.4% LEL

### Fase 2: Inicialización del Sistema

#### Paso 4: Activación FADEC
1. **Presionar** botón FADEC START
2. **Esperar** autotest completo (30 seg aprox.)
3. **Verificar** mensaje "SYSTEM READY" en pantalla

#### Paso 5: Purga del Sistema
1. **Iniciar** secuencia de purga:
   ```
   PURGE SELECTOR → N₂
   PURGE SWITCH → START
   ```
2. **Mantener** purga durante 60 segundos
3. **Verificar** concentración H₂ < 0.1% LEL
4. **Finalizar** purga:
   ```
   PURGE SWITCH → STOP
   PURGE SELECTOR → OFF
   ```

### Fase 3: Arranque del Motor

#### Paso 6: Activación Celdas de Combustible
1. **Abrir** válvulas principales H₂:
   ```
   VÁLVULA TANQUE 1 → OPEN
   VÁLVULA TANQUE 2 → OPEN  
   VÁLVULA PRINCIPAL → OPEN
   ```

2. **Monitorear** parámetros:
   - Presión línea: 8-12 bar
   - Flujo H₂: inicial < 1 kg/h
   - Temperatura celdas: estable

#### Paso 7: Encendido Celdas
1. **Presionar** FUEL CELL START
2. **Observar** secuencia de encendido:
   - Precalentamiento: 30 seg
   - Activación membrana: 45 seg
   - Generación inicial: 15 seg

3. **Verificar** parámetros de salida:
   - Voltaje DC: 750-800V
   - Corriente: < 10A inicialmente
   - Eficiencia: > 85%

#### Paso 8: Arranque Motor Eléctrico
1. **Confirmar** parámetros nominales FC
2. **Presionar** MOTOR START
3. **Acelerar** gradualmente:
   - RPM inicial: 500 rpm
   - Incremento: 100 rpm/10 seg
   - RPM objetivo: 2000 rpm

### Fase 4: Verificaciones Post-Arranque

#### Paso 9: Chequeo de Parámetros
Verificar todos los parámetros dentro de límites normales:

| Parámetro | Límite Normal | Acción si Fuera de Límite |
|-----------|---------------|---------------------------|
| Potencia FC | 0.5-2.5 MW | Verificar carga |
| Presión H₂ | 8-12 bar | Ajustar regulador |
| Temp. celdas | 60-80°C | Verificar enfriamiento |
| RPM motor | 1800-2200 | Ajustar control |
| Vibración | < 2.5 mm/s | Inspeccionar balanceo |

#### Paso 10: Test Funcional
1. **Realizar** variación de potencia:
   - Idle (10%) → 30 seg
   - 50% → 60 seg  
   - 75% → 30 seg
   - Vuelta a idle

2. **Verificar** respuesta del sistema:
   - Tiempo de respuesta < 2 seg
   - Estabilidad de parámetros
   - Ausencia de alarmas

## Criterios de Aceptación

El arranque se considera exitoso cuando:

- ✅ Todas las verificaciones de seguridad completadas
- ✅ Parámetros dentro de límites normales
- ✅ Sistema responde a comandos de potencia
- ✅ Sin alarmas o advertencias activas
- ✅ Test funcional completado satisfactoriamente

## Acciones en Caso de Fallo

### Fallo en Arranque de Celdas
1. **Parar** inmediatamente el procedimiento
2. **Cerrar** válvulas H₂
3. **Iniciar** purga de emergencia
4. **Consultar** FSC correspondiente

### Parámetros Fuera de Límite
1. **Reducir** potencia a idle
2. **Monitorear** 60 segundos
3. **Si persiste**: parada controlada
4. **Registrar** evento en log

### Alarma de Fuga H₂
1. **PARADA INMEDIATA** - Presionar EMERGENCY STOP
2. **Cerrar** válvula principal H₂
3. **Activar** ventilación forzada
4. **Evacuar** área hasta verificación

## Documentación Post-Procedimiento

Completar los siguientes registros:

- [ ] Log de operación con parámetros registrados
- [ ] Reporte de cualquier anomalía observada
- [ ] Firma del técnico certificado
- [ ] Actualización horas de servicio

## Referencias

- FSC-H2-001: Diagnóstico Sistema Hidrógeno
- PRC-EMERG-001: Procedimientos de Emergencia
- MMEL: Lista Mínima de Equipos

---

*Procedimiento aprobado por: Operations Manager*  
*Próxima revisión: 2025-07-16*