"""empty message

Revision ID: 4f88a27e5351
Revises: 
Create Date: 2021-04-17 10:55:30.452781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f88a27e5351'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('pronouns', sa.String(length=64), nullable=True),
    sa.Column('preferences', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=True)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=True)
    op.create_index(op.f('ix_user_preferences'), 'user', ['preferences'], unique=True)
    op.create_index(op.f('ix_user_pronouns'), 'user', ['pronouns'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_pronouns'), table_name='user')
    op.drop_index(op.f('ix_user_preferences'), table_name='user')
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
