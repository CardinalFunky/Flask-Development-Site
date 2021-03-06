"""empty message

Revision ID: 748a01615607
Revises: aa4335c154b2
Create Date: 2020-02-01 15:05:55.179860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '748a01615607'
down_revision = 'aa4335c154b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video_game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_game')
    # ### end Alembic commands ###
