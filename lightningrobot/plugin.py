from abc import ABC, abstractmethod
from lightningrobot import log
class Plugin(ABC):
    @abstractmethod
    async def on_message(self, message: str) -> None:
        """处理接收到的消息"""
        log.info("收到消息：",message)
        #未来在此处添加判断用户。
        pass