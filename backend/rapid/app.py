from __future__ import absolute_import
from __future__ import unicode_literals

from keg import Keg

from rapid.views import public


class Rapid(Keg):
    import_name = 'rapid'
    use_blueprints = [public]
    db_enabled = True
