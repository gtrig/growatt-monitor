from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import json

# Create a new client
class InfluxDB2Client:
    def __init__(self, url, token, org, default_bucket=None):
        self.bucket = default_bucket
        self.client = InfluxDBClient(url=url, token=token, org=org)

    def write(self, record, bucket=None):
        if bucket is None: bucket = self.bucket
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, record=record)

    def writeJson(self, json, bucket=None):
        if bucket is None: bucket = self.bucket
        record = json.loads(json)
        p = Point.from_dict(json)
        self.client.write_api().write(bucket=bucket, record=p)

    def query(self, query):
        return self.client.query_api().query(query)

    def close(self):
        self.client.close()