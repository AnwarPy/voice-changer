from typing import Protocol

from voice_changer.utils.LoadModelParams import LoadModelParams


class ModelSlotGenerator(Protocol):
    @classmethod
    def loadModel(self, params: LoadModelParams):
        ...
