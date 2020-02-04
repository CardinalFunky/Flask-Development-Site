"""empty message

Revision ID: b0aeb8c2f01b
Revises: 77bd98eecc9f
Create Date: 2020-02-02 14:13:31.681116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0aeb8c2f01b'
down_revision = '77bd98eecc9f'
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
