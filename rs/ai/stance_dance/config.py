# card id. 'strike+' is an upgraded strike
CARD_REMOVAL_PRIORITY_LIST = [
    'defend',
    'strike',
    'defend+'
    'strike+',
]

# [card display name]: [max amount to have in deck]
DESIRED_CARDS_FOR_DECK: dict[str, int] = {
    'rushdown': 1,
    'scrawl': 2,
    'inner peace': 1,
    'fear no evil': 1,
    'tantrum': 1,
    'empty mind': 1,
    'talk to the hand': 1,
    'mental fortress': 1,
    'meditate': 1,

    # not as sure about these
    'furry of blows': 1,
    'cut through fate': 1,
    'empty fist': 1,
}

# card display name: max amount to have in deck
DESIRED_CARDS_FROM_POTIONS: dict[str, int] = {
    'rushdown': 1,
    'inner peace': 1,
    'fear no evil': 1,
    'scrawl': 1,
    'master of strategy': 1,
}

HIGH_PRIORITY_UPGRADES = [
    'Eruption',
    'Rushdown',
    'Scrawl',
]

DESIRED_POTIONS = [
    'fruit juice',
    'fairy in a bottle',
    'focus potion',
    'cultist potion',
    'power potion',
    'potion of capacity',
    'heart of iron',
    'duplication potion',
    'distilled chaos',
    'blessing of the forge',
    'attack potion',
    'dexterity potion',
    'ambrosia',
    'fear potion',
    'essence of steel',
    'strength potion',
    'regen potion',
    'blood potion',
    'entropic brew',
    'liquid bronze',
    'energy potion',
    'skill potion',
    'ancient potion',
    'weak potion',
    'gambler\u0027s brew',
    'poison potion',
    'colorless potion',
    'flex potion',
    'swift potion',
    'bottled miracle',
    'essence of darkness',
    'fire potion',
    'explosive potion',
    'speed potion',
    'block potion',
    'cunning potion',
    'ghost in a jar',
    'stance potion',
    'smoke bomb',
    'elixir potion',
    'liquid memories',
    'snecko oil',
    'stance potion',
]