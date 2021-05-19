"""Create post table

Revision ID: 9d0e49187419
Revises: 94f2fe587bf8
Create Date: 2021-05-18 16:58:15.468317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9d0e49187419"
down_revision = "94f2fe587bf8"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True, unique=True),
        sa.Column("title", sa.String(100)),
        sa.Column("body", sa.String(1000)),
        sa.Column("owner_id", sa.Integer),
        sa.Column("is_active", sa.Boolean),
        sa.Column("created_date", sa.DateTime),
    )


def downgrade():
    pass
