CREATE DATABASE api_logs;
\c api_logs;

CREATE TABLE IF NOT EXISTS log (
    id uuid PRIMARY KEY,
    request_data TEXT,
    response_data TEXT,
    created_at timestamp with time zone
);