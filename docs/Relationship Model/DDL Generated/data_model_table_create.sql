CREATE TABLE IF NOT EXISTS user (
    nickname text NOT NULL,
    name text NOT NULL,
    password text NOT NULL,
    PRIMARY KEY (nickname)
);


CREATE TABLE IF NOT EXISTS room (
    id text NOT NULL,
    name text NOT NULL,
    max_number_of_participants integer NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS message (
    id text NOT NULL,
    sender_id text NOT NULL,
    receiver_id text NOT NULL,
    content_id text NOT NULL,
    type integer NOT NULL,
    date text NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id, sender_id, receiver_id),
    FOREIGN KEY (sender_id) REFERENCES user(nickname) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES user(nickname) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_message_sender_id ON message
    (sender_id);
CREATE INDEX IF NOT EXISTS idx_message_receiver_id ON message
    (receiver_id);


CREATE TABLE IF NOT EXISTS file (
    id text NOT NULL,
    name text NOT NULL,
    content bytea NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS room_messages (
    message_id text NOT NULL,
    room_id text NOT NULL,
    FOREIGN KEY (message_id) REFERENCES message(id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES room(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_room_messages_message_id ON room_messages
    (message_id);
CREATE INDEX IF NOT EXISTS idx_room_messages_room_id ON room_messages
    (room_id);


CREATE TABLE IF NOT EXISTS words (
    id text NOT NULL,
    content text NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS participants (
    user_id text NOT NULL,
    room_id text NOT NULL,
    UNIQUE (user_id, room_id),
    FOREIGN KEY (user_id) REFERENCES user(nickname) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES room(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_participants_user_id ON participants
    (user_id);
CREATE INDEX IF NOT EXISTS idx_participants_room_id ON participants
    (room_id);