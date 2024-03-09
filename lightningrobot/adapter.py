from abc import ABC, abstractmethod

class Adapter(ABC):
    @abstractmethod
    async def connect(self) -> None:
        """连接到聊天平台"""
        pass
    
    @abstractmethod
    async def send_message(self, message: str) -> None:
        """发送消息"""
        pass

    @abstractmethod
    async def listen(self) -> str:
        """监听并获取新消息"""
        pass