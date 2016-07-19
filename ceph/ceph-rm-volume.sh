#!/bin/bash
#user="cinder"
conf="/etc/ceph/ceph.conf"
pool="sbs"
volume_id=$1

if [ -z $1 ];
then
    echo "Need to pass volume_id as first argument"
    exit
fi

rbd --conf $conf -p $pool rm "volume-$volume_id"
