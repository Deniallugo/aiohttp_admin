from abc import ABC, abstractmethod


class GrpcClient(ABC):
    @abstractmethod
    async def update(self, entity_id: str, **kwargs):
        pass

    @abstractmethod
    async def create(self, **kwargs):
        pass

    @abstractmethod
    async def delete(self, entity_id: str):
        pass


class GrpcError(Exception):
    pass
