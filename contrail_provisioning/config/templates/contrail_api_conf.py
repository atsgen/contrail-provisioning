import string

template = string.Template("""
[DEFAULTS]
ifmap_server_ip=$__contrail_ifmap_server_ip__
ifmap_server_port=$__contrail_ifmap_server_port__
ifmap_username=$__contrail_ifmap_username__
ifmap_password=$__contrail_ifmap_password__
cassandra_server_list=$__contrail_cassandra_server_list__
listen_ip_addr=$__contrail_listen_ip_addr__
listen_port=$__contrail_listen_port__
multi_tenancy=$__contrail_multi_tenancy__
log_file=$__contrail_log_file__
log_local=1
log_level=SYS_NOTICE
disc_server_ip=$__contrail_disc_server_ip__
disc_server_port=$__contrail_disc_server_port__
zk_server_ip=$__contrail_zookeeper_server_ip__
redis_server_ip=$__contrail_redis_ip__
rabbit_server=$__rabbit_server_ip__
rabbit_port=$__rabbit_server_port__
list_optimization_enabled=True
# Sandesh send rate limit can be used to throttle system logs transmitted per
# second. System logs are dropped if the sending rate is exceeded
# sandesh_send_rate_limit=100

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__
""")
