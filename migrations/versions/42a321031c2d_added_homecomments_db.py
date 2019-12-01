"""added HomeComments db

Revision ID: 42a321031c2d
Revises: 9fdacc459b7e
Create Date: 2019-12-01 13:03:14.351044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42a321031c2d'
down_revision = '9fdacc459b7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homecomments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('home_comments_section', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homecomments')
    # ### end Alembic commands ###
