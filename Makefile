# TEKNIA R1 Makefile
# Convenience commands for TEKNIA operations

.PHONY: install validate anchor aggregate test clean all help

# Default target
all: validate anchor aggregate

# Install Python dependencies
install:
	@echo "Installing TEKNIA dependencies..."
	pip install jsonschema numpy pyyaml

# Validate all TEKTOKs
validate:
	@echo "Validating TEKTOKs..."
	python3 scripts/validate_tektoks.py

# Generate CDTL anchors
anchor:
	@echo "Generating CDTL anchors..."
	python3 scripts/cdtl_anchor.py

# Generate portfolio report
aggregate:
	@echo "Generating portfolio aggregation..."
	python3 scripts/aggregation_engine.py

# Run complete test suite
test: validate anchor aggregate
	@echo "All tests passed! ✓"
	@echo "Portfolio report generated at: tektoks/portfolio_report.json"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -f tektoks/samples/*_anchored.json
	rm -f tektoks/portfolio_report.json

# Show project status
status:
	@echo "TEKNIA R1 Status:"
	@echo "=================="
	@echo "TEKTOKs: $(shell ls tektoks/samples/TEKTOK-*.json 2>/dev/null | grep -v _anchored | wc -l)"
	@echo "Schemas: $(shell ls schemas/*.json 2>/dev/null | wc -l)"
	@echo "Scripts: $(shell ls scripts/*.py 2>/dev/null | wc -l)"
	@echo ""
	@if [ -f tektoks/portfolio_report.json ]; then \
		echo "Portfolio Report: Available"; \
		echo "Net Value: $(shell python3 -c "import json; print(json.load(open('tektoks/portfolio_report.json'))['portfolio']['total_net_value'])" 2>/dev/null || echo 'N/A')"; \
	else \
		echo "Portfolio Report: Not generated (run 'make aggregate')"; \
	fi

# Show help
help:
	@echo "TEKNIA R1 - Available Commands:"
	@echo "=============================="
	@echo "install    - Install Python dependencies"
	@echo "validate   - Validate all TEKTOK files"
	@echo "anchor     - Generate CDTL blockchain anchors"
	@echo "aggregate  - Generate portfolio report"
	@echo "test       - Run complete validation suite"
	@echo "status     - Show project status"
	@echo "clean      - Remove generated files"
	@echo "all        - Run validate + anchor + aggregate"
	@echo "help       - Show this help message"