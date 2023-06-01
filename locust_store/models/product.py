from typing import Optional, TYPE_CHECKING

from sqlmodel import Field, SQLModel, Relationship

from .cart_product_link import CartProductLink

if TYPE_CHECKING:
    from .cart import Cart


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

    carts: list["Cart"] = Relationship(back_populates="products", link_model=CartProductLink)
