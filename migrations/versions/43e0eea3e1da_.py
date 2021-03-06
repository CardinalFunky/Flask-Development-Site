"""empty message

Revision ID: 43e0eea3e1da
Revises: 748a01615607
Create Date: 2020-02-02 13:50:27.817600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43e0eea3e1da'
down_revision = '748a01615607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video_game', sa.Column('lore_link', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video_game', 'lore_link')
    # ### end Alembic commands ###
