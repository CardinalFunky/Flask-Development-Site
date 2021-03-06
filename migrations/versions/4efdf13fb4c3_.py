"""empty message

Revision ID: 4efdf13fb4c3
Revises: 50ec893d1c91
Create Date: 2020-02-01 00:39:40.662878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4efdf13fb4c3'
down_revision = '50ec893d1c91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video__game__achievements')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video__game__achievements',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('image_file', sa.VARCHAR(length=20), nullable=True),
    sa.Column('video_game_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
