from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = create_async_engine(url=DATABASE_URL, echo=True)


async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    permission = Column(JSON)
    users = relationship('User', cascade='all, delete')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role')
    announcemets = relationship('Announcement', cascade='all, delete')
    comments = relationship('Comment')


class AnnouncementType(Base):
    __tablename__ = 'announcement_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    announcements = relationship('Announcement', cascade='all, delete')


class Announcement(Base):
    __tablename__ = 'announcements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    type_id = Column(Integer, ForeignKey('announcement_types.id'))
    type = relationship('AnnouncementType')
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User')
    comments = relationship('Comment', cascade='all, delete')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    owner = relationship('User')
    announcement_id = Column(Integer, ForeignKey('announcements.id'))
    announcement = relationship('Announcement')


# async def get_session():
#     async with engine.begin() as connection:
#         await connection.run_sync(Base.metadata.drop_all)
#         await connection.run_sync(Base.metadata.create_all)


# asyncio.run(get_session())
