#!/usr/bin/env python3
'''
TEKNIA TEKTOK Validator
Validates TEKTOK files against schema and business rules
'''

import json
import jsonschema
import hashlib
import sys
from pathlib import Path

def validate_tektok(tektok_file, schema_file):
    '''Validate a TEKTOK file against schema'''
    
    # Load schema
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    
    # Load TEKTOK
    with open(tektok_file, 'r') as f:
        tektok_data = json.load(f)
    
    # Validate against schema
    try:
        jsonschema.validate(tektok_data, schema)
        print(f"✓ Schema validation passed for {tektok_file}")
    except jsonschema.exceptions.ValidationError as e:
        print(f"✗ Schema validation failed for {tektok_file}")
        print(f"  Error: {e.message}")
        return False
    
    # Additional business rules
    tektok = tektok_data['tektok']
    
    # Check Net Value calculation
    if 'inputs' in tektok['net_value']:
        inputs = tektok['net_value']['inputs']
        score = tektok['net_value']['score']
        
        # Simple validation: score should be between 0 and 1
        if not (0 <= score <= 1):
            print(f"✗ Net Value score out of range: {score}")
            return False
    
    # Check hash if provided
    if 'evidence' in tektok and 'sha256' in tektok['evidence']:
        hash_value = tektok['evidence']['sha256']
        if len(hash_value) != 64:
            print(f"✗ Invalid SHA256 hash length: {len(hash_value)}")
            return False
    
    print(f"✓ Business rules validation passed for {tektok_file}")
    return True

def main():
    schema_file = Path('schemas/tektok.schema.json')
    tektok_dir = Path('tektoks/samples')
    
    if not schema_file.exists():
        print(f"Schema file not found: {schema_file}")
        sys.exit(1)
    
    # Validate all TEKTOK files
    all_valid = True
    for tektok_file in tektok_dir.glob('*.json'):
        if not validate_tektok(tektok_file, schema_file):
            all_valid = False
    
    if all_valid:
        print("\n✓ All TEKTOK validations passed")
        sys.exit(0)
    else:
        print("\n✗ Some TEKTOK validations failed")
        sys.exit(1)

if __name__ == '__main__':
    main()