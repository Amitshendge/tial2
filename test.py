from azure.storage.queue import QueueClient,BinaryBase64EncodePolicy,BinaryBase64DecodePolicy


connq='DefaultEndpointsProtocol=https;AccountName=cohortdataengg;AccountKey=Ib4rKMs9yjmfhhu1JxshP3oTQr30pSeuQY+9Kc5pzzQ3xlpOgB0xfh3QkTtDu3iXg/iYBag0HIhRPRfd7E9qnQ==;EndpointSuffix=core.windows.net'

def que_message():
    base64_queue_client = QueueClient.from_connection_string(
                            conn_str=connq, queue_name='trial',
                            message_encode_policy = BinaryBase64EncodePolicy(),
                            message_decode_policy = BinaryBase64DecodePolicy()
                        )
    input_message=str("message").encode('utf8')
    base64_queue_client.send_message(input_message)
    print("message added to queue")

que_message()