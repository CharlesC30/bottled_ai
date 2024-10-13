from typing import List

from rs.common.handlers.common_upgrade_handler import CommonUpgradeHandler
from rs.machine.state import GameState


class UpgradeHandler(CommonUpgradeHandler):

    def __init__(self, high_priority_upgrades: List[str]):
        # super().__init__(priorities=[
        #     'eruption',
        #     'rushdown',
        #     'scrawl',

        # ])
        super().__init__(priorities=[p.lower() for p in high_priority_upgrades])


    def transform_priorities_based_on_game_state(self, priorities: List[str], state: GameState):
        remove_if_snecko = [
            'consecrate',
            'crescendo',
            'eruption',
            'flurry of blows',
            'halt',
            'just lucky',
            'master reality',
            'omniscience',
            'rushdown',
            'scrawl',
            'study',
            'tranquility',
            'vault',
        ]
        safe_remove_if_snecko = []

        if state.has_relic("Snecko Eye"):
            for c in remove_if_snecko:
                if c in priorities:
                    safe_remove_if_snecko.append(c)
            for d in safe_remove_if_snecko:
                priorities.remove(d)

        remove_if_pyramid = [
            'blasphemy',
            'worship',
        ]
        safe_remove_if_pyramid = []

        if state.has_relic("Runic Pyramid"):
            for c in remove_if_pyramid:
                if c in priorities:
                    safe_remove_if_pyramid.append(c)
            for d in safe_remove_if_pyramid:
                priorities.remove(d)
