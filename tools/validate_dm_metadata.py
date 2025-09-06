#!/usr/bin/env python3
"""
S1000D Data Module Metadata Validator
Validates Data Module .md files with S1000D front-matter against schema
"""

import json
import yaml
import jsonschema
import sys
import re
from pathlib import Path
from datetime import datetime

def extract_frontmatter(md_file):
    """Extract YAML front-matter from markdown file"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match front-matter between --- delimiters
        pattern = r'^---\n(.*?)\n---'
        match = re.match(pattern, content, re.DOTALL)
        
        if not match:
            return None
            
        frontmatter_yaml = match.group(1)
        return yaml.safe_load(frontmatter_yaml)
        
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return None

def validate_utcs_mi_v5(utcs_id):
    """Validate UTCS-MI v5.0 13-field structure"""
    fields = utcs_id.split(':')
    if len(fields) != 13:
        return False, f"Expected 13 fields, got {len(fields)}"
    
    field_names = [
        "Estándar", "Tipo", "Dominio", "VersionEsquema", 
        "CategoriaInfo", "Secuencial", "VersionContenido", 
        "Proyecto", "Generacion", "Clasificacion", 
        "Organizacion", "Hash", "CicloVida"
    ]
    
    # Basic validation for each field
    validations = []
    for i, (name, value) in enumerate(zip(field_names, fields)):
        if not value.strip():
            validations.append(f"Field {i+1} ({name}) is empty")
    
    return len(validations) == 0, validations

def validate_dmc(dmc):
    """Validate Data Module Code structure"""
    pattern = r'^DMC-[A-Z0-9]{2,5}-[A-Z]-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{3}[A-Z]-[0-9]{3}[A-Z]-[A-Z]$'
    if not re.match(pattern, dmc):
        return False, f"DMC does not match S1000D pattern: {dmc}"
    return True, None

def validate_dm_metadata(md_file, schema_file):
    """Validate a Data Module markdown file against S1000D schema"""
    print(f"\n📄 Validating: {md_file}")
    
    # Extract front-matter
    frontmatter = extract_frontmatter(md_file)
    if not frontmatter:
        print(f"  ❌ No valid YAML front-matter found")
        return False
    
    # Load schema
    try:
        with open(schema_file, 'r') as f:
            schema = json.load(f)
    except Exception as e:
        print(f"  ❌ Error loading schema: {e}")
        return False
    
    # Validate against JSON schema
    try:
        jsonschema.validate(frontmatter, schema)
        print(f"  ✅ Schema validation passed")
    except jsonschema.exceptions.ValidationError as e:
        print(f"  ❌ Schema validation failed:")
        print(f"     {e.message}")
        return False
    
    # Additional S1000D-specific validations
    
    # Validate UTCS-MI v5.0 structure
    if 'utcs_mi_v5_id' in frontmatter:
        is_valid, errors = validate_utcs_mi_v5(frontmatter['utcs_mi_v5_id'])
        if not is_valid:
            print(f"  ❌ UTCS-MI v5.0 validation failed:")
            for error in errors:
                print(f"     {error}")
            return False
        else:
            print(f"  ✅ UTCS-MI v5.0 structure valid (13 fields)")
    
    # Validate DMC structure
    if 's1000d' in frontmatter and 'dmc' in frontmatter['s1000d']:
        dmc = frontmatter['s1000d']['dmc']
        is_valid, error = validate_dmc(dmc)
        if not is_valid:
            print(f"  ❌ DMC validation failed: {error}")
            return False
        else:
            print(f"  ✅ DMC structure valid: {dmc}")
    
    # Check consistency between UTCS-MI and S1000D fields
    if 'utcs_mi_v5_id' in frontmatter and 's1000d' in frontmatter:
        utcs_fields = frontmatter['utcs_mi_v5_id'].split(':')
        s1000d = frontmatter['s1000d']
        
        # Check if domain matches
        if len(utcs_fields) >= 3 and 'S1000D' in utcs_fields[2]:
            print(f"  ✅ UTCS-MI domain indicates S1000D compliance")
        
        # Check version consistency
        if len(utcs_fields) >= 4 and 'schema_version' in s1000d:
            print(f"  ✅ Schema versions referenced in both UTCS-MI and S1000D")
    
    print(f"  ✅ All validations passed for {md_file.name}")
    return True

def scan_data_modules(docs_dir, schema_file):
    """Scan all .md files in docs directory for S1000D Data Modules"""
    md_files = []
    
    # Look for .md files with S1000D front-matter
    for md_file in Path(docs_dir).rglob('*.md'):
        # Skip index files and certain directories
        if md_file.name in ['index.md', 'README.md']:
            continue
            
        # Check if file has S1000D front-matter
        frontmatter = extract_frontmatter(md_file)
        if frontmatter and ('s1000d' in frontmatter or 'utcs_mi_v5_id' in frontmatter):
            md_files.append(md_file)
    
    return md_files

def main():
    """Main validation routine"""
    print("🔍 S1000D Data Module Metadata Validator")
    print("=" * 50)
    
    # Default paths
    docs_dir = Path('docs')
    schema_file = Path('docs/90-anexos/esquemas/s1000d_dm_meta.schema.json')
    
    # Check if schema exists
    if not schema_file.exists():
        print(f"❌ Schema file not found: {schema_file}")
        print("   Please ensure the S1000D metadata schema is in place.")
        sys.exit(1)
    
    # Scan for Data Module files
    dm_files = scan_data_modules(docs_dir, schema_file)
    
    if not dm_files:
        print("📝 No Data Module files found with S1000D front-matter")
        print("   Files should contain either 's1000d' or 'utcs_mi_v5_id' in YAML front-matter")
        return
    
    print(f"📋 Found {len(dm_files)} Data Module files to validate")
    
    # Validate each file
    all_valid = True
    valid_count = 0
    
    for dm_file in dm_files:
        if validate_dm_metadata(dm_file, schema_file):
            valid_count += 1
        else:
            all_valid = False
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print(f"   Total files: {len(dm_files)}")
    print(f"   Valid files: {valid_count}")
    print(f"   Invalid files: {len(dm_files) - valid_count}")
    
    if all_valid:
        print("✅ All Data Module validations passed!")
        sys.exit(0)
    else:
        print("❌ Some Data Module validations failed!")
        sys.exit(1)

if __name__ == '__main__':
    main()