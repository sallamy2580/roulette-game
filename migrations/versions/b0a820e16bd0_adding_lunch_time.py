"""adding lunch time

Revision ID: b0a820e16bd0
Revises: 24cb272fe5ab
Create Date: 2018-12-15 12:15:51.844636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0a820e16bd0'
down_revision = '24cb272fe5ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lunch_time', sa.Time(), nullable=True))
    op.create_index(op.f('ix_user_last_seen'), 'user', ['last_seen'], unique=False)
    op.create_index(op.f('ix_user_lunch_time'), 'user', ['lunch_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_lunch_time'), table_name='user')
    op.drop_index(op.f('ix_user_last_seen'), table_name='user')
    op.drop_column('user', 'lunch_time')
    # ### end Alembic commands ###
