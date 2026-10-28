"""add order status history

Revision ID: 62ff464c62bf
Revises: b2c3d4e5f6a7
Create Date: 2026-10-28 08:04:09.474279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

STATUS = postgresql.ENUM(
    "RECEIVED", "PROCESSING", "FULFILLED", "SHIPPED",
    "DELIVERED", "CANCELLED", "RETURNED",
    name="orderstatus", create_type=False,
)


# revision identifiers, used by Alembic.
revision: str = '62ff464c62bf'
down_revision: Union[str, Sequence[str], None] = 'b2c3d4e5f6a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "order_status_history",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("order_id", sa.Integer(),
                  sa.ForeignKey("orders.id"), nullable=False),
        sa.Column("status", STATUS, nullable=False),
        sa.Column("changed_at", sa.DateTime(),
                  server_default=sa.func.now(), nullable=False),
    )
    op.create_index(op.f("ix_order_status_history_id"),
                    "order_status_history", ["id"])
    op.create_index(op.f("ix_order_status_history_order_id"),
                    "order_status_history", ["order_id"])


def downgrade() -> None:
    op.drop_index(op.f("ix_order_status_history_order_id"),
                  table_name="order_status_history")
    op.drop_index(op.f("ix_order_status_history_id"),
                  table_name="order_status_history")
    op.drop_table("order_status_history")