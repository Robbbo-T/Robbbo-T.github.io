# TEKNIA R1 - Technology Export Knowing Net Value Into Aggregation

## 🎯 Overview

TEKNIA is the economic-technical grammar that converts **verifiable knowledge** into **aggregable net value** through **TEKTOKs** (minimal technical value notes) sealed on **CDTL** blockchain and traced with reproducible evidence (DET/S1000D-Q).

## 📋 Quick Start

```bash
# Validate all TEKTOKs
python scripts/validate_tektoks.py

# Generate CDTL anchors
python scripts/cdtl_anchor.py

# Create portfolio report
python scripts/aggregation_engine.py
```

## 🏗️ Repository Structure

```
TEKNIA_R1/
├── docs/
│   └── TEKNIA/
│       └── TEKNIA-Manifesto.md      # Core principles and definitions
├── schemas/
│   └── tektok.schema.json           # JSON Schema for TEKTOKs
├── tektoks/
│   ├── samples/                     # Example TEKTOKs
│   └── portfolio_report.json        # Aggregated portfolio analysis
├── scripts/
│   ├── validate_tektoks.py          # Schema and business rule validator
│   ├── cdtl_anchor.py               # CDTL blockchain anchor generator
│   └── aggregation_engine.py        # Portfolio aggregation engine
├── .github/
│   └── workflows/
│       └── teknia-ci.yml            # CI/CD pipeline
└── TEKNIA-README.md                 # This file
```

## 🔑 Key Concepts

### TEKTOK
Atomic unit of technical knowledge with:
- **Verifiable evidence** (DET references)
- **Net Value score** (0.0 to 1.0)
- **CDTL anchor** (blockchain proof)
- **Traceability** (S1000D-Q links)

### Net Value
Anti-bubble metric combining:
- Technology Readiness Level (TRL)
- Quality metrics
- Energy savings
- CO2 reduction
- Market readiness
- Risk discount

### Aggregation
TEKTOKs aggregate into:
- **Projects**: Coherent sets toward objectives
- **Portfolios**: Multiple projects with synergies
- **IPO-pre-genesis**: Valuation based on aggregated Net Value

## 📊 Example TEKTOKs

### BWB Architecture (AAA Domain)
- **ID**: TEKTOK-AAA-bwb-arch-0001
- **Net Value**: 0.72
- **TRL**: 7
- **Energy Savings**: 15%

### Zero Boil-off Tank (CQH Domain)
- **ID**: TEKTOK-CQH-cryo-tank-0042
- **Net Value**: 0.68
- **TRL**: 6
- **Energy Savings**: 25%

### Quantum-Safe Encryption (DDD Domain)
- **ID**: TEKTOK-DDD-cyber-sec-0003
- **Net Value**: 0.83
- **TRL**: 8
- **Market Readiness**: 80%

## 🔗 Integration Points

### AMPEL360
- TEKTOKs → RIE360 Events
- Net Value → ARIA Dashboards
- CDTL anchors → QAUDIT

### S1000D-Q
- CE references in TEKTOKs
- Data Module links
- Effectivity tracking

### CDTL Blockchain
- Hash-only anchoring
- Immutable evidence chain
- Timestamp verification

## 🛡️ Validation

All TEKTOKs must pass:
1. **Schema validation** (JSON Schema)
2. **Business rules** (Net Value bounds, hash format)
3. **CDTL anchoring** (blockchain proof)
4. **Traceability check** (DET/S1000D links)

## 📈 Metrics

Current portfolio metrics:
- Total TEKTOKs: 3
- Domains covered: AAA, CQH, DDD
- Average Net Value: 0.74
- Average TRL: 7

## 🚀 Roadmap

### R1 (Current)
- ✅ TEKTOK schema definition
- ✅ Validation engine
- ✅ CDTL anchor generation
- ✅ Basic aggregation

### R2 (Q2 2025)
- Portfolio optimization algorithms
- Advanced synergy calculations
- Real CDTL deployment
- RIE360 live integration

### R3 (Q3 2025)
- Tokenomics model
- Incentive mechanisms
- Marketplace features
- IPO-pre-genesis tools

## 📜 License

Apache 2.0 for open components. See individual TEKTOKs for specific licensing.

## 🤝 Contributing

1. Create TEKTOK following schema
2. Add evidence (DET references)
3. Calculate Net Value
4. Submit PR with validation passing

## 📞 Contact

- **Technical**: teknia@aqua-framework.org
- **Business**: ventures@aqua-framework.org
- **CDTL**: blockchain@aqua-framework.org

---

*TEKNIA R1 - Part of the AQUA Framework for H2-BWB-Q100 Program*