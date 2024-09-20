"""Profile.dob type: DateTime -> Profile.dob type: Date

Revision ID: 2e889a1bfdfa
Revises: 48c62dd0cd1b
Create Date: 2024-09-20 22:37:01.555628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e889a1bfdfa'
down_revision = '48c62dd0cd1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.alter_column('dob',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.alter_column('dob',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
