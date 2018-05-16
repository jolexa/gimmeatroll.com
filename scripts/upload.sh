#!/bin/bash

cd ${PWD}
aws s3 mv --acl public-read ${1} s3://gimmeatroll.com/
cd -
