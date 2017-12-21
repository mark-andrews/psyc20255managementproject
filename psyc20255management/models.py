'''
The database model for psyc20255.

Key characteristics of the database.

* There are N `Student`s (in 2017, N is around 500), and each one is assigned to
one and only one `LabGroup`.
* There are K `LabGroup`s, with each meeting in a particular room on a
particular day of the week and at a particular time.

'''

from sqlalchemy import (Column, 
                        ForeignKey, 
                        String, 
                        Integer, 
                        DateTime,
                        Boolean,
                        UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class LabGroup(Base):

    '''
    All students are assigned to one lab group. This group will meet once per
    week in a particular lab room, usually Ch5111, Ch425 or Ch424, at the same
    day and time each week. Each group has a number like 'SH 1', 'SH 2', etc.

    * uid (string), e.g. 'SH 1'
    * room (string), e.g. 'Chaucer, 5111'
    * weekday (string), e.g. 'Monday'
    * time (string), e.g. '09:00-12:00'

    Each lab group has a one-to-many relationship with the Student class.
    '''

    __tablename__ = 'labgroup'

    uid = Column(String(7), primary_key = True)

    room = Column(String(50))

    weekday = Column(String(10))
    time = Column(String(12))

class Student(Base):

    '''
    A student has a unique 8 character student ID (from which their email
    address is determined). They also have a first name and lastname.

    uid (string), e.g. 'N0606123'
    firstname (string), e.g. 'Billy Bob'
    lastname (string), e.g. 'Foo Bar'

    Each student has a many to one relationship with LabGroup.

    '''

    __tablename__ = 'student'

    uid = Column(String(8), primary_key = True)

    firstname = Column(String(100))
    lastname = Column(String(100))

    labgroup_id = Column(String, ForeignKey('labgroup.uid'))

class Sequence(Base):
    '''
    A lab sequence is either 'Psychometrics', 'Experimental', 'Qualitative'

    name (string), e.g. 'Experimental'

    '''
    __tablename__ = 'sequence'

    name = Column(String(25), primary_key=True)


class Lecturer(Base):

    '''
    Each lecturer is a member of academic staff, either a lecturer or associate
    professor or professor or an hourly paid lecturer (HPL). They'll all have
    staff accounts and an NTU staff email address.

    uid (string), e.g. psy3andrem
    firstname (string), e.g. 'Mary Beth'
    lastname (string), e.g. 'Baz Foo'
    email (string), e.g. 'mark.andrews@ntu.ac.uk'

    '''
    __tablename__ = 'lecturer'

    uid = Column(String(15), primary_key = True)
    firstname = Column(String(25))
    lastname = Column(String(25))
    email = Column(String(100), unique = True)


class LabGroupSequence(Base):

    __tablename__ = 'labgroup_sequence'
    __table_args__ = tuple(UniqueConstraint('labgroup_id', 'sequence_id'))

    uid = Column(Integer, primary_key = True)

    labgroup_id = Column(String, ForeignKey('labgroup.uid'))
    sequence_id = Column(String, ForeignKey('sequence.name'))

class LabGroupTeam(Base):

    __tablename__ = 'labgroup_sequence_team'

    uid = Column(Integer, primary_key = True)
    name = Column(String(25))

    labgroup_sequence_id = Column(Integer, ForeignKey('labgroup_sequence.uid'))
    student = Column(String, ForeignKey('student.uid'), unique=True)


class LabGroupSequenceLecturer(Base):

    __tablename__ = 'labgroup_sequence_lecturer'
    __table_args__ = (UniqueConstraint('labgroup_sequence_id', 'lecturer_id'),)

    uid = Column(Integer, primary_key = True)

    labgroup_sequence_id = Column(Integer, ForeignKey('labgroup.uid'))
    lecturer_id = Column(Integer, ForeignKey('lecturer.uid'))


class Report(Base):

    __tablename__ = 'report'
    __table_args__ = (UniqueConstraint('student', 'sequence'),)

    uid = Column(Integer, primary_key = True)

    # File info
    original_filename = Column(String(100))
    renamed_filename = Column(String(100))

    checksum = Column(String(100))

    timestamp = Column(DateTime)
    #########

    student = Column(String, ForeignKey('student.uid'))
    sequence = Column(String, ForeignKey('sequence.name'))
    marker = Column(String, ForeignKey('lecturer.uid'))

    # Grade 
    is_graded = Column(Boolean)
    grade = Column(String(4))
