"""componentnullable

Revision ID: a811e0ab44e7
Revises: a5ad206ef173
Create Date: 2020-01-06 10:16:47.663821

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a811e0ab44e7'
down_revision = 'a5ad206ef173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_menu', 'component',
               existing_type=mysql.VARCHAR(length=150),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_menu', 'component',
               existing_type=mysql.VARCHAR(length=150),
               nullable=False)
    # ### end Alembic commands ###
