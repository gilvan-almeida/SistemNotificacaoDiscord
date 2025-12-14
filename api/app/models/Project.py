from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config.database import Base

class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    organizationId  = Column(Integer, ForeignKey("organizations.id", ondelete = "CASCADE"), nullable = False)
    organization = relationship("Organization" , back_populates = "projects")