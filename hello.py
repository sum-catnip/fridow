import lib
from lib import Module

from typing import List

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Header, Footer, Checkbox, ListView, ListItem

class ModuleTui(ListItem):
    def __init__(self, mod: Module):
        super().__init__()
        self.mod = mod

    def compose(self) -> ComposeResult:
        yield Checkbox(label=f'{self.mod.name} ({self.mod.entry})', value=self.mod.enabled)

class FridaTui(App):
    mods: List[Module]

    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(
            ModuleTui(Module("kek", "kek.js", True)),
            ModuleTui(Module("top", "top.js", True))
        )
        yield Footer()

def main():
    app = FridaTui()
    app.run()

if __name__ == "__main__":
    main()
