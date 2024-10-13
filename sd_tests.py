from rs.ai.stance_dance.handlers.battle_handler import BattleHandler
from rs.ai.stance_dance.handlers.resources import load_resource_state

if __name__ == "__main__":
    handler = BattleHandler()
    state = load_resource_state("C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\misc\simple_infinite.json")
    print([card.name for card in state.deck.cards])
    print(state.deck.contains_card_amount("Rushdown"))
    print(state.deck.contains_card_amount("Rushdown+"))
    print(handler.has_infinite_in_deck(state))