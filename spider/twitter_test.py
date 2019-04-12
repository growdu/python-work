import facebook

graph = facebook.GraphAPI(access_token="800540000327990|umAuETUaHdTnjLcc_ifBoYXypm4", version="2.12")
friends = graph.get_connections(id='me', connection_name='friends')
comments = graph.get_connections(id='post_id', connection_name='comments')
