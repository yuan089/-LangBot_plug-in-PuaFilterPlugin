from __future__ import annotations
from langbot_plugin.api.definition.plugin import BasePlugin

class PuaFilterPlugin(BasePlugin):
    async def initialize(self) -> None:
        # 坚决弃用 self.logger，改用原生 print，保证 100% 存活
        print("\n\033[92m[SUCCESS] ✅ PuaFilterPlugin 已經成功載入並待命！\033[0m\n")

    def __del__(self) -> None:
        pass