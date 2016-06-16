import boto3
import ConfigParser
import tempfile


class ConfigFromS3(object):

    def __init__(self, bucket_name, key, region_name):
        """Read configuration file from S3 and parse it"""
        defaults = {
            "aws_region": region_name
        }
        session = boto3.session.Session(region_name=region_name)
        self.bucket = session.resource('s3').Bucket(bucket_name)
        temporary_file = tempfile.NamedTemporaryFile()
        self.bucket.download_file(key, temporary_file.name)
        self.config = ConfigParser.ConfigParser(defaults=defaults)
        with open(temporary_file.name, 'r') as f:
            self.config.readfp(f)
        temporary_file.close()
