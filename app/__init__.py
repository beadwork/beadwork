from __future__ import annotations

from pathlib import Path

from rio import App
from rio import Session

from . import components as comps
from . import themes


def on_session_start(sess: Session) -> None:
    pass


app = App(
    name="Beadwork",
    on_session_start=on_session_start,
    build=comps.RootComponent,
    theme=themes.THEME,
    assets_dir=Path(__file__).parent / "assets",
)
