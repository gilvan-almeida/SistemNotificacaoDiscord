from config.database import engine
from models.Task import Task
from models.Usuario import Usuario
from models.SecaoTask import SecaoTask
from models.ReportTask import ReportTask
from models.TaskHistory import taskHistory
from models.Files import Files


Task.__table__.create(bind=engine, checkfirst=True)
Usuario.__table__.create(bind=engine, checkfirst=True)
SecaoTask.__table__.create(bind=engine, checkfirst=True)
ReportTask.__table__.create(bind = engine, checkfirst = True)
taskHistory.__table__.create(bind = engine, checkfirst = True)
Files.__table__.create(bind = engine, checkfirst = True)