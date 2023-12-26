"""更改商品信息表默认值

Revision ID: 99a46abfac7c
Revises: c1df3bc26c57
Create Date: 2023-12-26 13:08:22.574405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.services.auth_service import get_password_hash


# revision identifiers, used by Alembic.
revision: str = '99a46abfac7c'
down_revision: Union[str, None] = 'c1df3bc26c57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods_info', 'amount',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_comment='数量')
    op.alter_column('goods_info', 'unit_price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True,
               existing_comment='单价')
    op.alter_column('goods_info', 'occasion',
               existing_type=sa.VARCHAR(length=50),
               nullable=True,
               existing_comment='使用场合')
    op.alter_column('goods_info', 'description',
               existing_type=sa.TEXT(),
               nullable=True,
               existing_comment='商品描述')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goods_info', 'description',
               existing_type=sa.TEXT(),
               nullable=False,
               existing_comment='商品描述')
    op.alter_column('goods_info', 'occasion',
               existing_type=sa.VARCHAR(length=50),
               nullable=False,
               existing_comment='使用场合')
    op.alter_column('goods_info', 'unit_price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False,
               existing_comment='单价')
    op.alter_column('goods_info', 'amount',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_comment='数量')
    # ### end Alembic commands ###
