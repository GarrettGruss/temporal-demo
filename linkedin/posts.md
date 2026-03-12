## Structure

Discuss the anatomy of a temporal project. 
- Key folders include the `activities` and `workflows`
- Actual work is handled by the `worker`
- A process is required to add a job to the queue, this is handled by the `start_workflow.py` script

## Retry logic

A core offering of temporal is the retry logic. It combines built in retry logic with a historical replay log to create a durable execution that can store state, allowing restarts.