from rs.ai.stance_dance.handlers.battle_handler import BattleHandler
from tests.test_helpers.resources import load_resource_state

def test_finding_infinite_in_deck():
    handler = BattleHandler()
    state = load_resource_state("battles/stances/simple_infinite.json")
    assert handler.has_infinite_in_deck(state), "Failed check for infinite test"