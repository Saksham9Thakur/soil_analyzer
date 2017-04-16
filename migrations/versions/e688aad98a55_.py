"""empty message

Revision ID: e688aad98a55
Revises: 
Create Date: 2017-03-08 16:23:25.985970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e688aad98a55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mitti',
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('SoilMositure', sa.Float(), nullable=False),
    sa.Column('Humidity', sa.Float(), nullable=False),
    sa.Column('Temperature', sa.Float(), nullable=False),
    sa.Column('ph', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('time')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mitti')
    # ### end Alembic commands ###