"""create comment system

Revision ID: 61ad34a3379d
Revises: aba1fd8e47b1
Create Date: 2021-05-19 10:36:57.096457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "61ad34a3379d"
down_revision = "aba1fd8e47b1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer, primary_key=True, unique=True),
        sa.Column("name", sa.String(100)),
        sa.Column("email", sa.String(1000)),
        sa.Column("body", sa.String(1000)),
        sa.Column("post_id", sa.Integer),
        sa.Column("is_active", sa.Boolean),
        sa.Column("created_date", sa.DateTime),
    )


def downgrade():
    pass
