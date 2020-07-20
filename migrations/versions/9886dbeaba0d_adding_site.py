"""adding site

Revision ID: 9886dbeaba0d
Revises: d805931e1abd
Create Date: 2018-09-18 16:46:53.391795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9886dbeaba0d'
down_revision = 'd805931e1abd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('site', sa.String(length=32), nullable=True))
    op.create_index(op.f('ix_user_site'), 'user', ['site'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_site'), table_name='user')
    op.drop_column('user', 'site')
    # ### end Alembic commands ###