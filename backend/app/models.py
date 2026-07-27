import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Category(enum.StrEnum):
    TOPS = "tops"
    BOTTOMS = "bottoms"
    OUTERWEAR = "outerwear"
    SHOES = "shoes"
    ACCESSORIES = "accessories"
    DRESSES = "dresses"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    clothing_items: Mapped[list["ClothingItem"]] = relationship(
        "ClothingItem", back_populates="user", cascade="all, delete-orphan"
    )
    outfits: Mapped[list["Outfit"]] = relationship(
        "Outfit", back_populates="user", cascade="all, delete-orphan"
    )


class ClothingItem(Base):
    __tablename__ = "clothing_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[Category] = mapped_column(Enum(Category), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_path: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="clothing_items")
    outfit_items: Mapped[list["OutfitItem"]] = relationship(
        "OutfitItem", back_populates="clothing_item", cascade="all, delete-orphan"
    )


class Outfit(Base):
    __tablename__ = "outfits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="outfits")
    items: Mapped[list["OutfitItem"]] = relationship(
        "OutfitItem", back_populates="outfit", cascade="all, delete-orphan"
    )


class OutfitItem(Base):
    __tablename__ = "outfit_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    outfit_id: Mapped[int] = mapped_column(
        ForeignKey("outfits.id", ondelete="CASCADE"), nullable=False
    )
    clothing_item_id: Mapped[int] = mapped_column(ForeignKey("clothing_items.id"), nullable=False)
    position: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    outfit: Mapped["Outfit"] = relationship("Outfit", back_populates="items")
    clothing_item: Mapped["ClothingItem"] = relationship(
        "ClothingItem", back_populates="outfit_items"
    )
