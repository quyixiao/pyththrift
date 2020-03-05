from thrift import Thrift
from thrift.protocol.TCompactProtocol import TCompactProtocol

from thrift.transport import TSocket, TTransport

from py.thrift.generated import PersonService, ttypes

try:
    tSocket = TSocket.TSocket("localhost", 8899)
    tSocket.setTimeout(600)
    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol(transport)
    client = PersonService.Client(protocol)
    transport.open()
    person = client.getPersonByUsername("张三")

    print(person.username)
    print(person.age)
    print(person.married)

    print('-------------------------')

    newPerson = ttypes.Person()
    newPerson.username = "李四"
    newPerson.age = 30
    newPerson.married = True

    client.savePerson(newPerson)
    transport.close()




except Exception as e:
    print(e)
