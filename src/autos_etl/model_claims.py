from dataclasses import dataclass

@dataclass
class ClaimLine:
    line_nbr: int = None
    sequence_nbr: int = None
    paid_amount: float = None
    allowed_amount: float = None
    rev_code: str = None

@dataclass
class Claim:
    claim_id: int
    claim_lines: list[ClaimLine]


@dataclass
class Encounter:
    pass

