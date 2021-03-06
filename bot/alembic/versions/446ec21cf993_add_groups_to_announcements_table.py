"""Add groups to Announcements table

Revision ID: 446ec21cf993
Revises: 434ccd372270
Create Date: 2020-12-07 01:12:22.822310

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "446ec21cf993"
down_revision = "434ccd372270"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("announcements", sa.Column("groups", sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("announcements", "groups")
    # ### end Alembic commands ###
