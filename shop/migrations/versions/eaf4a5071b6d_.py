"""empty message

Revision ID: eaf4a5071b6d
Revises: 
Create Date: 2020-01-03 20:24:00.904884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaf4a5071b6d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'products', ['id'])
    op.create_unique_constraint(None, 'shops', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'shops', type_='unique')
    op.drop_constraint(None, 'products', type_='unique')
    # ### end Alembic commands ###
