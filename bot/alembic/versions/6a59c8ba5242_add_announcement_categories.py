"""Add Announcement Categories

Revision ID: 6a59c8ba5242
Revises: adde2f8bdd4e
Create Date: 2020-12-20 20:01:09.178912

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "6a59c8ba5242"
down_revision = "adde2f8bdd4e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    table = op.create_table(
        "announcements_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=1024), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("announcements", sa.Column("category", sa.Integer(), nullable=True))
    op.create_foreign_key("announcement_id", "announcements", "announcements_categories", ["category"], ["id"])
    op.bulk_insert(
        table,
        [
            {"id": 1, "name": "Default"},
        ],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("announcement_id", "announcements", type_="foreignkey")
    op.drop_column("announcements", "category")
    op.drop_table("announcements_categories")
    # ### end Alembic commands ###
