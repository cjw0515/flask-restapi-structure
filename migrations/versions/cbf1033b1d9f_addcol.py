"""'addcol'

Revision ID: cbf1033b1d9f
Revises: b5c38e2c01af
Create Date: 2019-10-27 18:29:54.854060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf1033b1d9f'
down_revision = 'b5c38e2c01af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin_menu', sa.Column('component', sa.String(length=150), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin_menu', 'component')
    # ### end Alembic commands ###
