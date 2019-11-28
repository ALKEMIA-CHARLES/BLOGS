"""added username and relationships between blogs, comments and users

Revision ID: 6f907bef9f50
Revises: d029030221a9
Create Date: 2019-11-28 12:31:37.343836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f907bef9f50'
down_revision = 'd029030221a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogpost', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('blogpost', sa.Column('username', sa.String(), nullable=True))
    op.create_foreign_key(None, 'blogpost', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogpost', type_='foreignkey')
    op.drop_column('blogpost', 'username')
    op.drop_column('blogpost', 'user_id')
    # ### end Alembic commands ###