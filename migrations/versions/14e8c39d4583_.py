"""empty message

Revision ID: 14e8c39d4583
Revises: 4f88a27e5351
Create Date: 2021-04-17 11:02:21.743494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14e8c39d4583'
down_revision = '4f88a27e5351'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_last_name', table_name='user')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'email')
    op.drop_column('user', 'dob')
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.add_column('user', sa.Column('dob', sa.DATE(), nullable=False))
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(length=64), nullable=True))
    op.create_index('ix_user_last_name', 'user', ['last_name'], unique=1)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    # ### end Alembic commands ###