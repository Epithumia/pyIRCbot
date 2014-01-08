import botconfig

# Stop editing here

# Argument --debug means start in debug mode
#          --verbose means to print a lot of stuff (when not in debug mode)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--sabotage', action='store_true')
parser.add_argument('--mafia', action='store_true')
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()
botconfig.DEBUG_MODE = args.debug if not botconfig.DISABLE_DEBUG_MODE else False
botconfig.VERBOSE_MODE = args.verbose

botconfig.DEFAULT_MODULE = "sabotage" if args.sabotage else "wolfgame"
botconfig.DEFAULT_MODULE = "mafiagame" if args.mafia else "wolfgame"
