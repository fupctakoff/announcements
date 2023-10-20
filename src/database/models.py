from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    users = relationship('User', back_populates='role')


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    name = Column(String)
    hashed_password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey(
        'role.id', ondelete='SET NULL'), nullable=True)
    role = relationship('Role', back_populates='users')
    announcements = relationship('Announcement', back_populates='owner')
    comments = relationship('Comment', back_populates='owner')
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


class AnnouncementType(Base):
    __tablename__ = 'announcementtype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    announcements = relationship('Announcement', back_populates='type')


class Announcement(Base):
    __tablename__ = 'announcement'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    type_id = Column(Integer, ForeignKey(
        'announcementtype.id', ondelete='SET NULL'))
    type = relationship('AnnouncementType', back_populates='announcements')
    owner_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    owner = relationship('User', back_populates='announcements')
    comments = relationship(
        'Comment', back_populates='announcement', cascade='all, delete')


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    owner_id = Column(Integer, ForeignKey(
        'user.id', ondelete='SET NULL'), nullable=True)
    owner = relationship('User', back_populates='comments')
    announcement_id = Column(Integer, ForeignKey(
        'announcement.id', ondelete='CASCADE'))
    announcement = relationship('Announcement', back_populates='comments')


class EventType(Base):
    __tablename__ = 'eventtype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    events = relationship('Event', back_populates='type', primaryjoin="EventType.id == Event.type_id")


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    dresscode = Column(String)
    type_id = Column(Integer, ForeignKey(
        'eventtype.id', ondelete='SET NULL'))
    type = relationship('EventType', back_populates='events')
