import uuid

from sqlalchemy import Boolean, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Character(Base):
    __tablename__ = "characters"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), server_default=func.gen_random_uuid(), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    nickname: Mapped[str] = mapped_column(String(32))
    age: Mapped[int] = mapped_column(Integer())
    bio: Mapped[int] = mapped_column(String(255), nullable=True)
    coins: Mapped[int] = mapped_column(Integer(), default=0)
    health: Mapped[int] = mapped_column(Integer(), default=100)
    energy: Mapped[int] = mapped_column(Integer(), default=100)
    productivity: Mapped[int] = mapped_column(Integer(), default=100)
    reputation: Mapped[int] = mapped_column(Integer(), default=5)
    strength: Mapped[int] = mapped_column(Integer(), default=5)
    experience: Mapped[int] = mapped_column(Integer(), default=0)
    level: Mapped[int] = mapped_column(Integer(), default=0)
    violations: Mapped[int] = mapped_column(Integer(), default=0)
    arrested: Mapped[int] = mapped_column(Boolean(), default=False)

    user = relationship("User", back_populates="character")
