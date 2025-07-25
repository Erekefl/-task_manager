"""add city to user

Revision ID: 45b5fcdefa7c
Revises: 82b760d1aba9
Create Date: 2025-07-17 22:40:34.660267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45b5fcdefa7c'
down_revision: Union[str, Sequence[str], None] = '82b760d1aba9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('city', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'city')
    # ### end Alembic commands ###
