from src.domain.pericia import Pericia
from src.infrastructure.entity.pericia_entity import PericiaEntity

class PericiaMapper:

    def paraEntity(self, pericia: Pericia) -> PericiaEntity:
        return PericiaEntity(
            id_pericia=pericia.id,
            titulo=pericia.titulo
        )

    def paraDomain(self, pericia_entity: PericiaEntity) -> Pericia:
        return Pericia(
            id=pericia_entity.id_pericia,
            titulo=pericia_entity.titulo
        )