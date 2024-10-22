from dataclasses import dataclass, field
import random

from rs.calculator.executor import get_best_battle_action
from rs.calculator.interfaces.comparator_interface import ComparatorInterface
from rs.calculator.interfaces.memory_items import StanceType
from rs.game.card import CardType
from rs.machine.command import Command
from rs.machine.handlers.handler import Handler
from rs.machine.handlers.handler_action import HandlerAction
from rs.machine.state import GameState
from rs.machine.the_bots_memory_book import TheBotsMemoryBook
from rs.calculator.game_state_converter import create_battle_state
from rs.calculator.battle_state import Play

from rs.common.handlers.common_battle_handler import BattleHandlerConfig

from rs.helper.logger import log


# Function 
# get_wrath_enablers(state: GameState) -> List[str]
# get_calm_enablers(state: GameState) -> List[str]
# return appropriate enablers based on state

class InfiniteBattler:
    # def __init__(self, starting_state: GameState) -> None:
    #     self.starting_state = starting_state
    #     self.stance = StanceType.CALM if starting_state.has_relic("Tear Drop Locket") else StanceType.NO_STANCE
    def __init__(self) -> None:
        self.stance = None

    def battle(self, state: GameState) -> Play:
        played_rushdown = "rushdown" in [power['name'].lower() for power in state.get_player_combat()["powers"]]
        all_cards_in_hand = (len(state.discard_pile.cards) == 0) and (len(state.draw_pile.cards) == 0)
        cards_in_hand = [card.name for card in state.hand.cards]
        if played_rushdown and all_cards_in_hand:
            if self.stance is not StanceType.CALM:
                # Find 'best' calm enabler and play
                if "Inner Peace" in cards_in_hand:
                    enabler = "Inner Peace"
                elif "Inner Peace+" in cards_in_hand:
                    enabler = "Inner Peace+"
                elif any([("ATTACK" in monster['intent']) for monster in state.get_monsters()]):
                    if "Fear No Evil" in cards_in_hand:
                        enabler = "Fear No Evil"
                    elif "Fear No Evil+" in cards_in_hand:
                        enabler = "Fear No Evil+"
                elif state.has_relic("Violet Lotus") and state.get_player_combat()["energy"] > 2:
                    if "Vigilance" in cards_in_hand:
                        enabler = "Vigilance"
                    elif "Vigilance+" in cards_in_hand:
                        enabler = "Vigilance+"

                self.stance = StanceType.CALM
                card_index = state.hand.get_card_index_from_name(enabler)
                if enabler == "Fear No Evil" or enabler == "Fear No Evil+":
                    # find the index of first attacking monster
                    monster_intents = [monster["intent"] for monster in state.get_monsters()]
                    target_index = next((i for i, intent in enumerate(monster_intents) if "ATTACK" in intent), None)
                    return (card_index, target_index)
                return (card_index, -1)
            
        elif played_rushdown and self.stance is StanceType.CALM:
            # Find and play wrath enabler 
            if "Eruption+" in cards_in_hand:
                enabler = "Eruption+"
            elif "Tantrum" in cards_in_hand:
                enabler = "Tantrum"
            elif "Tantrum+" in cards_in_hand:
                enabler = "Tantrum+"

            self.stance = StanceType.WRATH
            card_index = state.hand.get_card_index_from_name(enabler)
            target_index = random.randint(0, len([monster for monster in state.get_monsters() if not monster["is_gone"]]) - 1)
            return (card_index, target_index)
        
        elif "Rushdown" in cards_in_hand:
            card_index = state.hand.get_card_index_from_name("Rushdown")
            return (card_index, -1)
        
        elif "Rushdown+" in cards_in_hand:
            card_index = state.hand.get_card_index_from_name("Rushdown+")
            return (card_index, -1)
        
        else:
            return None


class BattleHandler(Handler):

    def __init__(self, config: BattleHandlerConfig = BattleHandlerConfig(), max_path_count: int = 11_000):
        self.config: BattleHandlerConfig = config
        self.max_path_count: int = max_path_count
        self.infinite_battler = InfiniteBattler()
        self.in_infinite = False

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
        calm_enablers = ["Inner Peace", "Inner Peace+"]
        wrath_enablers = ["Eruption+", "Tantrum", "Tantrum+"]

        if len(state.deck.cards) > max_deck_size:
            return False

        contains_rushdown = state.deck.contains_cards(["Rushdown", "Rushdown+"])

        if state.has_relic("Violet Lotus"):
            calm_enablers.extend(["Vigilance", "Vigilance+"])
        if any([("ATTACK" in monster['intent']) for monster in state.get_monsters()]):
            calm_enablers.extend(["Fear No Evil", "Fear No Evil+"])
        contains_calm_enabler = state.deck.contains_cards(calm_enablers)

        contains_wrath_enabler = state.deck.contains_cards(wrath_enablers)

        return (contains_rushdown and contains_calm_enabler and contains_wrath_enabler)

    def handle(self, state: GameState) -> HandlerAction:
        if self.has_infinite_in_deck(state):
            if not self.in_infinite:
                log("Starting Infinite")
                self.in_infinite = True
                self.infinite_battler.stance = StanceType.CALM if state.has_relic("Tear Drop Locket") else StanceType.NO_STANCE
            next_move = self.infinite_battler.battle(state)

            # create a temp state for finding the state of the custom state after the chosen action
            _state = create_battle_state(state)
            _state.transform_from_play(next_move, is_first_play=False)  # not sure if it's ok that I'm setting that false
            memory_book = TheBotsMemoryBook(memory_by_card=_state.memory_by_card.copy(), memory_general=_state.memory_general.copy())
            if next_move[1] == -1:
                return HandlerAction(commands=[f"play {next_move[0] + 1}"], memory_book=memory_book)
            return HandlerAction(commands=[f"play {next_move[0] + 1} {next_move[1]}"], memory_book=memory_book)

        actions = get_best_battle_action(state, self.select_comparator(state), self.max_path_count)
        if actions:
            for command in actions.commands:
                log(command)
            return actions
        if state.has_command(Command.END):
            self.in_infinite = False
            return HandlerAction(commands=["end"], memory_book=None)
        return HandlerAction(commands=[], memory_book=None)









