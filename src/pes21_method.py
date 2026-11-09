"""Cálculo editorial reproduzível. NÃO calcula o OVR do motor PES.

Uso:
    python -m src.pes21_method validate
    python -m src.pes21_method evaluate examples/garnacho.json [--json]
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATTRIBUTES = (
    'attacking_prowess', 'ball_control', 'dribbling', 'tight_possession',
    'low_pass', 'lofted_pass', 'finishing', 'heading', 'set_piece_taking',
    'curl', 'speed', 'acceleration', 'kicking_power', 'jump',
    'physical_contact', 'balance', 'stamina', 'defensive_awareness',
    'ball_winning', 'aggression', 'gk_awareness', 'gk_catching',
    'gk_clearing', 'gk_reflexes', 'gk_reach',
)

def load_json(path: Path):
    with path.open('r', encoding='utf-8') as stream:
        return json.load(stream)

def validate_record(record: dict, criteria: dict) -> dict:
    if record['method_version'] != criteria['version']:
        raise ValueError('method_version incompatível')
    if record['record_status'] != 'PROVISIONAL_EXPERT_ESTIMATE':
        raise ValueError('Exemplos precisam ser explicitamente provisórios')
    if record['overall_game_verified'] is not None:
        raise ValueError('Overall in-game requer evidência externa de validação')
    if set(record['attributes']) != set(ATTRIBUTES):
        raise ValueError('A ficha não contém exatamente os 25 atributos PES')
    for name,value in record['attributes'].items():
        if not isinstance(value,int) or isinstance(value,bool) or not 40<=value<=99:
            raise ValueError(f'{name} fora da escala operacional provisória [40, 99]')
    specials = record['other_pes_settings']
    for field,minv,maxv in [('weak_foot_usage',1,4),('weak_foot_accuracy',1,4),('form',1,8),('injury_resistance',1,3)]:
        v=specials[field]
        if not isinstance(v,int) or isinstance(v,bool) or not minv<=v<=maxv:
            raise ValueError(f'Característica inválida {field}={v}')
    catalog=load_json(ROOT/'config/pes21-skills.json')
    valid_skills={x['en'] for x in catalog['player_skills']}
    suggested=specials['special_skills_proposed']
    if len(suggested)!=len(set(suggested)) or any(x not in valid_skills for x in suggested):
        raise ValueError('Habilidade especial proposta sem correspondência no catálogo PES 2021')
    for pending in specials.get('skills_pending_mapping',[]):
        if not isinstance(pending,str) or not pending.strip():
            raise ValueError('Pendência de mapeamento inválida')
    for field in ('carrying','low_pass','lofted_pass'):
        v=specials['inspiration'][field]
        if not isinstance(v,int) or isinstance(v,bool) or not 0<=v<=2:
            raise ValueError(f'inspiration.{field} fora da escala UI da liga')
    if set(record['dimensions']) != set(criteria['weights']):
        raise ValueError('As quatro dimensões não coincidem')
    index=Decimal('0')
    for name,weight in criteria['weights'].items():
        dim=record['dimensions'][name]
        value=dim['score']
        if not isinstance(value,(int,float)) or isinstance(value,bool) or not 0<=value<=100:
            raise ValueError(f'Dimensão fora de 0-100: {name}')
        if dim['provenance'] != 'expert_estimate':
            raise ValueError(f'{name} não pode ser rotulado como fórmula automática sem calibração')
        index += Decimal(str(value))*Decimal(str(weight))
    if sum(Decimal(str(x)) for x in criteria['weights'].values()) != Decimal('1.00'):
        raise ValueError('Pesos não somam 1')
    rounded=int(index.quantize(Decimal('1'),rounding=ROUND_HALF_UP))
    if rounded != record['expected_index_rounded'] or rounded != record['overall_target']:
        raise ValueError('Overall-alvo divergente do índice ponderado')
    # Valores adotados pela liga NÃO alteram o índice editorial da metodologia.
    assignment = record.get('league_assignment')
    if assignment is not None:
        if assignment.get('source') != 'explicit_league_decision_reported_by_user':
            raise ValueError('Decisão da liga sem proveniência explícita')
        if assignment.get('game_verified') is not False:
            raise ValueError('Decisão da liga não comprova o Overall do motor PES')
        if assignment.get('dribbling') != record['attributes']['dribbling']:
            raise ValueError('Drible adotado pela liga diverge da ficha')
        adopted = assignment.get('overall')
        if not isinstance(adopted,int) or isinstance(adopted,bool) or not 40 <= adopted <= 99:
            raise ValueError('Overall da liga fora da escala')
    for season in record['season_evidence']:
        if season['scope'] not in ('domestic_league','club_all_competitions'):
            raise ValueError('Escopo de temporada inválido')
        if season['source_key'] not in record['evidence_urls']:
            raise ValueError('Fonte não informada para temporada')
    tier=next((x['label'] for x in criteria['tier_table'] if x['minimum']<=rounded<=x['maximum']),None)
    if tier is None:
        tier='Fora da calibração'
    return {'player':record['player']['name'],'index':float(index), 'overall_target':rounded,
            'tier':tier, 'confidence':record['confidence'],
            'overall_game_verified':record['overall_game_verified'],
            'league_assigned_overall': assignment['overall'] if assignment else None,
            'league_assigned_dribbling': assignment['dribbling'] if assignment else None,
            'calibrated':False,'method_version':criteria['version']}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    ev=sub.add_parser('evaluate')
    ev.add_argument('file',type=Path)
    ev.add_argument('--json',action='store_true')
    opts=ap.parse_args()
    cfg=load_json(ROOT/'config/criteria.v1.json')
    if opts.command=='validate':
        for path in sorted((ROOT/'examples').glob('*.json')):
            out=validate_record(load_json(path),cfg)
            print(f"OK {path.name} — índice {out['index']:.2f}; OVR-alvo {out['overall_target']}")
        print('OK: fichas completas, pesos, escopos e cálculo editorial. NÃO valida PES in-game.')
    elif opts.command=='evaluate':
        obj=validate_record(load_json(opts.file),cfg)
        if opts.json:
            print(json.dumps(obj,ensure_ascii=False,indent=2))
        else:
            print(f"{obj['player']} | índice: {obj['index']:.2f} | OVR-alvo: {obj['overall_target']} "
                  f"({obj['tier']}) | confiança: {obj['confidence']} | PES: não verificado")

if __name__=='__main__':
    main()
