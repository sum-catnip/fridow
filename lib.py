from dataclasses import dataclass
from typing import List
import toml

@dataclass
class Module:
    name: str
    entry: str
    enabled: bool

def load_mods() -> List[Module]:
    with open('frida.toml') as f:
        cfg = toml.load(f)
        return [Module(n, **m) for n, m in cfg['modules'].items()]