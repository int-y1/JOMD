"""Refactor models

Revision ID: 83344019a25b
Revises: 94b640653b2d
Create Date: 2021-07-05 21:09:51.209119

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm, TypeDecorator, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Gitgud(Base):
    __tablename__ = 'gitgud'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    handle = sa.Column(sa.String, index=True)
    guild_id = sa.Column(sa.Integer, index=True)
    point = sa.Column(sa.Integer)
    problem_id = sa.Column(sa.String, sa.ForeignKey('problem.code'))
    time = sa.Column(sa.DateTime, index=True)


class CurrentGitgud(Base):
    __tablename__ = 'current_gitgud'

    id = sa.Column(sa.Integer, primary_key=True)
    handle = sa.Column(sa.String)
    guild_id = sa.Column(sa.Integer)
    problem_id = sa.Column(sa.String, sa.ForeignKey('problem.code'))
    point = sa.Column(sa.Integer)
    time = sa.Column(sa.DateTime, index=True)


class Problem(Base):
    __tablename__ = 'problem'

    code = sa.Column(sa.String, primary_key=True)

# revision identifiers, used by Alembic.
revision = '83344019a25b'
down_revision = '94b640653b2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    op.drop_table('contest')
    op.drop_table('contest_organization')
    op.drop_table('contest_participation')
    op.drop_table('contest_problem')
    op.drop_table('contest_user')
    op.drop_table('judge')
    op.drop_table('judge_language')
    op.drop_table('language')
    op.drop_table('language_problem')
    op.drop_table('language_submission')
    op.drop_table('organization')
    op.drop_table('organization_problem')
    op.drop_table('organization_user')
    op.drop_table('participation')
    op.drop_table('participation_user')
    op.drop_table('problem')
    op.drop_table('problem_submission')
    op.drop_table('problem_user')
    op.drop_table('submission')
    op.drop_table('submission_user')
    op.drop_table('user')

    op.create_table('contest',
                    sa.Column('key', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('start_time', sa.DateTime(), nullable=True),
                    sa.Column('end_time', sa.DateTime(), nullable=True),
                    sa.Column('time_limit', sa.Float(), nullable=True),
                    sa.Column('is_rated', sa.Boolean(), nullable=True),
                    sa.Column('rate_all', sa.Boolean(), nullable=True),
                    sa.Column('has_rating', sa.Boolean(), nullable=True),
                    sa.Column('rating_floor', sa.Integer(), nullable=True),
                    sa.Column('rating_ceiling', sa.Integer(), nullable=True),
                    sa.Column('hidden_scoreboard', sa.Boolean(), nullable=True),
                    sa.Column('scoreboard_visibility', sa.String(), nullable=True),
                    sa.Column('is_organization_private', sa.Boolean(), nullable=True),
                    sa.Column('is_private', sa.Boolean(), nullable=True),
                    sa.Column('format__name', sa.String(), nullable=True),
                    sa.Column('format__config__cumtime', sa.Boolean(), nullable=True),
                    sa.Column('format__config__first_ac_bonus', sa.Integer(), nullable=True),
                    sa.Column('format__config__time_bonus', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('key')
                    )
    op.create_index(op.f('ix_contest_end_time'), 'contest', ['end_time'], unique=False)
    op.create_index(op.f('ix_contest_hidden_scoreboard'), 'contest', ['hidden_scoreboard'], unique=False)
    op.create_index(op.f('ix_contest_is_organization_private'), 'contest', ['is_organization_private'], unique=False)
    op.create_index(op.f('ix_contest_is_private'), 'contest', ['is_private'], unique=False)
    op.create_index(op.f('ix_contest_name'), 'contest', ['name'], unique=False)
    op.create_index(op.f('ix_contest_scoreboard_visibility'), 'contest', ['scoreboard_visibility'], unique=False)
    op.create_index(op.f('ix_contest_start_time'), 'contest', ['start_time'], unique=False)
    op.create_table('judge',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('start_time', sa.DateTime(), nullable=True),
                    sa.Column('ping', sa.Float(), nullable=True),
                    sa.Column('load', sa.Float(), nullable=True),
                    sa.PrimaryKeyConstraint('name')
                    )
    op.create_table('language',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('key', sa.String(), nullable=True),
                    sa.Column('short_name', sa.String(), nullable=True),
                    sa.Column('common_name', sa.String(), nullable=True),
                    sa.Column('ace_mode_name', sa.String(), nullable=True),
                    sa.Column('pygments_name', sa.String(), nullable=True),
                    sa.Column('code_template', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_language_key'), 'language', ['key'], unique=False)
    op.create_table('organization',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('slug', sa.String(), nullable=True),
                    sa.Column('short_name', sa.String(), nullable=True),
                    sa.Column('is_open', sa.Boolean(), nullable=True),
                    sa.Column('member_count', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_organization_slug'), 'organization', ['slug'], unique=False)
    op.create_table('problem',
                    sa.Column('code', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('group', sa.String(), nullable=True),
                    sa.Column('time_limit', sa.Float(), nullable=True),
                    sa.Column('memory_limit', sa.Integer(), nullable=True),
                    sa.Column('points', sa.Integer(), nullable=True),
                    sa.Column('partial', sa.Boolean(), nullable=True),
                    sa.Column('short_circuit', sa.Boolean(), nullable=True),
                    sa.Column('is_organization_private', sa.Boolean(), nullable=True),
                    sa.Column('is_public', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('code')
                    )
    op.create_index(op.f('ix_problem_group'), 'problem', ['group'], unique=False)
    op.create_index(op.f('ix_problem_is_organization_private'), 'problem', ['is_organization_private'], unique=False)
    op.create_index(op.f('ix_problem_is_public'), 'problem', ['is_public'], unique=False)
    op.create_index(op.f('ix_problem_name'), 'problem', ['name'], unique=False)
    op.create_index(op.f('ix_problem_points'), 'problem', ['points'], unique=False)
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=True),
                    sa.Column('points', sa.Float(), nullable=True),
                    sa.Column('performance_points', sa.Float(), nullable=True),
                    sa.Column('problem_count', sa.Integer(), nullable=True),
                    sa.Column('rank', sa.String(), nullable=True),
                    sa.Column('rating', sa.Integer(), nullable=True),
                    sa.Column('volatility', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_points'), 'user', ['points'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('contest_organization',
                    sa.Column('contest_id', sa.String(), nullable=False),
                    sa.Column('organization_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['contest_id'], ['contest.key'], ),
                    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
                    sa.PrimaryKeyConstraint('contest_id', 'organization_id')
                    )
    op.create_table('contest_problem',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('is_pretested', sa.Boolean(), nullable=True),
                    sa.Column('max_submissions', sa.Integer(), nullable=True),
                    sa.Column('label', sa.String(), nullable=True),
                    sa.Column('problem_id', sa.String(), nullable=True),
                    sa.Column('contest_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['contest_id'], ['contest.key'], ),
                    sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_contest_problem_is_pretested'), 'contest_problem', ['is_pretested'], unique=False)
    op.create_index(op.f('ix_contest_problem_label'), 'contest_problem', ['label'], unique=False)
    op.create_index(op.f('ix_contest_problem_max_submissions'), 'contest_problem', ['max_submissions'], unique=False)
    op.create_table('contest_tag',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('tag', sa.String(), nullable=True),
                    sa.Column('contest_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['contest_id'], ['contest.key'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_contest_tag_tag'), 'contest_tag', ['tag'], unique=False)

    rs = list(session.execute('select * from current_gitgud'))

    op.drop_table('current_gitgud')

    op.create_table('current_gitgud',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('handle', sa.String(), nullable=True),
        sa.Column('guild_id', sa.Integer(), nullable=True),
        sa.Column('problem_id', sa.String(), nullable=True),
        sa.Column('point', sa.Integer(), nullable=True),
        sa.Column('time', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_current_gitgud_time'), 'current_gitgud', ['time'], unique=False)

    for row in rs:
        row = dict(row)
        row['id'] = row['_id']
        del row['_id']
        row['time'] = datetime.fromisoformat(row['time'])
        session.add(CurrentGitgud(**row))

    session.commit()

    rs = list(session.execute('select * from gitgud'))

    op.drop_table('gitgud')

    op.create_table('gitgud',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('handle', sa.String(), nullable=True),
        sa.Column('guild_id', sa.Integer(), nullable=True),
        sa.Column('point', sa.Integer(), nullable=True),
        sa.Column('problem_id', sa.String(), nullable=True),
        sa.Column('time', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gitgud_guild_id'), 'gitgud', ['guild_id'], unique=False)
    op.create_index(op.f('ix_gitgud_handle'), 'gitgud', ['handle'], unique=False)
    op.create_index(op.f('ix_gitgud_time'), 'gitgud', ['time'], unique=False)

    for row in rs:
        row = dict(row)
        row['id'] = row['_id']
        del row['_id']
        row['time'] = datetime.fromisoformat(row['time'])
        session.add(Gitgud(**row))

    session.commit()

    op.create_table('judge_language',
                    sa.Column('judge_id', sa.String(), nullable=False),
                    sa.Column('language_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['judge_id'], ['judge.name'], ),
                    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ),
                    sa.PrimaryKeyConstraint('judge_id', 'language_id')
                    )
    op.create_table('language_problem',
                    sa.Column('problem_id', sa.String(), nullable=False),
                    sa.Column('language_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ),
                    sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
                    sa.PrimaryKeyConstraint('problem_id', 'language_id')
                    )
    op.create_table('organization_problem',
                    sa.Column('problem_id', sa.String(), nullable=False),
                    sa.Column('organization_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
                    sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
                    sa.PrimaryKeyConstraint('problem_id', 'organization_id')
                    )
    op.create_table('organization_user',
                    sa.Column('organization_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('organization_id', 'user_id')
                    )
    op.create_table('participation',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('start_time', sa.DateTime(), nullable=True),
                    sa.Column('end_time', sa.DateTime(), nullable=True),
                    sa.Column('score', sa.Float(), nullable=True),
                    sa.Column('cumulative_time', sa.Integer(), nullable=True),
                    sa.Column('tiebreaker', sa.Float(), nullable=True),
                    sa.Column('old_rating', sa.Integer(), nullable=True),
                    sa.Column('new_rating', sa.Integer(), nullable=True),
                    sa.Column('is_disqualified', sa.Boolean(), nullable=True),
                    sa.Column('virtual_participation_number', sa.Integer(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('contest_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['contest_id'], ['contest.key'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('problem_language_limit',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('type', sa.Integer(), nullable=True),
                    sa.Column('language_id', sa.String(), nullable=True),
                    sa.Column('time_limit', sa.Float(), nullable=True),
                    sa.Column('memory_limit', sa.Integer(), nullable=True),
                    sa.Column('problem_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['language_id'], ['language.key'], ),
                    sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_problem_language_limit_type'), 'problem_language_limit', ['type'], unique=False)
    op.create_table('problem_type',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('type', sa.Integer(), nullable=True),
                    sa.Column('problem_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_problem_type_type'), 'problem_type', ['type'], unique=False)
    op.create_table('problem_user',
                    sa.Column('problem_code', sa.String(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['problem_code'], ['problem.code'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('problem_code', 'user_id')
                    )
    op.create_table('submission',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date', sa.DateTime(), nullable=True),
                    sa.Column('time', sa.Float(), nullable=True),
                    sa.Column('memory', sa.Float(), nullable=True),
                    sa.Column('points', sa.Float(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('result', sa.String(), nullable=True),
                    sa.Column('case_points', sa.Float(), nullable=True),
                    sa.Column('case_total', sa.Float(), nullable=True),
                    sa.Column('problem_id', sa.String(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('language_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ),
                    sa.ForeignKeyConstraint(['problem_id'], ['problem.code'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_submission_date'), 'submission', ['date'], unique=False)
    op.create_table('user_volatility',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('volatility', sa.Integer(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_volatility_volatility'), 'user_volatility', ['volatility'], unique=False)
    op.create_table('participation_solution',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('points', sa.Float(), nullable=True),
                    sa.Column('time', sa.Float(), nullable=True),
                    sa.Column('participation_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['participation_id'], ['participation.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('contest_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['contest_id'], ['contest.key'], ),
                    )
    op.create_index(op.f('ix_participation_solution_points'), 'participation_solution', ['points'], unique=False)
    op.create_table('participation_user',
                    sa.Column('participation_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['participation_id'], ['participation.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('participation_id', 'user_id')
                    )
    op.create_table('submission_case',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('type', sa.String(), nullable=True),
                    sa.Column('case_id', sa.Integer(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('time', sa.Float(), nullable=True),
                    sa.Column('memory', sa.Float(), nullable=True),
                    sa.Column('points', sa.Float(), nullable=True),
                    sa.Column('total', sa.Float(), nullable=True),
                    sa.Column('submission_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['submission_id'], ['submission.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_submission_case_points'), 'submission_case', ['points'], unique=False)
    op.create_index(op.f('ix_submission_case_total'), 'submission_case', ['total'], unique=False)


def downgrade():
    pass
    # Uhh yeah, screw downgrades
    # ### end Alembic commands ###
