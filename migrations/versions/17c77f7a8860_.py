"""empty message

Revision ID: 17c77f7a8860
Revises: 8af9f3313560
Create Date: 2020-07-02 20:54:31.466356

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '17c77f7a8860'
down_revision = '8af9f3313560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('UPDATE event SET hide = FALSE WHERE hide IS NULL')
    # ### end Alembic commands ###


def downgrade():
    None
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###