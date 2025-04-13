def get_user_topics():
    return [
        {
            "name": "user-events",
            "partitions": 3,
            "replication_factor": 1,
        }
    ]
