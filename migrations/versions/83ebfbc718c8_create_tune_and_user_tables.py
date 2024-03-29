"""Create tune and user tables

Revision ID: 83ebfbc718c8
Revises: 
Create Date: 2023-04-16 02:30:42.231842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ebfbc718c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tunes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('composer', sa.String(length=64), nullable=True),
    sa.Column('key', sa.String(length=3), nullable=True),
    sa.Column('other_key', sa.String(length=12), nullable=True),
    sa.Column('song_form', sa.String(length=20), nullable=True),
    sa.Column('style', sa.String(length=20), nullable=True),
    sa.Column('meter', sa.SmallInteger(), nullable=True),
    sa.Column('year', sa.SmallInteger(), nullable=True),
    sa.Column('decade', sa.String(length=5), nullable=True),
    sa.Column('knowledge', sa.String(length=10), nullable=True),
    sa.Column('started_learning', sa.DateTime(), nullable=True),
    sa.Column('last_played', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('repertoire',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tune_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tune_id'], ['tunes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tune_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repertoire')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    op.drop_table('tunes')
    # ### end Alembic commands ###
