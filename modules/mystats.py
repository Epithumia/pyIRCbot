# Copyright (c) 2011, Jimmy Cao
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from tools import decorators
import settings.mystats as var
import time
from datetime import datetime, timedelta
import botconfig

import sqlite3

COMMANDS = {}
PM_COMMANDS = {}
HOOKS = {}

cmd = decorators.generate(COMMANDS)
pmcmd = decorators.generate(PM_COMMANDS)
hook = decorators.generate(HOOKS, raw_nick=True, permissions=False)

def connect_callback(cli):
    var.PHASE = "none"
    var.PLAYERS = []
    
    var.LAST_STATS = None


@cmd("mystats")
def get_my_stats(cli, nick, chan, rest):
    """Get my stats of how good I really am/was."""
    rest = rest.strip()
    if(rest == ""):
        cli.msg(chan, "Supply a role name.")
    
    var.CONN = sqlite3.connect(var.NAME, check_same_thread = False)
    with var.CONN:
        c = var.CONN.cursor()
        for row in c.execute("SELECT * FROM rolestats WHERE player = '%s' AND role = '%s'" % (nick, rest.strip())):
            row = list(row)[1:]
            print(len(row))
            cli.msg(chan, ("As {0}, you have {1} team wins, {2} individual wins, and {3} total games.".format(*row)))
    
def load_saved_settings(nam):
    var.CONN = sqlite3.connect(nam, check_same_thread = False)

    with var.CONN:
        c = var.CONN.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS away (nick TEXT)')  # whoops, i mean cloak, not nick

        c.execute('CREATE TABLE IF NOT EXISTS simple_role_notify (cloak TEXT)') # people who understand each role


        c.execute(('CREATE TABLE IF NOT EXISTS rolestats (player TEXT, role TEXT, '+
            'teamwins SMALLINT, individualwins SMALLINT, totalgames SMALLINT, '+
            'UNIQUE(player, role))'))
            
load_saved_settings(var.NAME)
