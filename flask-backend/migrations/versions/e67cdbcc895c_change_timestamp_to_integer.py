"""Change timestamp to Integer

Revision ID: e67cdbcc895c
Revises: 848ac7a01c00
Create Date: 2023-12-13 22:28:22.883458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e67cdbcc895c'
down_revision = '848ac7a01c00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entry', schema=None) as batch_op:
        batch_op.alter_column('timestamp',
               existing_type=sa.DATETIME(),
               type_=sa.Integer(),
               existing_nullable=False,
               existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entry', schema=None) as batch_op:
        batch_op.alter_column('timestamp',
               existing_type=sa.Integer(),
               type_=sa.DATETIME(),
               existing_nullable=False,
               existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))

    # ### end Alembic commands ###
