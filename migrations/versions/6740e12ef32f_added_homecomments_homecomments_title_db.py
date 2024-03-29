"""added HomeComments homecomments title db

Revision ID: 6740e12ef32f
Revises: 42a321031c2d
Create Date: 2019-12-01 13:22:03.499782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6740e12ef32f'
down_revision = '42a321031c2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('homecomments', sa.Column('home_comments_title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('homecomments', 'home_comments_title')
    # ### end Alembic commands ###
