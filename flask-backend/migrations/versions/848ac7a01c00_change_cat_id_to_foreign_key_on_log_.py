"""Change cat ID to foreign key on log entry

Revision ID: 848ac7a01c00
Revises: 6d708112a570
Create Date: 2023-12-13 22:07:58.336974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '848ac7a01c00'
down_revision = '6d708112a570'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entry', schema=None) as batch_op:
        batch_op.alter_column('cat_id',
               existing_type=sa.INTEGER(),
            )
        batch_op.create_foreign_key('fk_log_entry_cat_id', 'cat', ['cat_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entry', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('cat_id',
               existing_type=sa.INTEGER(),
            )
    # ### end Alembic commands ###
