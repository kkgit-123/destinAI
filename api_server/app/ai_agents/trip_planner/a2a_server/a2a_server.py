# a2a_server.py
import uvicorn
from python_a2a import A2AServer, run_server
from agent import trip_planner

class TripPipelineA2AServer(A2AServer):
    async def handle_task(self, task):
        # Use your agent orchestrator to process the incoming task message
        user_input = task.message["content"]["text"]
        result = await trip_planner.run_chain({"prompt": user_input})
        
        task.artifacts = [{
            "parts": [{"type": "text", "text": result}]
        }]
        task.status = task.status.COMPLETED
        return task

if __name__ == "__main__":
    server = TripPipelineA2AServer(agent_card=trip_planner.agent_card)
    run_server(server, host="0.0.0.0", port=8000)
