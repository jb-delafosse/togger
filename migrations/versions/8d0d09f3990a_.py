"""empty message

Revision ID: 8d0d09f3990a
Revises:
Create Date: 2020-06-25 22:22:13.900545

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
import togger

revision = "8d0d09f3990a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "calendar",
        sa.Column("id", togger.database.GUID(), nullable=False),
        sa.Column("settings", sa.JSON(), nullable=True),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", togger.database.GUID(), nullable=False),
        sa.Column("alias_id", togger.database.GUID(), nullable=False),
        sa.Column("username", sa.String(length=80), nullable=False),
        sa.Column("first_name", sa.String(length=80), nullable=False),
        sa.Column("last_name", sa.String(length=80), nullable=False),
        sa.Column("password", sa.String(length=100), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("alias_id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "recur_event",
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("start", sa.DateTime(), nullable=False),
        sa.Column("end", sa.DateTime(), nullable=False),
        sa.Column("all_day", sa.Boolean(), nullable=False),
        sa.Column("id", togger.database.GUID(), nullable=False),
        sa.Column("start_recur", sa.DateTime(), nullable=False),
        sa.Column("end_recur", sa.DateTime(), nullable=True),
        sa.Column("rrule", sa.String(length=256), nullable=False),
        sa.Column("recurrent_type", sa.String(length=256), nullable=False),
        sa.Column("recurrent_interval", sa.Integer(), nullable=False),
        sa.Column("calendar_id", togger.database.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["calendar_id"],
            ["calendar.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "role",
        sa.Column("id", togger.database.GUID(), nullable=False),
        sa.Column("type", sa.Integer(), nullable=False),
        sa.Column("calendar_id", togger.database.GUID(), nullable=False),
        sa.Column("user_id", togger.database.GUID(), nullable=False),
        sa.Column("is_default", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["calendar_id"],
            ["calendar.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("calendar_id", "user_id", name="role_cal_user_key"),
    )
    op.create_table(
        "event",
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("start", sa.DateTime(), nullable=False),
        sa.Column("end", sa.DateTime(), nullable=False),
        sa.Column("all_day", sa.Boolean(), nullable=False),
        sa.Column("id", togger.database.GUID(), nullable=False),
        sa.Column("recur_id", togger.database.GUID(), nullable=True),
        sa.Column("init_start", sa.DateTime(), nullable=True),
        sa.Column("calendar_id", togger.database.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["calendar_id"],
            ["calendar.id"],
        ),
        sa.ForeignKeyConstraint(
            ["recur_id"],
            ["recur_event.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "shift",
        sa.Column("id", togger.database.GUID(), nullable=False),
        sa.Column("person", sa.String(length=80), nullable=False),
        sa.Column("event_id", togger.database.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["event.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "person", "event_id", name="shift_person_event_key"
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shift")
    op.drop_table("event")
    op.drop_table("role")
    op.drop_table("recur_event")
    op.drop_table("user")
    op.drop_table("calendar")
    # ### end Alembic commands ###
