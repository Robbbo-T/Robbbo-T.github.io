#!/usr/bin/env python3
'''
TEKNIA Aggregation Engine
Aggregates TEKTOKs into portfolios with Net Value calculation
'''

import json
from pathlib import Path
import numpy as np

class AggregationEngine:
    def __init__(self):
        self.tektoks = []
        self.synergy_matrix = {}
        
    def load_tektoks(self, directory):
        '''Load all TEKTOKs from directory'''
        for tektok_file in Path(directory).glob('TEKTOK-*.json'):
            # Skip anchored files to avoid duplicates
            if '_anchored' not in str(tektok_file):
                with open(tektok_file, 'r') as f:
                    data = json.load(f)
                    self.tektoks.append(data['tektok'])
        print(f"Loaded {len(self.tektoks)} TEKTOKs")
    
    def calculate_portfolio_value(self, tektok_ids=None):
        '''Calculate aggregated Net Value for portfolio'''
        if tektok_ids:
            portfolio = [t for t in self.tektoks if t['id'] in tektok_ids]
        else:
            portfolio = self.tektoks
        
        if not portfolio:
            return 0
        
        # Base aggregation: weighted average
        scores = [t['net_value']['score'] for t in portfolio]
        base_value = np.mean(scores)
        
        # Apply synergy bonus (simplified)
        synergy_bonus = self._calculate_synergy(portfolio)
        
        # Apply diversification factor
        diversity_factor = self._calculate_diversity(portfolio)
        
        # Final portfolio value
        portfolio_value = base_value * (1 + synergy_bonus) * diversity_factor
        
        return min(portfolio_value, 1.0)  # Cap at 1.0
    
    def _calculate_synergy(self, portfolio):
        '''Calculate synergy bonus between TEKTOKs'''
        # Simplified: TEKTOKs in same domain have 10% synergy
        domains = [t['domain'] for t in portfolio]
        domain_counts = {}
        for d in domains:
            domain_counts[d] = domain_counts.get(d, 0) + 1
        
        synergy = 0
        for count in domain_counts.values():
            if count > 1:
                synergy += 0.1 * (count - 1) / len(portfolio)
        
        return min(synergy, 0.3)  # Cap synergy at 30%
    
    def _calculate_diversity(self, portfolio):
        '''Calculate diversity factor'''
        domains = set([t['domain'] for t in portfolio])
        diversity = len(domains) / max(len(portfolio), 1)
        return 0.8 + 0.2 * diversity  # 80% base + up to 20% for diversity
    
    def generate_portfolio_report(self, name="TEKNIA Portfolio"):
        '''Generate portfolio report'''
        portfolio_value = self.calculate_portfolio_value()
        
        report = {
            'portfolio': {
                'name': name,
                'tektok_count': len(self.tektoks),
                'domains': list(set([t['domain'] for t in self.tektoks])),
                'total_net_value': portfolio_value,
                'tektoks': [
                    {
                        'id': t['id'],
                        'title': t['title'],
                        'domain': t['domain'],
                        'score': t['net_value']['score']
                    }
                    for t in self.tektoks
                ],
                'metrics': {
                    'avg_trl': np.mean([
                        t['net_value']['inputs'].get('trl', 5) 
                        for t in self.tektoks 
                        if 'inputs' in t['net_value']
                    ]),
                    'avg_quality': np.mean([
                        t['net_value']['inputs'].get('quality', 0.5)
                        for t in self.tektoks
                        if 'inputs' in t['net_value']
                    ])
                }
            }
        }
        
        return report

def main():
    engine = AggregationEngine()
    engine.load_tektoks('tektoks/samples')
    
    report = engine.generate_portfolio_report("AQUA H2-BWB Portfolio")
    
    # Save report
    with open('tektoks/portfolio_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nPortfolio Report Generated:")
    print(f"  Total TEKTOKs: {report['portfolio']['tektok_count']}")
    print(f"  Portfolio Net Value: {report['portfolio']['total_net_value']:.3f}")
    print(f"  Domains: {', '.join(report['portfolio']['domains'])}")

if __name__ == '__main__':
    main()