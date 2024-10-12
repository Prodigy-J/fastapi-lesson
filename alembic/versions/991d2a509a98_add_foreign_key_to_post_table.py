"""add foreign key to post table

Revision ID: 991d2a509a98
Revises: b71a27efbc60
Create Date: 2024-10-05 08:15:57.242789

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "991d2a509a98"
down_revision: Union[str, None] = "b71a27efbc60"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("post", sa.Column("user_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "user_post_fk",
        source_table="post",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    op.rename_table("post", "posts")
    pass


def downgrade() -> None:
    op.rename_table("posts", "post")
    op.drop_constraint(constraint_name="user_post_fk", table_name="post")
    op.drop_column(column_name="user_id", table_name="post")
    pass
