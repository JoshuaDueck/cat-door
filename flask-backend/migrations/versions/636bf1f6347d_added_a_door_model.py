"""Added a door model

Revision ID: 636bf1f6347d
Revises: 62e52f69fd1c
Create Date: 2023-12-29 14:33:10.704481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '636bf1f6347d'
down_revision = '62e52f69fd1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('door',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('locked', sa.Boolean(), nullable=True),
    sa.Column('open', sa.Boolean(), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('door')
    # ### end Alembic commands ###
