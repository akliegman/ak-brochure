"""empty message

Revision ID: 9598d4ecc64c
Revises:
Create Date: 2018-08-16 12:04:32.112816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9598d4ecc64c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('first_name', sa.String(length=32), nullable=True),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
