from pydantic import BaseModel, Field
from crewai import Agent
from typing import Dict, Any

class Task(BaseModel):
    """
    A class representing a task in CrewAI. Each task is associated with an agent and contains a description, expected output, and optional inputs.
    """
    description: str = Field(..., description="A brief description of the task")
    agent: Agent = Field(..., description="The agent assigned to this task")
    expected_output: Any = Field(..., description="The expected outcome of the task")
    inputs: Dict[str, Any] = Field(default_factory=dict, description="Input data required for the task")
    config: Dict[str, Any] = Field(default_factory=dict, description="Configuration settings for the task")  # Add config here

    def execute(self):
        """
        Executes the task using the assigned agent.
        """
        print(f"Task Description: {self.description}")
        print(f"Executing task with agent: {self.agent.role}")
        
        # Execute the task logic here using the agent
        output = self.agent.llm.generate(prompt=self.description, **self.inputs)
        print(f"Task completed. Output: {output}")
        return output
