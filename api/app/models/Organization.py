from sqlalchemy import Column, Integer, String, DateTime
from config.database import Base

from sqlalchemy.orm import relationship


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    projects = relationship("Project", back_populates="organization")