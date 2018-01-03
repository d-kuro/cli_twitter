# -*- encoding: utf-8 -*-

HELLO_MESSAGE = """\
 ██████╗██╗     ██╗                                     
██╔════╝██║     ██║                                     
██║     ██║     ██║                                     
██║     ██║     ██║                                     
╚██████╗███████╗██║                                     
 ╚═════╝╚══════╝╚═╝                                     
                                                        
████████╗██╗    ██╗██╗████████╗████████╗███████╗██████╗ 
╚══██╔══╝██║    ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
   ██║   ██║ █╗ ██║██║   ██║      ██║   █████╗  ██████╔╝
   ██║   ██║███╗██║██║   ██║      ██║   ██╔══╝  ██╔══██╗
   ██║   ╚███╔███╔╝██║   ██║      ██║   ███████╗██║  ██║
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                        
 ██████╗██╗     ██╗███████╗███╗   ██╗████████╗          
██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝          
██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║             
██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║             
╚██████╗███████╗██║███████╗██║ ╚████║   ██║             
 ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝             
 Show Help is Type [help].
"""

HELP_MESSAGE = """\
[h] / [home]       = show timeline.(non stream)
                     [OPTION] [COUNT(DEFAULT 10)]
[stream]           = steram timeline.
[p] / [post]       = post tweet.
                     [OPTIONS] [*POSTTEXT] [REPLYID]
[r] / [retweet]    = retweet.
                     [OPTION] [*ID]
[s] / [search]     = search tweets.
                     [OPTIONS] [*KEYWORD] [COUNT(DEFAULT 10)]
[m] / [mydata]     = show mydata.

* is Required

***************************************************************

[q] / [e] / [exit] = exit.
[help]             = show help.
[c] / [clear]      = claer console.
"""

COMMAND_LIST = [
  "h", "home",
  "stream",
  "p", "post",
  "r", "retweet",
  "s", "search",
  "m", "mydata",
  "q", "e", "exit",
  "help",
  "c", "clear"
]
