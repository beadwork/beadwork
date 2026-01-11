from __future__ import annotations

from rio import Column
from rio import Component
from rio import PageView
from rio import Spacer

# from .. import components as comps


class RootComponent(Component):

    def build(self) -> Component:
        return Column(
            # comps.Navbar(),
            Spacer(min_height=10),
            PageView(grow_y=True),
            # comps.Footer(),
        )
