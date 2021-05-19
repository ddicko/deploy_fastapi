"""adding image field

Revision ID: aba1fd8e47b1
Revises: 9d0e49187419
Create Date: 2021-05-19 09:24:28.758764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "aba1fd8e47b1"
down_revision = "9d0e49187419"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("url", sa.String(200)))


def downgrade():
    pass
