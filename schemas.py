from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


class Category(str, Enum):
    TEACHING = "Teaching"
    INFRASTRUCTURE = "Infrastructure"
    COURSE = "Course"
    OTHER = "Other"


class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class FeedbackAnalysis(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    sentiment: Sentiment
    category: Category
    priority: Priority
    summary: str = Field(min_length=5, max_length=300)
    reason: str = Field(min_length=5, max_length=500)
