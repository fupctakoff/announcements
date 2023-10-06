from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import declarative_base, relationship


# DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# engine = create_async_engine(url=DATABASE_URL, echo=True)


# async_session = sessionmaker(
#     engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    permission = Column(JSON)
    users = relationship('User', cascade='all, delete')


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    name = Column(String)
    hashed_password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role')
    announcemets = relationship('Announcement', cascade='all, delete')
    comments = relationship('Comment')
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


class AnnouncementType(Base):
    __tablename__ = 'announcementtype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    announcements = relationship('Announcement', cascade='all, delete')


class Announcement(Base):
    __tablename__ = 'announcement'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    type_id = Column(Integer, ForeignKey('announcementtype.id'))
    type = relationship('AnnouncementType')
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User')
    comments = relationship('Comment', cascade='all, delete')


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    owner = relationship('User')
    announcement_id = Column(Integer, ForeignKey('announcement.id'))
    announcement = relationship('Announcement')


# async def get_session():
#     async with engine.begin() as connection:

#         await connection.run_sync(Base.metadata.drop_all)
#         await connection.run_sync(Base.metadata.create_all)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session() as session:
#         yield session


# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)


# asyncio.run(get_session())
