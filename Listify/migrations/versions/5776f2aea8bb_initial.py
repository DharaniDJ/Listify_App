"""initial

Revision ID: 5776f2aea8bb
Revises: 
Create Date: 2023-03-26 12:56:21.805290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5776f2aea8bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###
