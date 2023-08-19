# broker
broker = "redis://127.0.0.1:6379/0",
backend = "redis://127.0.0.1:6379/0"
broker_pool_limit = 100
broker_heartbeat = 120
broker_connection_timeout = 4

# worker
worker_prefetch_multiplier = 4
worker_send_task_event = False
worker_cancel_long_running_tasks_on_connection_loss = False
worker_deduplicate_successful_tasks = True
worker_disable_rate_limits = True
worker_send_task_events = False
task_send_sent_event = False
task_track_started = False

task_routes = (
    [
        # plan tasks
        ('oopsdated.plan', {'queue': 'plan'}),

        # get target file from the repo
        ('oopsdated.scan', {'queue': 'scan'}),

        # extract outdated packages 
        ('oopsdated.extract', {'queue': 'extract'}),
    ],
)
