"""create users table

Revision ID: 88b4987a1a16
Revises: 46412376ba72
Create Date: 2024-09-02 09:26:08.227181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88b4987a1a16'
down_revision: Union[str, None] = '46412376ba72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
