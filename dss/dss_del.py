import boto
import boto.s3.connection
#from boto.s3.key import Key
import os
import subprocess
import sys

import pdb
access_key = 'd4fe3da8ffe1409788b505630816ed8b'
secret_key = 'c835131dd45e4c4aa2d1dfa3f20b18c6'
bucket_name = 'rvrscss-cc1a6ae5-8e81'
host = 'dss.ind-west-1.internal.jiocloudservices.com'
#host = '10.140.214.250'
conn = boto.connect_s3(host=host,aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                       is_secure=True,
                       calling_format = boto.s3.connection.OrdinaryCallingFormat(),)
#pdb.set_trace()
cmdargs=str(sys.argv[1])
backup_bucket = None
bucket = conn.get_bucket(bucket_name)
if bucket != None:
    print bucket

print "deleting %s" % cmdargs
bucket.delete_key(cmdargs)
