from models.ReportTask import ReportTask
from sqlalchemy.orm import Session

class ReportTaskRepository:

    @staticmethod
    def criarReportTask(db: Session, reportTask: ReportTask):
        db.add(reportTask)
        db.commit()
        db.refresh(reportTask)
        return reportTask
    
    @staticmethod
    def getReportTask(db: Session, taskId: int):
        report = db.query(ReportTask).filter(ReportTask.taskId == taskId).first()
        return report