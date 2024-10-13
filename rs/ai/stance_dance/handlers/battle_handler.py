from dataclasses import dataclass, field

from rs.calculator.executor import get_best_battle_action
from rs.calculator.interfaces.comparator_interface import ComparatorInterface
from rs.common.comparators.big_fight_comparator import BigFightComparator
from rs.common.comparators.common_general_comparator import CommonGeneralComparator
from rs.common.comparators.gremlin_nob_comparator import GremlinNobComparator
from rs.common.comparators.three_sentry_comparator import ThreeSentriesComparator
from rs.common.comparators.three_sentry_turn_1_comparator import ThreeSentriesTurn1Comparator
from rs.common.comparators.transient_comparator import TransientComparator
from rs.common.comparators.waiting_lagavulin_comparator import WaitingLagavulinComparator
from rs.game.card import CardType
from rs.machine.command import Command
from rs.machine.handlers.handler import Handler
from rs.machine.handlers.handler_action import HandlerAction
from rs.machine.state import GameState

from rs.common.handlers.common_battle_handler import BattleHandlerConfig

from rs.helper.logger import log

calm_enablers = ["Inner Peace", "Inner Peace+"]
wrath_enablers = ["Eruption+", "Tantrum", "Tantrum+"]



class BattleHandler(Handler):

    def __init__(self, config: BattleHandlerConfig = BattleHandlerConfig(), max_path_count: int = 11_000):
        self.config: BattleHandlerConfig = config
        self.max_path_count: int = max_path_count

    def can_handle(self, state: GameState) -> bool:
        return state.has_command(Command.PLAY) \
               or state.current_action() == "DiscardAction" \
               or state.current_action() == "ExhaustAction"

    def select_comparator(self, state: GameState) -> ComparatorInterface:
        alive_monsters = len(list(filter(lambda m: not m["is_gone"], state.get_monsters())))

        big_fight = state.floor() in self.config.big_fight_floors

        gremlin_nob_is_present = state.has_monster("Gremlin Nob")

        three_sentries_are_alive_turn_1 = state.has_monster("Sentry") \
                                   and alive_monsters == 3 \
                                   and state.combat_state()['turn'] == 1

        three_sentries_are_alive = state.has_monster("Sentry") \
                                          and alive_monsters == 3

        lagavulin_is_sleeping = state.has_monster("Lagavulin") \
                                and state.combat_state()['turn'] <= 2 \
                                and not state.game_state()['room_type'] == "EventRoom"

        lagavulin_is_worth_delaying = state.deck.contains_type(CardType.POWER) \
                                      or state.deck.contains_cards(["Terror", "Terror+"]) \
                                      or state.deck.contains_cards(["Talk To The Hand", "Talk To The Hand+"]) \
                                      or state.has_relic("Warped Tongs") \
                                      or state.has_relic("Ice Cream")

        transient_is_present = state.has_monster("Transient") and alive_monsters == 1

        if big_fight:
            return self.config.big_fight_comparator()
        elif gremlin_nob_is_present:
            return self.config.gremlin_nob_comparator()
        elif three_sentries_are_alive_turn_1:
            return self.config.three_sentries_turn_1_comparator()
        elif three_sentries_are_alive:
            return self.config.three_sentries_comparator()
        elif lagavulin_is_sleeping and lagavulin_is_worth_delaying:
            return self.config.waiting_lagavulin_comparator()
        elif transient_is_present:
            return self.config.transient_comparator()
        return self.config.general_comparator()
    
    def has_infinite_in_deck(self, state: GameState) -> bool:
        # can add nuance later
        max_deck_size = 5
        if len(state.deck.cards) > max_deck_size:
            return False

        contains_rushdown = state.deck.contains_cards(["Rushdown", "Rushdown+"])

        if state.has_relic("Violet Lotus"):
            calm_enablers.extend(["Vigilance", "Vigilance+"])
        if any([(monster['intent'] == "ATTACK") for monster in state.get_monsters()]):
            calm_enablers.extend(["Fear No Evil", "Fear No Evil+"])
        contains_calm_enabler = state.deck.contains_cards(calm_enablers)

        contains_wrath_enabler = state.deck.contains_cards(wrath_enablers)

        return (contains_rushdown and contains_calm_enabler and contains_wrath_enabler)

    def handle(self, state: GameState) -> HandlerAction:
        if self.has_infinite_in_deck(state):
            log("Infinite present")
        else:
            log("No Infinite")

        actions = get_best_battle_action(state, self.select_comparator(state), self.max_path_count)
        if actions:
            return actions
        if state.has_command(Command.END):
            return HandlerAction(commands=["end"], memory_book=None)
        return HandlerAction(commands=[], memory_book=None)









