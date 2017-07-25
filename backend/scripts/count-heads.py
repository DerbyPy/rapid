#!/usr/bin/env python3

from alembic.config import Config
from alembic.script import ScriptDirectory

cfg = Config('alembic.ini')
scripts = ScriptDirectory.from_config(cfg)
current_heads = scripts.get_revisions(scripts.get_heads())

if len(current_heads) != 1:
    print("WARNING!!! Multiple migration heads found ({})".format(len(current_heads)))
    print("This issue will cause the deployment to fail. To resolve this issue, ensure that only "
          "one head is present in the alembic tree by properly setting the down revision. \n")

    for head in current_heads:
        print("Offending Revision Details:")
        print(head.cmd_format(True))
    exit(1)
else:
    exit(0)
