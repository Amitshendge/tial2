from datetime import datetime
from flask import *
import time
from azure.storage.queue import QueueClient,BinaryBase64EncodePolicy,BinaryBase64DecodePolicy
from . import app

connq='DefaultEndpointsProtocol=https;AccountName=cohortdataengg;AccountKey=Ib4rKMs9yjmfhhu1JxshP3oTQr30pSeuQY+9Kc5pzzQ3xlpOgB0xfh3QkTtDu3iXg/iYBag0HIhRPRfd7E9qnQ==;EndpointSuffix=core.windows.net'
class practice():
    def __init__(self) -> None:
        self.a=True
    def stop_loop(self):
        self.a=False
    def start_loop(self):
        self.a=True
        self.run()

    def run(self):
        while self.a:
            base64_queue_client = QueueClient.from_connection_string(
                                conn_str=connq, queue_name='trial',
                                message_encode_policy = BinaryBase64EncodePolicy(),
                                message_decode_policy = BinaryBase64DecodePolicy()
                            )
            input_message=str("message").encode('utf8')
            base64_queue_client.send_message(input_message)
            print("message added to queue")
            time.sleep(5)

testing=practice()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/result',methods=['POST','GET'])
def result():
    output=request.form.to_dict()
    name=output["name"]
    outing=name
    if (name.lower()=="start"):
        outing="started"
        print(outing)
        testing.start_loop()
    elif (name.lower()=="stop"):
        outing="stopped"
        print(outing)
        testing.stop_loop()
    else:
        outing="cannot start or stop (wrong input FOUND!!!)"
    return render_template('index.html',name=outing)
