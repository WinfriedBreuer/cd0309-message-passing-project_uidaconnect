import json
import logging
import os
from datetime import datetime
from typing import Dict

import psycopg2
from kafka import KafkaConsumer
from marshmallow import Schema, fields

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
KAFKA_URL = os.environ["KAFKA_URL"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class LocationSchema(Schema):
    person_id = fields.Integer(attribute="person_id")
    longitude = fields.String(attribute="longitude")
    latitude = fields.String(attribute="latitude")


def validate_location(location_message):
    logger.info(f"Validating message: {location_message}")

    # Deserialize the message to a dictionary
    # Assuming the message is in JSON format
    try:
        location_dict = json.loads(location_message)
    except Exception as e:
        logger.error(f"Error deserializing message: {location_message}, reason: {e}")
        logger.warning(f"Message was not a dictionary: {location_message}")
        return False

    # Validate the JSON message against the schema
    validation_result: Dict = LocationSchema().validate(location_dict)
    if validation_result:
        logger.warning(
            f"Error in schema format: {location_dict}, reason: {validation_result}"
        )
        return False

    return True


def insert_location_into_db(conn, location_message):
    location_dict = json.loads(location_message)
    with conn.cursor() as cursor:
        try:
            insert_sql = "INSERT INTO location (person_id, coordinate, creation_time) VALUES ({}, ST_Point({}, {}), '{}')".format(
                int(location_dict["person_id"]),
                float(location_dict["latitude"]),
                float(location_dict["longitude"]),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            cursor.execute(insert_sql)
            conn.commit()
            logger.info(f"Inserted message into database: {location_message}")
            cursor.close()
        except Exception as e:
            logger.error(f"error when inserting message . reason: {e}")


# Create the kafka consumer
kafka_location_consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[KAFKA_URL],
    auto_offset_reset='earliest',     
    enable_auto_commit=True,
    value_deserializer=lambda m: m.decode("utf-8"),
)

# connect to the database
with psycopg2.connect(
    database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
) as conn:
    conn.autocommit = True
    logger.info(f"Connected to the database: {DB_NAME}")

    # iterate over the messages in the location topic
    for location_message_dict in kafka_location_consumer:        
        if validate_location(location_message_dict.value):
            logger.info(f"Valid message: {location_message_dict.value}")

            # Insert the message into the database
            insert_location_into_db(conn, location_message_dict.value)
        else: 
            logger.warning(f"Invalid message: {location_message_dict.value}")

    conn.close()