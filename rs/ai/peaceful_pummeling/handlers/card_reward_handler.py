from rs.common.handlers.card_reward.common_card_reward_handler import CommonCardRewardHandler
from rs.machine.state import GameState


class CardRewardHandler(CommonCardRewardHandler):

    def __init__(self):
        super().__init__(
            cards_desired_for_deck={
                'blasphemy': 1,
                'talk to the hand': 3,
                'rushdown': 1,
                'tantrum': 2,
                'battle hymn': 1,
                'mental fortress': 2,
                'tranquility': 2,
                'wallop': 2,
                'flurry of blows': 2,
                'empty body': 2,
                'indignation': 1,
                'crush joints': 1,
                'fear no evil': 2,
                'empty fist': 1,
                'reach heaven': 1,
                'inner peace': 1,
                'cut through fate': 1,
                'crescendo': 1,
                'halt': 1,  # removed if snecko
                'deceive reality': 1,
                'carve reality': 1,
                'spirit shield': 1,
                'sands of time': 1,
                'ragnarok': 1,
                'perseverance': 2,
                'wheel kick': 1,
                'like water': 1,
                'follow up': 1,
            }, cards_desired_from_potions={
                'apotheosis': 1,
                'mental fortress': 5,
                'master of strategy': 3,
                'wish': 2,
                'deva form': 2,
                'like water': 3,
                'devotion': 2,
                'rushdown': 3,
                'master reality': 1,
                'establishment': 2,
                'talk to the hand': 7,
                'scrawl': 1,
                'lesson learned': 1,
                'dark shackles': 2,
                'panache': 3,
                'panacea': 3,
                'deus ex machina': 1,
                'bandage up': 3,
                'dramatic entrance': 3,
                'trip': 1,
                'blind': 1,
                'enlightenment': 2,
                'hand of greed': 2,
                'sadistic nature': 2,

            }
        )

    def transform_desired_cards_map_from_state(self, cards: dict[str, int], state: GameState):
        if state.has_relic("Snecko Eye"):
            del cards['halt']
