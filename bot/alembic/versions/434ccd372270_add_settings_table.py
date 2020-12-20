"""Add Settings table

Revision ID: 434ccd372270
Revises: 80d6b49d2d7b
Create Date: 2020-12-07 01:10:18.187418

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "434ccd372270"
down_revision = "80d6b49d2d7b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "settings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(length=128), nullable=False),
        sa.Column("value", sa.String(length=1024), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("settings")
    # ### end Alembic commands ###