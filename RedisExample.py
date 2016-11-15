#!/usr/bin/python
import sys
import redis


def getKeyValue(redisPool, variable_name):
    redisServer = redis.Redis(connection_pool=redisPool)
    response = redisServer.get(variable_name)
    
    return response


def setKeyValue(redisPool, variable_name, variable_value):
    redisServer = redis.Redis(connection_pool=redisPool)
    redisServer.set(variable_name, variable_value)


def delKeyValue(redisPool, variable_name, variable_value):
    redisServer = redis.Redis(connection_pool=redisPool)
    redisServer.delete(variable_name, variable_value)


def main():
	redisPool = redis.ConnectionPool(host='172.17.0.2', port=6379, db=0)
	setKeyValue(redisPool, "chave:subchave", "valor")
	if getKeyValue(redisPool, "chave:subchave") is not None:
		print(getKeyValue(redisPool, "chave:subchave"))
	delKeyValue(redisPool, "chave:subchave", "valor")
	print(getKeyValue(redisPool, "chave:subchave"))



if __name__ == '__main__':
		sys.exit(main())