from enum import Enum


class PowerId(Enum):
    FAKE = 'fake'  # for unknown powers
    FAKE_ALPHA_BETA = 'fake_alpha_beta'  # hack for valuing playing these cards

    AMPLIFY = 'amplify'
    ANGER_NOB = 'anger'  # Non-standard naming to distinguish it from Angry
    ANGRY = 'angry'
    ACCURACY = 'accuracy'
    AFTER_IMAGE = 'after image'
    ARTIFACT = 'artifact'
    BARRICADE = 'barricade'
    BATTLE_HYMN = 'battlehymn'
    BIAS = 'bias'
    BERSERK = 'berserk'
    BLASPHEMER = 'endturndeath'
    BLOCK_RETURN = 'blockreturnpower'
    BLUR = 'blur'
    BUFFER = 'buffer'
    BURST = 'burst'
    CHOKED = 'choked'
    COLLECT = 'collect'
    CONFUSED = 'confusion'  # Bot takes the new costs into account
    CONSTRICTED = 'constricted'
    CORPSE_EXPLOSION = 'corpse explosion'
    CORRUPTION = 'corruption'
    CREATIVE_AI = 'creative ai'
    CURIOSITY = 'curiosity'
    CURL_UP = 'curl up'
    DARK_EMBRACE = 'dark embrace'
    DEMON_FORM = 'demon form'
    DEVA = 'devaform'
    DEVOTION = 'devotionpower'
    DEXTERITY = 'dexterity'
    DOUBLE_DAMAGE = 'double damage'
    DOUBLE_TAP = 'double tap'
    DRAW_CARD = 'draw card'  # It affects a future turn though, so we mostly don't do anything with it.
    DRAW_REDUCTION = 'draw reduction'  # It affects a future turn though, so we mostly don't do anything with it.
    DUPLICATION_POTION_POWER = 'duplicationpower'
    ECHO_FORM = 'echo form'
    ELECTRO = 'electro'
    ENERGIZED = 'energizedblue'  # It affects a future turn though, so we mostly don't do anything with it.
    ENTANGLED = 'entangled'
    EQUILIBRIUM = 'equilibrium'
    ENVENOM = 'envenom'
    EVOLVE = 'evolve'
    ESTABLISHMENT = 'establishmentpower'
    EXPLOSIVE = 'explosive'
    FADING = 'fading'
    FASTING = 'energydownpower'
    FEEL_NO_PAIN = 'feel no pain'
    FIRE_BREATHING = 'fire breathing'
    FLAME_BARRIER = 'flame barrier'
    FLIGHT = 'flight'
    FOCUS = 'focus'
    FORESIGHT = 'wireheadingpower'
    FRAIL = 'frail'
    FREE_ATTACK_POWER = 'freeattackpower'
    HEATSINK = 'heatsink'
    HELLO = 'hello'
    HEX = 'hex'
    INFINITE_BLADES = 'infinite blades'
    INTANGIBLE_PLAYER = 'intangibleplayer'
    INTANGIBLE_ENEMY = 'intangible'
    INTERNAL_ECHO_FORM_READY = 'echo form ready'  # internal use only, for marking whether echo form can be used
    JUGGERNAUT = 'juggernaut'
    LIKE_WATER = 'likewaterpower'
    LOCK_ON = 'lockon'
    LOOP = 'loop'
    MACHINE_LEARNING = 'machine learning'
    MAGNETISM = 'magnetism'
    MALLEABLE = 'malleable'
    MANTRA = 'mantra'
    MARK = 'pathtovictorypower'
    MAYHEM = 'mayhem'
    MENTAL_FORTRESS = 'controlled'
    MASTER_REALITY = 'masterrealitypower'
    METALLICIZE = 'metallicize'
    MINION = 'minion'
    MODE_SHIFT = 'mode shift'
    NEXT_TURN_BLOCK = 'next turn block'  # It affects a future turn though, so we mostly don't do anything with it.
    NIRVANA = 'nirvana'
    NO_DRAW = 'no draw'
    NOXIOUS_FUMES = 'noxious fumes'
    OMEGA = 'omega'
    PANACHE = 'panache'
    # We currently have damage provided by triggering the Panache power hardcoded to 10.
    # It's the first power we've run into that has multiple values associated with it.
    PEN_NIB_POWER = 'pen nib'  # Covered by Pen Nib relic counting
    PHANTASMAL = 'phantasmal'
    POISON = 'poison'
    PLATED_ARMOR = 'plated armor'
    RAGE = 'rage'
    REGENERATE_ENEMY = 'regenerate'
    REGENERATION_PLAYER = 'regeneration'
    REPAIR = 'repair'
    RUSHDOWN = 'adaptation'
    SADISTIC = 'sadistic'
    SHACKLED = 'shackled'  # Enemy regains strength at end of turn, not currently relevant
    SHARP_HIDE = 'sharp hide'
    SHIFTING = 'shifting'
    SIMMERING_RAGE = 'simmeringrage'
    SPLIT = 'split'
    STORM = 'storm'
    STRENGTH = 'strength'
    STUDY = 'study'
    TOOLS_OF_THE_TRADE = 'tools of the trade'
    THIEVERY = 'thievery'  # N/A
    THORNS = 'thorns'
    THOUSAND_CUTS = 'thousand cuts'
    TIME_WARP = 'time warp'
    UNAWAKENED = 'unawakened'
    VIGOR = 'vigor'
    VULNERABLE = 'vulnerable'
    WAVE_OF_THE_HAND = 'waveofthehandpower'
    WEAKENED = 'weakened'
    WRAITH_FORM_POWER = 'wraith form'
