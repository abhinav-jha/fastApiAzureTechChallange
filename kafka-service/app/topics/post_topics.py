def get_post_topics():
    return [
        {
            "name": "post-events",
            "partitions": 3,
            "replication_factor": 1,
        }
    ]
