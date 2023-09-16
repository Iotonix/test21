#!/bin/bash
docker build . -t lingo:2.13.2
docker tag lingo:2.13.2 registry.winstantpay.com/lingo:2.13.2
docker push registry.winstantpay.com/lingo:2.13.2
