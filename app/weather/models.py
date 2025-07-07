from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Double
from sqlalchemy.orm import relationship

from app.database import Base



class Weather(Base):
    __tablename__ = 'weather'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    city = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    temperature = Column(Double, nullable=False)
    request_datatime = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="weathers")

    def __repr__(self):
        return f"city={self.city}, temperature={self.temperature}, request datetime={self.request_datatime}"
