"""
"""

# pylint: disable=too-few-public-methods
import enum
from sqlalchemy import Column, String, Integer, Enum
from src.infra.config import Base


class StatusType(enum.Enum):
    """Status Types"""

    DONE = "done"
    ON_HOLD = "on hold"
    IN_PROGRESS = "in progress"


class PriorityType(enum.Enum):
    """Priority Type"""

    IMPORTANT = "important"
    URGENT = "urgent"
    LOW_EFFORT = "low effort"


class Task(Base):
    """Task Entity"""

    __tablename__ = 'task'

    id_task = Column(Integer, autoincrement=True, primary_key=True)
    task = Column(String(100), nullable=False)
    status = Column(Enum(StatusType))
    priority = Column(Enum(PriorityType))
    start_date = Column(String(15), nullable=False)
    end_date = Column(String(15), nullable=True)

    def __repr__(self):
        return f'task {self.task}, status {self.status}, {self.priority}'
