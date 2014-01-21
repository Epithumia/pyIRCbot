############################
# General options/settings #
############################

PING_WAIT = 300  # Seconds
PING_MIN_WAIT = 30 # How long !start has to wait after a !ping
MINIMUM_WAIT = 60
EXTRA_WAIT = 20
MAXIMUM_WAITED = 3  # limit for amount of !wait's
STATS_RATE_LIMIT = 15
VOTES_RATE_LIMIT = 15
ADMINS_RATE_LIMIT = 300
MAX_PLAYERS = 40

NIGHT_TIME_LIMIT = 120
NIGHT_TIME_WARN = 90  # should be less than NIGHT_TIME_LIMIT

MIDNIGHT_TIME_LIMIT = 60
MIDNIGHT_TIME_WARN = 55  # should be less than MIDNIGHT_TIME_LIMIT

DAY_TIME_LIMIT_WARN = 600
DAY_TIME_LIMIT_CHANGE = 120  # seconds after DAY_TIME_LIMIT_WARN has passed
# May only be set if the above are also set
SHORT_DAY_PLAYERS = 6 # Number of players left to have a short day
SHORT_DAY_LIMIT_WARN = 400
SHORT_DAY_LIMIT_CHANGE = 120
KILL_IDLE_TIME = 300
WARN_IDLE_TIME = 180
PART_GRACE_TIME = 12
QUIT_GRACE_TIME = 30
#  controls how many people it does in one /msg; only works for messages that are the same
MAX_PRIVMSG_TARGETS = 2
LEAVE_STASIS_PENALTY = 1
IDLE_STASIS_PENALTY = 0
PART_STASIS_PENALTY = 1

GOAT_HERDER = True

SELF_LYNCH_ALLOWED = True

CARE_BOLD = True
CARE_COLOR = True
KILL_COLOR = False
KILL_BOLD = False

LOG_FILENAME = "game.log"
BARE_LOG_FILENAME = "barelog.log"







#################################################################################################################
# ROLE INDEX: PLAYERS SEER|WOLF|CURSED|DRUNK|HARLOT|TRAITOR|GUNNER|CROW|GUARD|DETECTIVE                        ##
#                     WITCH|CUPID|THIEF|GIRL|HUNTER|ANCIENT|SHAMAN|IDIOT|SCAPEGOAT|PIPER                       ##
#                     WHITEWOLF|CROW|KID|ANGEL|FATHER|BBW|SISTER|CHATTYSEER                                    ##
#################################################################################################################
ROLES_GUIDE = { 4    : (1,1,0,0,0,0,0,0,0,0,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                6    : (1,1,1,1,0,0,0,0,0,0,                                                                   ##
                                            1,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,2,0),                              ##
                8    : (1,2,1,1,1,0,0,0,0,0,                                                                   ##
                                            1,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,2,0),                              ##
                10   : (1,2,1,1,1,1,1,0,0,0,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                12   : (1,2,1,1,1,1,1,1,0,1,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                15   : (1,3,1,1,1,1,1,1,0,1,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                17   : (1,3,1,1,1,1,1,1,1,1,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                22   : (1,4,1,1,1,1,1,1,1,1,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                25   : (1,4,2,1,1,1,1,1,1,1,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                29   : (1,5,2,1,1,1,1,1,1,1,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0),                              ##
                None : (0,0,0,0,0,0,0,0,0,0,                                                                   ##
                                            0,0,0,0,0,0,0,0,0,0,                                               ##
                                                                0,0,0,0,0,0,0,0)}                              ##
#################################################################################################################
#   Notes:                                                                                                     ##
#################################################################################################################

GAME_MODES = {}
AWAY = []  # cloaks of people who are away.
SIMPLE_NOTIFY = []  # cloaks of people who !simple, who want everything /notice'd

ROLE_INDICES = {0  : "seer",                 # ok
                1  : "wolf",                 # ok
                2  : "cursed villager",      # ok
                3  : "village drunk",        # ok
                4  : "harlot",               # ok
                5  : "traitor",              # ok
                6  : "gunner",               # ok
                7  : "werecrow",             # ok
                8  : "guardian angel",       # ok
                9  : "detective",            # ok
                10 : "witch",                # ok
                11 : "cupid",                # TODO
                12 : "thief",                # TODO
                13 : "little girl",          # ok
                14 : "hunter",               # TODO
                15 : "ancient",              # TODO
                16 : "shaman",               # ok
                17 : "village idiot",        # ok
                18 : "scapegoat",            # TODO
                19 : "pied piper",           # TODO
                20 : "white wolf",           # TODO
                21 : "crow",                 # ok
                22 : "wild kid",             # TODO
                23 : "angel",                # ok
                24 : "wolf father",          # TODO
                25 : "big bad wolf",         # TODO
                26 : "sister"                # ok
                27 : "chatty seer"           # ok
                }

# TODO: Code roles
# Villager : default role, tries to survive with the restof the village
# 0: Seer: Can scrye at night to discover the identity of a villager
# 1: Wolf: Meets other wolves at night to eat a villager
# 2: Cursed: Seen as a wolf by the seer but as an innocent by the detective
# 3: Drunk villager: no power
# 4: Harlot: can visit someone at night and prevent their power
# 5: Traitor: appears as a villager, but sided with the wolves
# 6: Gunner: has a gun, may kill the wolves at night, may lose his gun upon death
SHOTS_MULTIPLIER = .12  # ceil(shots_multiplier * len_players) = bullets given
DRUNK_SHOTS_MULTIPLIER = 3
                    #       HIT    MISS    SUICIDE
GUN_CHANCES         =   (   5/7  ,  1/7  ,   1/7   )
DRUNK_GUN_CHANCES   =   (   2/7  ,  4/7  ,   1/7   )
MANSLAUGHTER_CHANCE =       1/5  # ACCIDENTAL HEADSHOT (FATAL)
GUNNER_KILLS_WOLF_AT_NIGHT_CHANCE = 0
# 7: Werecrow: sided with the wolves, can visit a player at night to spy on him
# 8: Guardian angel: each night, can protect one player from the wolves. May (will?) die if he protects a wolf. No effect on the little girl.
GUARDIAN_ANGEL_DIES_CHANCE = 1/2
# 9: Detective: can check someone's true identity during the day, may reveal himself doing so.
DETECTIVE_REVEALED_CHANCE = 2/5
# 10: Witch: tries to eliminate the wolves, has two potions:
#     life potion to save the werewolves target, death potion to kill someone during the night 
# 11: Cupid: tries to kill the wolves ; at the beginning of the game, will choose two players and "marry" them
#        The two lovers' fate are linked: if one dies, so does the other. They know each other.
#        Their goal is to survive together. If they are on opposite side, their goal is to win against everyone.
# 12: Thief: will choose his role between the two that haven't been drawn.
# 13: Little girl: villager, can spy the wolves at night
LITTLE_GIRL_PEEK_CHANCE = 1/5
LITTLE_GIRL_SEEN_CHANCE = 1/6 #Double if peek is successful
# 14: Hunter: villager, revenge kills one player when he dies
# 15: Ancient: villager, he can survive the first wolf attack. 
#     If he is lynched or killed by the hunter or witch, every villager loses their power
# 16: Shaman: tries to kill the wolves ; has a short time during the night to listen to the spirits 
# 17: Village idiot: villager. If the village decides to lynch him, he will be spared at the last moment, but will lose his right to vote.
# 18: Scapegoat: villager. In case of a tie, he will be killed by default.
# 19: Pied piper: His goal is to win alone. He must charm every player alive, up to two each night.
# 20: White Wolf: His goal is to win the game alone. The other werewolves think he is a normal wolf, but every other night, 
#     he may kill one werewolf of his choice.
# 21: Crow: villager ; each night he may curse one player which will have two votes against him the next morning.
# 22: Wild kid: villager. At the beginning of the game, chooses a role model. If that player dies, the kid becomes a werewolf.
# 23: Angel: his goal is to be eliminated on the first turn of the game. If he does, the game ends and he wins. 
#     If he fails, he becomes a powerless villager
# 24: Wolf-father: his goal is to eliminate all the innocents (non-werewolves). At night convenes with the wolves to eliminate a player
#     Once per game, he can change the victim of the wolves into a wolf. The infected player keeps his power.
# 25: Big Bad Wolf: his goal is to kill the innocents (non wolves), each nights he convenes with the wolves.
#     Each night as long as no other wolf is dead, he may kill an additional victim
# 26: Sister: villager. She knows the identity of her sister, whom she can trust.
# 27: chatty seer: almost as a seer, but what was seen is announced to the room


INDEX_OF_ROLE = dict((v,k) for k,v in ROLE_INDICES.items())

NO_VICTIMS_MESSAGES = ("The body of a young penguin pet is found.",
                       "A pool of blood and wolf paw prints are found.",
                       "Traces of wolf fur are found.")
LYNCH_MESSAGES = ("The villagers, after much debate, finally decide on lynching \u0002{0}\u0002, who turned out to be... a \u0002{1}\u0002.",
                  "Under a lot of noise, the pitchfork-bearing villagers lynch \u0002{0}\u0002, who turned out to be... a \u0002{1}\u0002.",
                  "The mob drags a protesting \u0002{0}\u0002 to the hanging tree. S/He succumbs to the will of the horde, and is hanged. It is discovered (s)he was a \u0002{1}\u0002.",
                  "Resigned to his/her fate, \u0002{0}\u0002 is led to the gallows. After death, it is discovered (s)he was a \u0002{1}\u0002.",
                  "As s/he is about to be lynched, \u0002{0}\u0002, the \u0002{1}\u0002, throws a grenade at the mob.  The grenade explodes early.")

import botconfig

RULES = (botconfig.CHANNEL + " channel rules: 1) Be nice to others. 2) Do not share information "+
         "after death. 3) No bots allowed. 4) Do not play with clones.\n"+
         "5) Do not quit unless you need to leave. 6) Keep it "+
         "safe for work. 7) Do not paste PM's from the bot during the game. "+
         "8) Use common sense. 9) Waiting for timeouts is discouraged.")

# Other settings:
START_WITH_DAY = False
WOLF_STEALS_GUN = False  # at night, the wolf can steal steal the victim's bullets

OPT_IN_PING = False  # instead of !away/!back, users can opt-in to be pinged
PING_IN = []  # cloaks of users who have opted in for ping

is_role = lambda plyr, rol: rol in ROLES and plyr in ROLES[rol]

def plural(role):
    if role == "wolf": return "wolves"
    elif role == "person": return "people"
    else: return role + "s"

def list_players():
    pl = []
    for x in ROLES.values():
        pl.extend(x)
    return pl

def list_players_and_roles():
    plr = {}
    for x in ROLES.keys():
        for p in ROLES[x]:
            plr[p] = x
    return plr

get_role = lambda plyr: list_players_and_roles()[plyr]


def del_player(pname):
    prole = get_role(pname)
    ROLES[prole].remove(pname)



class InvalidModeException(Exception): pass
def game_mode(name):
    def decor(c):
        GAME_MODES[name] = c
        return c
    return decor


CHANGEABLE_ROLES = { "seers"  : INDEX_OF_ROLE["seer"],
                     "wolves" : INDEX_OF_ROLE["wolf"],
                     "cursed" : INDEX_OF_ROLE["cursed villager"],
                    "drunks"  : INDEX_OF_ROLE["village drunk"],
                   "harlots"  : INDEX_OF_ROLE["harlot"],
                  "traitors"  : INDEX_OF_ROLE["traitor"],
                   "gunners"  : INDEX_OF_ROLE["gunner"],
                 "werecrows"  : INDEX_OF_ROLE["werecrow"],
                 "angels"     : INDEX_OF_ROLE["guardian angel"],
                 "detectives" : INDEX_OF_ROLE["detective"]}




# TODO: implement game modes
@game_mode("roles")
class ChangedRolesMode(object):
    """Example: !fgame roles=wolves:1,seers:0,angels:1"""

    def __init__(self, arg):
        self.ROLES_GUIDE = ROLES_GUIDE.copy()
        lx = list(ROLES_GUIDE[None])
        pairs = arg.split(",")
        if not pairs:
            raise InvalidModeException("Invalid syntax for mode roles.")
        for pair in pairs:
            change = pair.split(":")
            if len(change) != 2:
                raise InvalidModeException("Invalid syntax for mode roles.")
            role, num = change
            try:
                num = int(num)
                try:
                    lx[CHANGEABLE_ROLES[role.lower()]] = num
                except KeyError:
                    raise InvalidModeException(("The role \u0002{0}\u0002 "+
                                                "is not valid.").format(role))
            except ValueError:
                raise InvalidModeException("A bad value was used in mode roles.")
        for k in ROLES_GUIDE.keys():
            self.ROLES_GUIDE[k] = tuple(lx)


# Persistence


# Load saved settings
import sqlite3

conn = sqlite3.connect("data.sqlite3", check_same_thread = False)

with conn:
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS away (nick TEXT)')  # whoops, i mean cloak, not nick

    c.execute('CREATE TABLE IF NOT EXISTS simple_role_notify (cloak TEXT)') # people who understand each role

    c.execute('SELECT * FROM away')
    for row in c:
        AWAY.append(row[0])

    c.execute('SELECT * FROM simple_role_notify')
    for row in c:
        SIMPLE_NOTIFY.append(row[0])

    # populate the roles table
    c.execute('DROP TABLE IF EXISTS roles')
    c.execute('CREATE TABLE roles (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT)')

    for x in ["villager"]+list(ROLE_INDICES.values()):
        c.execute("INSERT OR REPLACE INTO roles (role) VALUES (?)", (x,))


    c.execute(('CREATE TABLE IF NOT EXISTS rolestats (player TEXT, role TEXT, '+
        'teamwins SMALLINT, individualwins SMALLINT, totalgames SMALLINT, '+
        'UNIQUE(player, role))'))

    if OPT_IN_PING:
        c.execute('CREATE TABLE IF NOT EXISTS ping (cloak text)')

        c.execute('SELECT * FROM ping')
        for row in c:
            PING_IN.append(row[0])


def remove_away(clk):
    with conn:
        c = conn.cursor()
        c.execute('DELETE from away where nick=?', (clk,))

def add_away(clk):
    with conn:
        c = conn.cursor()
        c.execute('INSERT into away VALUES (?)', (clk,))

def remove_simple_rolemsg(clk):
    with conn:
        c = conn.cursor()
        c.execute('DELETE from simple_role_notify where cloak=?', (clk,))

def add_simple_rolemsg(clk):
    with conn:
        c = conn.cursor()
        c.execute('INSERT into simple_role_notify VALUES (?)', (clk,))

def remove_ping(clk):
    with conn:
        c = conn.cursor()
        c.execute('DELETE from ping where cloak=?', (clk,))
def add_ping(clk):
    with conn:
        c = conn.cursor()
        c.execute('INSERT into ping VALUES (?)', (clk,))


def update_role_stats(acc, role, won, iwon):
    with conn:
        wins, iwins, totalgames = 0, 0, 0
        c = conn.cursor()
        c.execute(("SELECT teamwins, individualwins, totalgames FROM rolestats "+
                   "WHERE player=? AND role=?"), (acc, role))
        row = c.fetchone()
        if row:
            wins, iwins, total = row
        else:
            wins, iwins, total = 0,0,0

        if won:
            wins += 1
        if iwon:
            iwins += 1
        total += 1

        c.execute("INSERT OR REPLACE INTO rolestats VALUES (?,?,?,?,?)",
                  (acc, role, wins, iwins, total))



