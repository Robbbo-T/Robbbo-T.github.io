#!/usr/bin/env python3
'''
CDTL Anchor Generator for TEKTOKs
Generates and verifies CDTL blockchain anchors
'''

import json
import hashlib
import time
from pathlib import Path

class CDTLAnchor:
    def __init__(self, network='cdtl-main-sandbox'):
        self.network = network
        self.chain_height = 0
        
    def compute_tektok_hash(self, tektok_data):
        '''Compute canonical hash of TEKTOK'''
        # Serialize in canonical form
        canonical = json.dumps(tektok_data, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(canonical.encode()).hexdigest()
    
    def create_anchor(self, tektok_file):
        '''Create CDTL anchor for TEKTOK'''
        with open(tektok_file, 'r') as f:
            tektok_data = json.load(f)
        
        # Compute hash
        tektok_hash = self.compute_tektok_hash(tektok_data)
        
        # Simulate blockchain transaction
        tx_id = f"0x{hashlib.sha256(f'{tektok_hash}{time.time()}'.encode()).hexdigest()[:16]}"
        block_hash = f"0x{hashlib.sha256(f'block{self.chain_height}'.encode()).hexdigest()[:16]}"
        
        anchor = {
            'network': self.network,
            'tx_id': tx_id,
            'block_hash': block_hash,
            'height': self.chain_height,
            'tektok_hash': tektok_hash,
            'timestamp': int(time.time())
        }
        
        self.chain_height += 1
        
        # Update TEKTOK with anchor
        tektok_data['tektok']['evidence'] = tektok_data['tektok'].get('evidence', {})
        tektok_data['tektok']['evidence']['sha256'] = tektok_hash
        tektok_data['tektok']['evidence']['cdtl_anchor'] = anchor
        
        # Save updated TEKTOK
        anchor_file = tektok_file.parent / f'{tektok_file.stem}_anchored.json'
        with open(anchor_file, 'w') as f:
            json.dump(tektok_data, f, indent=2)
        
        print(f"✓ CDTL anchor created for {tektok_file.name}")
        print(f"  Hash: {tektok_hash}")
        print(f"  TX: {tx_id}")
        print(f"  Block: {block_hash} (height: {self.chain_height - 1})")
        
        return anchor

def main():
    anchor_service = CDTLAnchor()
    tektok_dir = Path('tektoks/samples')
    
    for tektok_file in tektok_dir.glob('TEKTOK-*.json'):
        if '_anchored' not in str(tektok_file):
            anchor_service.create_anchor(tektok_file)

if __name__ == '__main__':
    main()