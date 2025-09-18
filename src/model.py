from pydantic import BaseModel


class EmbeddingConfig(BaseModel):
    alphabets: list[str]
    Query_marker: str  # answer-begin marker, Q
    HB_marker: str  # token encapsulation begin marker, (
    HE_marker: str  # token encapsulation end marker, )


class IsoCategory(BaseModel):
    """
    A category of li
    """
    name: str
    base_forms: list[list[str]]  # e.g. [['AA', 'CC', 'TT'], ['AA', 'TT', 'CC']]
    permuted_allowed: bool
    result_marker: str