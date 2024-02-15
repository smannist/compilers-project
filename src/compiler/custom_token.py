from dataclasses import dataclass

@dataclass(frozen=True)
class L:
    line: int
    column: int

    def __str__(self) -> str:
        return f"L(line={self.line}, column={self.column})"

    def __eq__(self, object: object) -> bool:
        if (type(object).__name__ == "L" and hasattr(object, "line") and hasattr(object, "column")):
            return self.line == object.line and self.column == object.column
        return False

@dataclass(frozen=True)
class Token:
    loc: L
    type: str | None
    text: str

    def __str__(self) -> str:
        return f'Token(loc={self.loc}, type="{self.type}", text="{self.text}")'
