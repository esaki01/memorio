import dataclasses

from src.domain.library import Library


@dataclasses.dataclass
class GetLibraryResponse:
    library: Library
