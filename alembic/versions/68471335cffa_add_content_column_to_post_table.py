"""Add content column to post table

Revision ID: 68471335cffa
Revises: aad0e5a4c8c6
Create Date: 2024-10-05 06:52:45.821143

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68471335cffa"
down_revision: Union[str, None] = "aad0e5a4c8c6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("post", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("post", "content")
    pass
