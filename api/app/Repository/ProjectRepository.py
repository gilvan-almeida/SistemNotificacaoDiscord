from sqlalchemy.orm import Session
from models.Project import Project

class ProjectRepository:

    @staticmethod
    def criarProjectRepository(db: Session, project: Project):
        db.add(project)
        db.commit()
        db.refresh(project)
        return project
    
    @staticmethod
    def getProject(db: Session, idProject: int):
        return db.query(Project).filter(Project.id == idProject).first()
    
    @staticmethod
    def editProjectRepository(db: Session, id: int, project: dict):
        projectDate = ProjectRepository.getProject(db, id)

        if not projectDate:
            return None
        
        for camp, valor in project.items():
            setattr(projectDate, camp, valor)

        db.commit()
        db.refresh(projectDate)

        return projectDate