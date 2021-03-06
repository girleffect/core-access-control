"""empty message

Revision ID: bf47ce5e7e69
Revises: f826c9bf9577
Create Date: 2018-11-21 10:36:28.840070

"""
import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm


# revision identifiers, used by Alembic.
revision = 'bf47ce5e7e69'
down_revision = 'f826c9bf9577'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deletion_method',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.VARCHAR(length=100), nullable=False),
    sa.Column('data_schema', sa.JSON(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deletion_method_label'), 'deletion_method', ['label'], unique=True)

    # NOTE: server_default added manually
    op.add_column('site', sa.Column('deletion_method_data', sa.JSON(), nullable=False, server_default='{}'))
    op.add_column('site', sa.Column('deletion_method_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'site', 'deletion_method', ['deletion_method_id'], ['id'])
    # ### end Alembic commands ###

    # DATA MIGRATION
    op.execute(
        "INSERT INTO deletion_method (id, label, data_schema, description, created_at, updated_at)"
        " VALUES ('0', 'none', '{\"type\": \"object\", \"additionalProperties\": false, \"properties\": {}}',"
        f" 'None type method', '{datetime.datetime(1970, 1, 1, 0, 0, 0).isoformat()}', '{datetime.datetime(1970, 1, 1, 0, 0, 0).isoformat()}');"
    )
    op.execute("UPDATE site SET deletion_method_id=0;")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'site', type_='foreignkey')
    op.drop_column('site', 'deletion_method_id')
    op.drop_column('site', 'deletion_method_data')
    op.drop_index(op.f('ix_deletion_method_label'), table_name='deletion_method')
    op.drop_table('deletion_method')
    # ### end Alembic commands ###
