"""empty message

Revision ID: 77bd98eecc9f
Revises: 0904c1488eb0
Create Date: 2020-02-02 14:13:15.870393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77bd98eecc9f'
down_revision = '0904c1488eb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video_game', 'lore_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video_game', sa.Column('lore_link', sa.VARCHAR(length=100), nullable=False))
    # ### end Alembic commands ###
