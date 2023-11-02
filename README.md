# kafka-tutorial

Install zookeeper and kafka by docker
```
docker compose up -d --build
```

Install environment
```
cd project_name

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Run these 2 command on 2 difference command line:
```
python3 consumer.py
python3 producer.py
```

Note:

Kafka send message by binary, so we have to convert to binary before send message

Kafka wont send the message that didn't encode to binary